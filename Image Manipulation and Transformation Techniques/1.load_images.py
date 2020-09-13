import cv2
import numpy as np

# Read Images into  variable
img = cv2.imread('data/flower.jpg')

# Print data that represents image
print(img)

# The Extracted data is a numpy array
# With the Extracted data we can get Information About Image

print("Image Dimension = ",  img.shape)
print("Image Width = ",  img.shape[0])
print("Image Height = ",  img.shape[1])
# for An colored Image it containe 3 Channels ie B G R Value
print("Image Height = ",  img.shape[2])



print(" ------------- BGR Value -----------------")
print("Blue = ",  img[0 ,0, 0])
print("Green = ",  img[0 ,0, 1])
print("Red = ",  img[0 ,0, 2])

# Shows image in window
cv2.imshow('flower', img)

# Wait for User Interaction
cv2.waitKey()

# Destroys All open windows
cv2.destroyAllWindows()