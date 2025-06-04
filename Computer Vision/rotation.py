import imutils
import cv2
img=cv2.imread("OIP.jpeg")
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.imwrite("rotation.png",img)
rotated=imutils.rotate(img,angle=45)
cv2.imshow("Rotated",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()