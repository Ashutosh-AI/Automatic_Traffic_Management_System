import cv2
import numpy as np

class Utils():

    def __init__(self):

        self.region1_Left = [(300, 340), (350, 330), (250, 500), (200, 505)]
        self.region2_Top = [(450, 200), (950, 90), (930, 70), (460, 170)]
        self.region3_Right = [(1100, 150), (1140, 145), (1230, 245), (1190, 250)]
        self.region4_Bottom = [(350, 580), (1200, 360), (1230, 390), (340, 620)]

        """
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
        """

    def draw_roi_on_image(self, frame):

        colors = [(150, 0, 70), (0, 200, 0), (0, 125, 250), (200, 200, 0)]

        for idx, region in enumerate([self.region4_Bottom, self.region1_Left, self.region2_Top, self.region3_Right]):
            if idx == 0:
                color = colors[0]
            if idx == 1:
                color = colors[1]
            if idx == 2:
                color = colors[2]
            if idx == 3:
                color = colors[3]

            cv2.polylines(frame, [np.array(region, np.int32)], True, color, 2)

        return frame


    def isPoint_inside_region1_Left(self, bbox):

        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)

        result = cv2.pointPolygonTest(np.array(self.region1_Left, np.int32), (cx, cy), False)
        #print(result)

        if result >= 0:
            return True
        else:
            return False


    def isPoint_inside_region2_Top(self, bbox):

        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)

        result = cv2.pointPolygonTest(np.array(self.region2_Top, np.int32), (cx, cy), False)
        #print(result)

        if result >= 0:
            return True
        else:
            return False


    def isPoint_inside_region3_Right(self, bbox):

        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)

        result = cv2.pointPolygonTest(np.array(self.region3_Right, np.int32), (cx, cy), False)
        #print(result)

        if result >= 0:
            return True
        else:
            return False


    def isPoint_inside_region4_Bottom(self, bbox):

        cx = int((bbox[0] + bbox[2]) / 2)
        cy = int((bbox[1] + bbox[3]) / 2)

        result = cv2.pointPolygonTest(np.array(self.region4_Bottom, np.int32), (cx, cy), False)
        #print(result)

        if result >= 0:
            return True
        else:
            return False


    def calculate_speed(self, elasped_time):

        distance = 60     # meters
        avg_speed_ms = distance/elasped_time
        avg_speed_kh = avg_speed_ms * 3.6

        return avg_speed_kh







    """
    def vehicle_from_Bottom(self, bbox, id):

        # Vehicles Out from Bottom Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region4_Bottom(bbox)
        if result:
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


            print("Bottom to Top", self.B_to_T)
            print("Bottom to Left", self.B_to_L)
            print("Bottom to Right", self.B_to_R)


    def vehicle_from_Left(self, bbox, id):

        # Vehicles Out from Left Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region1_Left(bbox)
        if result:
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
                self.L_to_R.add()

        print("Left to Top", self.L_to_T)
        print("Left to Bottom", self.L_to_B)
        print("Left to Right", self.L_to_R)



    def vehicle_from_Top(self, bbox, id):

        # Vehicles Out from Top Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region2_Top(bbox)
        if result:
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
                self.T_to_R.add()

        print("Top to Left", self.T_to_L)
        print("Top to Bottom", self.T_to_B)
        print("Top to Right", self.T_to_R)



    def vehicle_from_Right(self, bbox, id):

        # Vehicles Out from Right Region
        x4, y4 = bbox[2], bbox[3]
        result = self.isPoint_inside_region3_Right(bbox)
        if result:
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
                self.R_to_T.add()

        print("Right to Left", self.R_to_L)
        print("Right to Bottom", self.R_to_B)
        print("Right to Right", self.R_to_T)
    """