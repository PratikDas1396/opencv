import cv2
import numpy as np

capture = cv2.VideoCapture(0)

lower_skin = np.array([0,60,100], dtype=np.uint8)
upper_skin = np.array([20,255,255], dtype=np.uint8)
     
while(True):
    try:
        ret, frame = cap.read()
        frame=cv2.flip(frame,1)
        kernel = np.ones((2,2),np.uint8)
        
        roi=frame[100:300, 100:300]
        cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        mask = cv2.dilate(mask,kernel,iterations = 4)
        mask = cv2.GaussianBlur(mask,(3,3),100) 

        contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = max(contours, key = cv2.contourArea)

        epsilon = 0.0005 * cv2.arcLength(cnt,True)
        print(cv2.arcLength(cnt,True), epsilon)
        approx= cv2.approxPolyDP(cnt, epsilon ,True)

        hull = cv2.convexHull(approx, returnPoints=False)
        defects = cv2.conv.exityDefects(approx, hull)

        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            cv2.line(roi,start, end, [0,255,0], 2)
    
        cv2.imshow('mask',mask)
        cv2.imshow('frame',frame)

    except Exception as inst:
        pass
    
    if cv2.waitKey() == 27:
        break
    
cv2.destroyAllWindows()
cap.release()    