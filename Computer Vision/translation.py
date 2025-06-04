import imutils
import cv2
img=cv2.imread("OIP.jpeg")
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.imwrite("translation.png",img)
shifted = imutils.translate(img, 25, -50) 
cv2.imshow("Shifted",shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()