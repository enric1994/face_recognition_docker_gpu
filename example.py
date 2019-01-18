import os
import face_recognition

for root, dirs, files in os.walk("/face_recognition/images"):
    for name in files:
        image = face_recognition.load_image_file(os.path.join(root,name))
        face_locations = face_recognition.face_locations(image, model="cnn")
        print(face_locations)