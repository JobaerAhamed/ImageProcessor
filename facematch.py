import face_recognition as FR

bill_img = FR.load_image_file('./img/known/Bill Gates.jpg')
bill_face = FR.face_encodings(bill_img)[0]

rand_img = FR.load_image_file('./img/unknown/keanu-reeves-2000.jpg')
rand_face = FR.face_encodings(rand_img)[0]

#compare
print(FR.compare_faces([bill_face], rand_face)[0])