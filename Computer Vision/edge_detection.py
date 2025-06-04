import imutils
import cv2
img=cv2.imread("OIP.jpeg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("edgedetection.jpeg",grayImg)
blurred = cv2.GaussianBlur(grayImg, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 150)  # Lower and upper thresholds
cv2.imshow("Edges", edged)
cv2.waitKey(0)
cv2.imshow("PS IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

