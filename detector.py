import cv2
import numpy as np
import os
import time
import torch


class YoloDetector():

    def __init__(self, model_name):

        self.model = self.load_model(model_name)
        self.classes = self.model.names
        #print(self.classes)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Using Device: ", self.device)
        self.allowed_objects = ["bicycle", "car", "motorcycle", "bus", "truck"]
        print("allowed Objects :", self.allowed_objects)


    def load_model(self, model_name):

        if model_name:
            model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True)

        return model


    def score_frame(self, frame):

        self.model.to(self.device)

        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        #print("labels cord", labels, cord)

        return labels, cord


    def class_to_label(self, x):

        return self.classes[int(x)]


    def plot_boxes(self, results, frame, height, width, score_thresh=0.3):

        labels, cord = results
        x_shape, y_shape = width, height
        detections = []

        n = len(labels)

        for i in range(n):
            row = cord[i]

            if row[4] >= score_thresh:
                if self.class_to_label(labels[i]) in self.allowed_objects:

                    x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)

                    x_center = x1 + ((x2-x1) / 2)
                    y_center = y1 + ((y2-y1) / 2)

                    tlwh = np.asarray([x1, y1, int(x2-x1), int(y2-y1)], dtype=np.float32)
                    confidence = float(row[4].item())
                    feature = self.class_to_label(labels[i])

                    detections.append(([x1, y1, int(x2-x1), int(y2-y1)], confidence, feature))

        return frame, detections
