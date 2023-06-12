import time
import cv2
from Utilities.utils import Utils

# Inherit Utils class
class Region(Utils):

    def __init__(self):
        super().__init__()

        self.inside_Bottom = {}
        self.inside_Left = {}
        self.inside_Top = {}
        self.inside_Right = {}

        self.B_to_T = set()
        self.B_to_L = set()
        self.B_to_R = set()

        self.L_to_T = set()
        self.L_to_R = set()
        self.L_to_B = set()

        self.T_to_B = set()
        self.T_to_L = set()
        self.T_to_R = set()

        self.R_to_B = set()
        self.R_to_L = set()
        self.R_to_T = set()

        self.vehicles_elasped_time = {}
        self.vehicles_entering = {}



    def vehicle_from_Bottom(self, bbox, id, img):

        # Vehicles Out from Bottom Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region4_Bottom(bbox)
        if result:
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (150, 0, 70), 3)
            self.inside_Bottom[id] = (x4, y4)

        if id in self.inside_Bottom:

            result = self.isPoint_inside_region2_Top(bbox)
            if result:
                self.B_to_T.add(id)

            result = self.isPoint_inside_region1_Left(bbox)
            if result:
                self.B_to_L.add(id)

            result = self.isPoint_inside_region3_Right(bbox)
            if result:
                self.B_to_R.add(id)

        cv2.putText(img, "Bottom to Top : " + str(len(self.B_to_T)), (60, 550), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 0, 70), 2)
        cv2.putText(img, "Bottom to Left : " + str(len(self.B_to_L)), (60, 575), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 0, 70), 2)
        cv2.putText(img, "Bottom to Right : " + str(len(self.B_to_R)), (60, 600), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (150, 0, 70), 2)

        #print("Bottom to Top", self.B_to_T)
        #print("Bottom to Left", self.B_to_L)
        #print("Bottom to Right", self.B_to_R)


    def vehicle_from_Left(self, bbox, id, img):

        # Vehicles Out from Left Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region1_Left(bbox)
        if result:
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 200, 0), 3)
            self.inside_Left[id] = (x4, y4)

        if id in self.inside_Left:

            result = self.isPoint_inside_region2_Top(bbox)
            if result:
                self.L_to_T.add(id)

            result = self.isPoint_inside_region4_Bottom(bbox)
            if result:
                self.L_to_B.add(id)

            result = self.isPoint_inside_region3_Right(bbox)
            if result:
                self.L_to_R.add(id)

        cv2.putText(img, "Left to Top : " + str(len(self.L_to_T)), (80, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)
        cv2.putText(img, "Left to Right : " + str(len(self.L_to_R)), (80, 325), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)
        cv2.putText(img, "Left to Bottom : " + str(len(self.L_to_B)), (80, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 200, 0), 2)

        #print("Left to Top", self.L_to_T)
        #print("Left to Bottom", self.L_to_B)
        #print("Left to Right", self.L_to_R)



    def vehicle_from_Top(self, bbox, id, img):

        # Vehicles Out from Top Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region2_Top(bbox)
        if result:
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (0, 125, 250), 3)
            self.inside_Top[id] = (x4, y4)

        if id in self.inside_Top:

            result = self.isPoint_inside_region1_Left(bbox)
            if result:
                self.T_to_L.add(id)

            result = self.isPoint_inside_region4_Bottom(bbox)
            if result:
                self.T_to_B.add(id)

            result = self.isPoint_inside_region3_Right(bbox)
            if result:
                self.T_to_R.add(id)

        cv2.putText(img, "Top to Right : " + str(len(self.T_to_R)), (1000, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 125, 250), 2)
        cv2.putText(img, "Top to Bottom : " + str(len(self.T_to_B)), (1000, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 125, 250), 2)
        cv2.putText(img, "Top to Left : " + str(len(self.T_to_L)), (1000, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 125, 250), 2)

        #print("Top to Left", self.T_to_L)
        #print("Top to Bottom", self.T_to_B)
        #print("Top to Right", self.T_to_R)



    def vehicle_from_Right(self, bbox, id, img):

        # Vehicles Out from Right Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region3_Right(bbox)
        if result:
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), (200, 200, 0), 3)
            self.inside_Right[id] = (x4, y4)

        if id in self.inside_Right:

            result = self.isPoint_inside_region1_Left(bbox)
            if result:
                self.R_to_L.add(id)

            result = self.isPoint_inside_region4_Bottom(bbox)
            if result:
                self.R_to_B.add(id)

            result = self.isPoint_inside_region2_Top(bbox)
            if result:
                self.R_to_T.add(id)

        cv2.putText(img, "Right to Top : " + str(len(self.R_to_T)), (1200, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)
        cv2.putText(img, "Right to Bottom : " + str(len(self.R_to_B)), (1200, 275), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)
        cv2.putText(img, "Right to Left : " + str(len(self.R_to_L)), (1200, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 0), 2)

        #print("Right to Left", self.R_to_L)
        #print("Right to Bottom", self.R_to_B)
        #print("Right to Top", self.R_to_T)
