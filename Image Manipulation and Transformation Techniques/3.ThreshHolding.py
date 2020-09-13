import cv2

# Read Images into  variable
img = cv2.imread('data/gredient.jpg')

grayscale  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale", grayscale)
cv2.waitKey()

rec, THRESH_BINARY = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("THRESH_BINARY", THRESH_BINARY)

cv2.waitKey()
rec, THRESH_BINARY_INV = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("THRESH_BINARY_INV", THRESH_BINARY_INV)

cv2.waitKey()
rec, THRESH_TRUNC = cv2.threshold(grayscale, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("THRESH_TRUNC", THRESH_TRUNC)

cv2.waitKey()
rec, THRESH_TOZERO = cv2.threshold(grayscale, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("THRESH_TOZERO", THRESH_TOZERO)

cv2.waitKey()
rec, THRESH_TOZERO_INV = cv2.threshold(grayscale, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("THRESH_TOZERO_INV", THRESH_TOZERO_INV)

# Wait for User Interaction
cv2.waitKey()

# Destroys All open windows
cv2.destroyAllWindows()