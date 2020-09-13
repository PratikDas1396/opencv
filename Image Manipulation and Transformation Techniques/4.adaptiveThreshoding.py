import cv2

try:
    # Read Images into  variable
    img = cv2.imread('data/page.jpg')

    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.waitKey()
    rec, THRESH_BINARY = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("THRESH_BINARY", THRESH_BINARY)

    cv2.waitKey()
    BlurredImg = cv2.GaussianBlur(grayscale, (3, 3), 0)
    adaptive = cv2.adaptiveThreshold(BlurredImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
    cv2.imshow("adaptiveThreshold", adaptive) 

    cv2.waitKey()
    BlurredImg_5 = cv2.GaussianBlur(grayscale, (5, 5), 0)
    rec1, THRESH_BINARY_OTSU = cv2.threshold(BlurredImg_5, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("THRESH_BINARY_OTSU", THRESH_BINARY_OTSU)

except Exception as inst:
        print(inst.args)
        pass

# Wait for User Interaction
cv2.waitKey()

# Destroys All open windows
cv2.destroyAllWindows()
