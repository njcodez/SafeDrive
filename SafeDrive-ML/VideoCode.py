import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("drowsiness.h5")

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    
    if not ret:
        continue
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            eyes_roi = roi_color[ey: ey+eh, ex:ex + ew]
            final_image = cv2.resize(eyes_roi, (145, 145))  # Resize to match model's input shape
            final_image = np.expand_dims(final_image, axis=0)
            final_image = final_image / 255.0
            predictions = model.predict(final_image)
            prediction = predictions[0][2]
            threshold = 0.5  
            if prediction > threshold:
                status = "Open Eyes"
            else:
                status = "Closed Eyes"
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, status, (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)
    
    cv2.imshow("Drowsiness Detector", frame)
    
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
