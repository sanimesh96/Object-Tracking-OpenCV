import cv2
import numpy as np
from thresholding import process_image,trackobj


def nothing(x):
    pass

cv2.namedWindow('thresh')
cv2.createTrackbar('h', 'thresh', 5, 255, nothing)
cv2.createTrackbar('s', 'thresh', 100, 255, nothing)
cv2.createTrackbar('v', 'thresh', 100, 255, nothing)
cv2.createTrackbar('H', 'thresh', 16, 255, nothing)
cv2.createTrackbar('S', 'thresh', 255, 255, nothing)
cv2.createTrackbar('V', 'thresh', 255, 255, nothing)

cam=cv2.VideoCapture(0)

while (True):

    _,frame=cam.read()
    input_image= frame.copy()

    frame=cv2.blur(frame,(20,20))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h = cv2.getTrackbarPos('h', 'thresh')
    s = cv2.getTrackbarPos('s', 'thresh')
    v = cv2.getTrackbarPos('v', 'thresh')
    H = cv2.getTrackbarPos('H', 'thresh')
    S = cv2.getTrackbarPos('S', 'thresh')
    V = cv2.getTrackbarPos('V', 'thresh')

    lower = np.array([h,s,v])
    upper = np.array([H,S,V])

    mask = cv2.inRange(hsv, lower, upper)
    coloured_mask,mask = process_image(mask, input_image)

    track,input_image=trackobj(input_image,mask,coloured_mask)

    cv2.imshow('thresh', track)
    cv2.imshow('mask', mask)
    cv2.imshow('original', input_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()