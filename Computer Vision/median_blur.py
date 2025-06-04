import cv2
img=cv2.imread("OIP.jpeg")
median=cv2.medianBlur(img,5)
cv2.imwrite("medianBlur.png",median)
cv2.imshow("median blur",median)
cv2.waitKey(0)
cv2.destroyAllWindows()