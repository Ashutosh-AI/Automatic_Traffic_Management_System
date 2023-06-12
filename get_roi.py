import cv2
import numpy as np
from Utilities import utils

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

region1_Left = [(300, 340), (350, 330), (250, 500), (200, 505)]
region2_Top = [(450,200), (950, 90), (930, 70), (460, 170)]
region3_Right = [(1100, 150), (1140, 145), (1230, 245), (1190, 250)]
region4_Bottom = [(350,580), (1200, 360), (1230, 390), (340,620)]

cap = cv2.VideoCapture('TorontoIntersections.mp4')

while True:
    ret, frame = cap.read()
    #frame = frame[200:frame.shape[1]]
    height, width = frame.shape[0], frame.shape[1]
    frame = frame[350:height, 100:width - 200]
    #frame = cv2.resize(frame, (1200, 720))

    for region in [region1_Left, region2_Top, region3_Right, region4_Bottom]:
        cv2.polylines(frame, [np.array(region, np.int32)], True, (0,0,255), 2)

    #frame = cv2.resize(frame, (1200, 720))

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
