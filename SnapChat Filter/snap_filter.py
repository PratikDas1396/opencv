import cv2
import sys
import numpy as np
import face_recognition
import math
# from .helpers import FACIAL_LANDMARKS_IDXS
# from .helpers import shape_to_np

faceCascade = cv2.CascadeClassifier('./data/haar-cascade/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

settings = {
    'scaleFactor': 1.3,
    'minNeighbors': 5,
    'minSize': (50, 50),
    'flags': cv2.CASCADE_DO_ROUGH_SEARCH | cv2.CASCADE_FIND_BIGGEST_OBJECT
}

landmarks_arr = []

while True:
    marked = None
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)

    glass = cv2.imread('./data/glasses.png')

    faces = faceCascade.detectMultiScale(frame, **settings)
    landmarks = face_recognition.face_landmarks(frame)

     # # Draw a rectangle around the faces
    if len(faces) > 0:
        for (x, y, w, h) in faces:  # detected[-1:]:
            x1, y1, x2, y2 = x, y, (x + w), (y + h)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    if len(landmarks) > 0:
        x1, x2, y1, y2 = 0, 0, 0, 0
        chin_start_x, chin_start_y, chin_end_x, chin_end_y = 0, 0, 0, 0
        left_x, left_y, rigth_x, rigth_y = 0, 0, 0, 0
        
        if len(landmarks) > 0:

            chin_start_x, chin_start_y = landmarks[0]['chin'][0]
            chin_end_x, chin_end_y = landmarks[0]['chin'][len(landmarks[0]['chin']) - 1]

            left_x, left_y = landmarks[0]['left_eyebrow'][len(landmarks[0]['left_eyebrow']) - 1]
            rigth_x, right_y = landmarks[0]['right_eyebrow'][2]

            print("left", left_x, left_y )
            print("chin", chin_start_x, chin_start_y)
            # cv2.circle(frame, (chin_start_x , left_y), 1,  (0, 0, 255), 2) 
            
            for key in ['right_eyebrow', 'left_eyebrow', 'chin']:
                for points in landmarks[0][key]:
                    cv2.circle(frame, points, 1,  (0, 255, 0), 2)
                

            print(chin_start_x, chin_start_y, chin_end_x, chin_end_y)
            width = abs(chin_start_x - chin_end_x)
            height = int(0.3 * width)

            glass = cv2.resize(glass, (width, height), interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(glass, cv2.COLOR_BGR2GRAY)
            thresh, mask = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
            glass[mask > 200] = 0

            y_from, y_to = left_y , (left_y + height)
            # y_from, y_to = chin_start_y , (chin_start_y + height)
            x_from, x_to = chin_start_x, (chin_start_x + width)

            glass_area = frame[y_from: y_to,  x_from:x_to]

            masked_glass_area = cv2.bitwise_and(glass_area, glass_area, mask=mask)

            final_glass = cv2.add(masked_glass_area, glass)
            frame[y_from: y_to,  x_from:x_to] = final_glass
            cv2.imshow('Video', frame)
            cv2.imshow('mask', mask)
            cv2.imshow('glass_area', glass_area)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()