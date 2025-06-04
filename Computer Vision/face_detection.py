import cv2
import imutils

# Load the image
image = cv2.imread("face.jpeg")
if image is None:
    print("Error: Image not found! Check the file path.")
    exit()

# Display and save original image
cv2.imshow("Original Image", image)
cv2.imwrite("face_detection.jpeg", image)
cv2.waitKey(0)

# Convert to grayscale (required for face detection)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --- FACE DETECTION ---
# Load pre-trained Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Detect faces with optimized parameters
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,  # Reduce by 10% each pass
    minNeighbors=5,    # Higher = fewer detections but higher quality
    minSize=(30, 30),  # Minimum face size
    flags=cv2.CASCADE_SCALE_IMAGE
)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display and save result
cv2.imshow("Face Detection", image)
cv2.imwrite("faces_detected.jpg", image)
cv2.waitKey(0)

# --- OPTIONAL: PROCESS DETECTED FACES ---
# You could add face-specific processing here, like:
# 1. Extract face ROIs
# 2. Apply blurring/effects to faces
# 3. Face recognition

# --- CONTINUE WITH PREVIOUS PROCESSING ---
# Thresholding
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
eroded = cv2.erode(binary, kernel, iterations=1)
dilated = cv2.dilate(binary, kernel, iterations=1)

# Display results
cv2.imshow("Binary", binary)
cv2.imshow("Eroded", eroded)
cv2.imshow("Dilated", dilated)
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()