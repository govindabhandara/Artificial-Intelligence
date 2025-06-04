import cv2
import imutils
import numpy as np
from datetime import datetime
import time

def webcam_processing():
    cap = cv2.VideoCapture(0)  # 0 = default webcam
    
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return

    # Load face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cv2.namedWindow("Smart Webcam", cv2.WINDOW_NORMAL)
    
    prev_time = 0
    fps = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break

        frame = imutils.resize(frame, width=800)
        frame = cv2.flip(frame, 1)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Corrected detectMultiScale call with proper closing parenthesis
        faces = face_cascade.detectMultiScale (
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Face", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"Faces: {len(faces)}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, datetime.now().strftime("%H:%M:%S"), (10, 90),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.imshow("Smart Webcam", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            cv2.imwrite(f"webcam_{timestamp}.jpg", frame)
            print(f"Saved webcam_{timestamp}.jpg")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam_processing()
    print("Webcam session ended")
