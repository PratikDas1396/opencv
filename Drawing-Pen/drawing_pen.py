import cv2
import numpy as np

capture = cv2.VideoCapture(0)

kernel = np.ones((1, 1), 'uint8')
fake_all = None

lower_band = np.array([38, 100, 100])
upper_band = np.array([75, 255, 255])


while True:
    _, frame = capture.read()
    frame = cv2.flip(frame, 1)
    smooth_imge = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame = cv2.cvtColor(smooth_imge, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, lower_band, upper_band)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel)

    if fake_all is None:
        fake_all = np.zeros(np.array(mask).shape)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) != 0 :
        c = max(contours, key=cv2.contourArea)
        if len(c) > 20:
            x, y, w, h = cv2.boundingRect(c)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            fake_all = cv2.circle(fake_all, (x,y), 5, (255, 0, 0) , -1) 
    
    cv2.imshow("mask", fake_all)
    cv2.imshow("Input Video", frame)
    key = cv2.waitKey(1)
    if key == 27:  # escape key
        break

cv2.destroyAllWindows()
capture.release()    