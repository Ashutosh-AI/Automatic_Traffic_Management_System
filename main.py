import time
import cv2
import numpy as np

from detector import YoloDetector
from Utilities.utils import Utils
from deep_sort_realtime.deepsort_tracker import DeepSort
from Utilities.region_to_region import Region

detector = YoloDetector(model_name=None)
utils = Utils()
regions = Region()
object_tracker = DeepSort(max_age=15,      # if an object is not detected for 15 consecutive frames, its track will be terminated
                          n_init=2,
                          nms_max_overlap=1.0,
                          max_cosine_distance=0.3,
                          nn_budget=None,
                          override_track_class=None,
                          embedder="mobilenet",
                          half=True,
                          bgr=True,
                          embedder_gpu=True,
                          embedder_model_name=None,
                          embedder_wts=None,
                          polygon=False,
                          today=None)


cap = cv2.VideoCapture("TorontoIntersectionsOrignal.mp4")
count = 0

# Tracking vehicles
vehicles_entering = {}
vehicles_elasped_time = {}


try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("WebCam Closed")
            break

        height, width = frame.shape[0], frame.shape[1]
        frame = frame[350:height, 100:width-200]

        count+=1
        if count % 3 != 0:
            continue

        frame = utils.draw_roi_on_image(frame)

        start_time = time.time()

        results = detector.score_frame(frame)
        img, detections = detector.plot_boxes(results, frame, height=frame.shape[0], width=frame.shape[1], score_thresh=0.6)

        tracks = object_tracker.update_tracks(detections, frame=img)

        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            ltrb = track.to_ltrb()
            bbox = ltrb

            #cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0,0,255), 2)
            #cv2.putText(img, "ID: " + str(track_id), (int(bbox[0]), int(bbox[1]-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            result = utils.isPoint_inside_region4_Bottom(bbox)
            if result:
                vehicles_entering[track_id] = time.time()

            if track_id in vehicles_entering:
                result = utils.isPoint_inside_region2_Top(bbox)

                if result:
                    elasped_time = time.time() - vehicles_entering[track_id]

                    if track_id not in vehicles_elasped_time:
                        vehicles_elasped_time[track_id] = elasped_time

                    if track_id in vehicles_elasped_time:
                        elasped_time = vehicles_elasped_time[track_id]

                    # Calculate avg speed
                    speed = utils.calculate_speed(elasped_time)

                    #cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0,0,255), 2)
                    #cv2.putText(img, "ID: " + str(track_id), (int(bbox[0]), int(bbox[1]-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
                    #cv2.putText(img, "E.T: " + str(int(elasped_time)), (int(bbox[0]), int(bbox[1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
                    cv2.putText(img, "Speed: " + str(int(speed)), (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            regions.vehicle_from_Bottom(bbox, track_id, img)
            regions.vehicle_from_Left(bbox, track_id, img)
            regions.vehicle_from_Top(bbox, track_id, img)
            regions.vehicle_from_Right(bbox, track_id, img)


        end_time = time.time()
        total_time = end_time - start_time
        fps = 1 / total_time

        cv2.putText(img, f"FPS: {int(fps)}", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        img = cv2.resize(img, (1200, 720))
        cv2.imshow("Traffic Management System", img)
        if cv2.waitKey(1) & 0xFF == ("q"):
            cv2.destroyAllWindows()
            cap.release()
            break
    print("Process Terminated")
    print("Average FPS: ", str("{0:.2f}".format(fps)))

except KeyboardInterrupt:
    print("Process Terminated")
    print("Average FPS: ", str("{0:.2f}".format(fps)))