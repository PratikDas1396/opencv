import cv2
import numpy as np

img = cv2.imread('data/1.jpg')

height, width  = img.shape[:2]

img.resize()

quarter_height , quarter_width = height / 4, width / 4

cv2.imshow('img', img)

# Translation Matrix
# t = [ 1, 0 , Tx]
#     [ 0, 1 , Ty]

t = np.float32([[1, 0, quarter_width], [0, 1, quarter_height ]])

translated_img = cv2.warpAffine(img, t, (width, height))

cv2.imshow('translated_img', translated_img)
print(t)
cv2.waitKey()
cv2.destroyAllWindows()