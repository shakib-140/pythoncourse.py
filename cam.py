import cv2
cam=cv2.VideoCapture(1)
while true:
    _,frame=cam.read()
    cv2.imshow('my web camera',frame)
    cv2.waitKey(1)




