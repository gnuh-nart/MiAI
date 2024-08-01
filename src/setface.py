
import cv2
import os

# Path for face image database
dataset_path = 'src/Dataset/FaceData/raw'  # Update the path if needed

# Function to add a new user to the dataset without encryption
def add_user(user_id, username, path=dataset_path):
    # Create a new directory for the user
    user_path = os.path.join(path, str(user_id))
    os.makedirs(user_path, exist_ok=True)

    # Open the camera for capturing images
    cap = cv2.VideoCapture(0)

    # Use the Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Start capturing and storing images
    count = 0
    while count < 30:  # Capture 30 images
        ret, frame = cap.read()
        faces = face_cascade.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face_roi = frame[y:y + h, x:x + w]

            # Save the image to the user's directory
            cv2.imwrite(os.path.join(user_path, f'{count}.png'), face_roi)

            count += 1

        cv2.imshow('Add User', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Input user information from the keyboard
    user_id = int(input("Enter user ID: "))
    username = input("Enter username: ")

    # Add a new user to the dataset without encryption
    add_user(user_id, username)
