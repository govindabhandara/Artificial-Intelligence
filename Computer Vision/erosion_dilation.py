import cv2
import imutils

# Load the image
img = cv2.imread("OIP.jpeg")
if img is None:
    print("Error: Image not found! Check the file path.")
    exit()

# Display and save original image
cv2.imshow("Original Image", img)
cv2.imwrite("erosion_dilation.jpeg", img)
cv2.waitKey(0)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary threshold (needed for morphological operations)
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Binary Image", binary)
cv2.waitKey(0)

# Create kernel for morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Erosion (shrinks white regions)
eroded = cv2.erode(binary, kernel, iterations=1)
cv2.imshow("Erosion", eroded)
cv2.waitKey(0)
cv2.imwrite("eroded.jpg", eroded)

# Dilation (expands white regions)
dilated = cv2.dilate(binary, kernel, iterations=1)
cv2.imshow("Dilation", dilated)
cv2.waitKey(0)
cv2.imwrite("dilated.jpg", dilated)

# Optional Advanced Operations:
# Opening (erosion followed by dilation - removes noise)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.waitKey(0)

# Closing (dilation followed by erosion - fills holes)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()