import cv2
import imutils

# Load the image
img = cv2.imread("OIP.jpeg")

# Display and save original image
cv2.imshow("Original Image", img)
cv2.imwrite("otsu.jpeg", img)
cv2.waitKey(0)

# Convert to grayscale (required for thresholding)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display Otsu's result
cv2.imshow("Otsu Threshold", otsu)
cv2.waitKey(0)

# Optional: Rotate using imutils (example)
rotated = imutils.rotate(img, angle=45)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()