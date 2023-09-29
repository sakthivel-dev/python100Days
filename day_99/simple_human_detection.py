# Import the OpenCV library
import cv2

# Import the pathlib library
import pathlib

# Get the path to the Haar Cascade Classifier XML file for face detection
cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"

# Print the path to the cascade classifier XML file
print(cascade_path)

# Create a CascadeClassifier object for face detection using the Haar Cascade XML file
clf = cv2.CascadeClassifier(str(cascade_path))

# Open a video capture object, either from the default camera (0) or from a video file ("video.mp4")

# camera = cv2.VideoCapture(0)  # Uncomment this line for using the default camera

camera = cv2.VideoCapture("video.mp4")  # Uncomment this line for using a video file

# Start an infinite loop for video capture and processing
while True:
    # Read a frame from the video capture
    _, frame = camera.read()

    # Convert the frame to grayscale (needed for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use the CascadeClassifier to detect faces in the grayscale frame
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,       # Scale factor for multi-scale detection
        minNeighbors=5,       # Minimum neighbors for a region to be considered a face
        minSize=(30, 30),     # Minimum size of a detected face
        flags=cv2.CASCADE_SCALE_IMAGE  # Flag for scaling the image
    )

    # Loop through the detected faces and draw rectangles around them
    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)  # Draw a rectangle around the face

    # Display the frame with detected faces
    cv2.imshow("faces", frame)

    # Check if the 'q' key is pressed to exit the loop
    if cv2.waitKey(1) == ord("q"):
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
