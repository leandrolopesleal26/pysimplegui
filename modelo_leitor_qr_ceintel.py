import pyzbar.pyzbar as pyzbar
from pyzbar import decode
import numpy as np
import cv2
import time


# Camera:
# cap = cv2.VideoCapture("rtsp://admin:1406@172.20.8.5:1025/chID=13&streamType=main&linkType=tcpa")
cap = cv2.VideoCapture("rtsp://admin:IACNCZ@10.0.0.105:554/cam/realmonitor?channel=1&subtype=0")

# get the webcam:
#cap = cv2.VideoCapture(0)


def decode(im):
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
        print('Tipo : ', obj.type)
        print('Dados lidos : ', obj.data, '\n')
    return decodedObjects


font = cv2.FONT_HERSHEY_SIMPLEX

while (cap.isOpened()):

    ret, frame = cap.read()
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    decodedObjects = decode(im)

    for decodedObject in decodedObjects:
        points = decodedObject.polygon

        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number of points in the convex hull
        n = len(hull)
        # Draw the convext hull
        for j in range(0, n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
            x = decodedObject.rect.left
        y = decodedObject.rect.top

        barCode = str(decodedObject.data)
        cv2.putText(frame, barCode, (x, y), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('LEITOR DE QR CODE CAMERAS IP CEINTEL', frame)
    key = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
