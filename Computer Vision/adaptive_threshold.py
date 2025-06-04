import cv2
import imutils

# Load the image
img = cv2.imread("OIP.jpeg")
if img is None:
    print("Error: Image not found! Check the file path.")
    exit()

# Display and save original image
cv2.imshow("Original Image", img)
cv2.imwrite("adaptive.jpeg", img)
cv2.waitKey(0)

# Convert to grayscale (required for thresholding)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Otsu's Thresholding
_, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Otsu Threshold", otsu)
cv2.waitKey(0)

# 2. Adaptive Thresholding
adaptive = cv2.adaptiveThreshold(
    gray, 
    255, 
    cv2.ADAPTIVE_THRESH_MEAN_C, 
    cv2.THRESH_BINARY, 
    11, 
    2
)
cv2.imshow("Adaptive Threshold", adaptive)
cv2.waitKey(0)

# Optional: Rotate using imutils
rotated = imutils.rotate(img, angle=45)
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)

# Save processed images
cv2.imwrite("otsu_threshold.jpg", otsu)
cv2.imwrite("adaptive_threshold.jpg", adaptive)
cv2.imwrite("rotated_image.jpg", rotated)

# Close all windows
cv2.destroyAllWindows()