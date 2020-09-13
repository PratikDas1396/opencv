import cv2

# Read Images into  variable
img = cv2.imread('data/flower.jpg')

grayscale  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("grayscale", grayscale)

print("Gray Scaled Image Information")
print("Gray Scaled Image Shape = ", grayscale.shape)
print("Gray Scaled Image width = ", grayscale.shape[0])
print("Gray ScaledImage Height = ", grayscale.shape[1])

cv2.waitKey()

hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv)
print("HSV color Schemed Image Information")
print("Image Shape = ", hsv.shape)
print("Image width = ", hsv.shape[0])
print("Image Height = ", hsv.shape[1])

# Show Images with each channel
cv2.waitKey()
cv2.imshow("Hue Channel", hsv[:, :, 0])
cv2.waitKey()
cv2.imshow("Saturation Channel", hsv[:, :, 1])
cv2.waitKey()
cv2.imshow("Value Channel", hsv[:, :, 2])

# Wait for User Interaction
cv2.waitKey()

# Destroys All open windows
cv2.destroyAllWindows()