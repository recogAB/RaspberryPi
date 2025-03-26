import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture("/dev/video10")
cap.set(3,1920)  #width
cap.set(4,1080)  #height
camera = True
while camera == True:
    success, frame = cap.read()

    for conde in decode(frame):
        print(code.type)
        print(code.data.decode('utf-8'))

    #show the camera
    cv2.imshow('code scan', frame)
    cv2.waitKey(1)