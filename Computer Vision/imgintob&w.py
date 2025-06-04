import imutils
import cv2
img=cv2.imread("OIP.jpeg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresImg=cv2.threshold(grayImg,190,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("thresholdImage.jpeg",thresImg)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()