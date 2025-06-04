import imutils
import cv2
img=cv2.imread("OIP.jpeg")
cv2.imwrite("newimage.jpeg",img)
cv2.imshow("PS IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
