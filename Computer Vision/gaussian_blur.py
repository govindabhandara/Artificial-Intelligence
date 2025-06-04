import imutils
import cv2
img=cv2.imread("OIP.jpeg")
Blurred=cv2.GaussianBlur(img,(11,11),0)
cv2.imwrite("gaussianBlur.png",Blurred)
cv2.imshow("Blurred",Blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

