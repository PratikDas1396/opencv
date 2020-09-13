import cv2
import numpy as np

img = cv2.imread('data/1.jpg')
cv2.imshow('img', img)
cv2.waitKey()

img_small = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('img_small', img_small)
cv2.waitKey()

INTER_CUBIC = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('INTER_CUBIC', INTER_CUBIC)
cv2.waitKey()

INTER_AREA = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
cv2.imshow('INTER_AREA', INTER_AREA)
cv2.waitKey()

INTER_NEAREST = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_NEAREST)
cv2.imshow('INTER_NEAREST', INTER_NEAREST)
cv2.waitKey()

INTER_LINEAR = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LINEAR)
cv2.imshow('INTER_LINEAR', INTER_LINEAR)
cv2.waitKey()

INTER_LANCZOS4 = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('INTER_LANCZOS4', INTER_LANCZOS4)
cv2.waitKey()

cv2.destroyAllWindows()