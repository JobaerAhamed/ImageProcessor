import face_recognition as FR
from PIL import Image

image = FR.load_image_file('./img/groups/team1.jpg')
face_locations = FR.face_locations(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]

    pil_image = Image.fromarray(face_image)
    pil_image.save(f'{top}.jpg')