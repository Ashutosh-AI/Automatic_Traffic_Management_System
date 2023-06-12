import time
import cv2

from detector1 import YoloDetector
from tracker1 import Tracker


detector = YoloDetector(model_name=None)
obj_tracker = Tracker()

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    start_time = time.time()

    results = detector.score_frame(frame=frame)
    img, detections = detector.plot_boxes(results, frame, height=frame.shape[0], width=frame.shape[1], score_thresh=0.3)
    #print(detections)
    boxes, ids = obj_tracker.objTracker(detections, img)
    #print(boxes, ids)


    cv2.imshow("img", img)
    cv2.waitKey(1)

cv2.destroyAllWindows()
cap.release()
