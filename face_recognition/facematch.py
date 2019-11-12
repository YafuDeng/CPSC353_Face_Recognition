import face_recognition

image_of_yafu = face_recognition.load_image_file('./img/known/YafuDeng.jpg')
my_face_encoding = face_recognition.face_encodings(image_of_yafu)[0]

unknown_image = face_recognition.load_image_file('./img/unknown/123 03.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# compare faces
result = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if result[0]:
	print('this is yafu')
else:
	print('nope')

