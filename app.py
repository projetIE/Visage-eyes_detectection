


import sys
import cv2 as cv


# charger les classificateur en cascade pré-entrainés

face_cascade =   cv.CascadeClassifier('haarcascade_frontalface_default.xml')



#charger les images

img = cv.imread('obama.jpg')
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 


#executer la detection d'image
faces = face_cascade.detectMultiScale(gray_image,1.1,8)         #(image,scale factor(10%=1.1),nb_voisins)



#verifier le nombre de visage

if len(faces) != 2:
    sys.exit('la photo doit avoir 2 visages, try again')

#recuperation des dimensions des visages


x1,y1,w1,h1 = faces[0]
x2,y2,w2,h2 = faces[1]


#extraction de l'image des visages
face1 = img[y1:y1+h1,x1:x1+w1]
face2 = img[y2:y2+h2,x2:x2+w2]

#redimenensioner face 2 au dim de face 1 et l'inverse
face2= cv.resize(face2,(w1,h1))
face1= cv.resize(face1,(w2,h2))



#remplacer face 1 par face 0
img[y1:y1+h1,x1:x1+w1] = face2
#remplacer face 0 par face 1
img[y2:y2+h2,x2:x2+w2] = face1


#affichage des visages

cv.imshow('face1',face1)
cv.imshow('face2',face2)
cv.imshow('echange',img)
cv.waitKey(0)
cv.destroyAllWindows()













    