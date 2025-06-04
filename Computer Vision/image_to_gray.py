import imutils
import cv2
img=cv2.imread("OIP.jpeg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gretimage.jpeg",grayImg)
cv2.imshow("PS IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

