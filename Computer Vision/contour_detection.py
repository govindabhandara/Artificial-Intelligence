import imutils
import cv2
img=cv2.imread("OIP.jpeg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(grayImg, 30, 150)
cv2.imwrite("contour.jpeg",grayImg)
# Find contours
contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)  # Handles OpenCV version differences

# Draw contours
output = grayImg.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)
cv2.imshow("PS IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

