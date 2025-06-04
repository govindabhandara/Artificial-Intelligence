import cv2
import numpy as np

# Load the image
image = cv2.imread('face.jpeg')  # Replace with your image path
if image is None:
    print("Error: Could not load image")
    exit()

# Resize image to match our transformation dimensions
image = cv2.resize(image, (300, 300))

# Define source and destination points for perspective transform
src = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])
dst = np.float32([[50, 50], [250, 50], [300, 300], [0, 300]])

# Compute perspective transform matrix
M = cv2.getPerspectiveTransform(src, dst)

# Apply perspective transformation
warped = cv2.warpPerspective(image, M, (300, 300))

# Draw points on original image for visualization
for point in src:
    cv2.circle(image, tuple(point.astype(int)), 5, (0, 0, 255), -1)

# Draw points on warped image for visualization
for point in dst:
    cv2.circle(warped, tuple(point.astype(int)), 5, (0, 255, 0), -1)

# Display results
cv2.imshow("Original with Source Points (red)", image)
cv2.imshow("Warped with Destination Points (green)", warped)
cv2.waitKey(0)

# Save results
cv2.imwrite("original_with_points.jpg", image)
cv2.imwrite("perspective_warped.jpg", warped)

# Print transformation matrix
print("Perspective Transformation Matrix:")
print(M)

cv2.destroyAllWindows()