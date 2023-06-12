from deep_sort_realtime.deepsort_tracker import DeepSort
from detector1 import YoloDetector
import cv2

class Tracker():

    def __init__(self):
        self.object_tracker = DeepSort(max_age=20)

    def objTracker(self, detections, img):

        boxes = ids = []

        tracks = self.object_tracker.update_tracks(detections, img)

        for track in tracks:
            """Newly created tracks are
               classified as `tentative` until enough evidence has been collected. Then,
               the track state is changed to `confirmed"""
            if not track.is_confirmed():
                continue
            track_id = track.track_id
            ltrb = track.to_ltrb()
            #print("track Id", track_id)
            #print("coordinates", ltrb)

            bbox = ltrb

            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 0, 255), 2)
            cv2.putText(img, "ID: " + str(track_id), (int(bbox[0]), int(bbox[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


            boxes.append(bbox)
            ids.append(track_id)

        return boxes, ids
