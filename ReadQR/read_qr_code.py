import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture("/dev/video10")
cap.set(3,1280)  #width
cap.set(4,720)  #height
camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        print(code.type)
        print(code.data.decode('utf-8'))

    #show the camera
    cv2.imshow('code scan', frame)
    cv2.waitKey(1)