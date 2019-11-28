import cv2
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
XML_PATH = os.path.join(APP_ROOT, 'haarcascade_frontalface_default.xml')

def count_faces(imagePath):
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(XML_PATH)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    totalFaces = len(faces)
    print(f"{totalFaces} faces found in image {imagePath}")
    return totalFaces
