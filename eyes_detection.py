import cv2 as cv

# charger les classificateur en cascade pré-entrainés

face_cascade =   cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade =   cv.CascadeClassifier('haarcascade_eye.xml')


#charger les images

img = cv.imread('obama.jpg')
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 

#executer la detection d'image
faces = face_cascade.detectMultiScale(gray_image,1.1,8)         #(image,scale factor(10%=1.1),nb_voisins)

#affichage des visages      format = (x,y,longueur,largeur)


print('size faces=', len(faces),len(faces[0]))
for face in faces:      
    print (face)
    x,y,w,h = face
    

    #dessiner le resctangle     
    cv.rectangle(img , (x, y ) ,(x + w , y + h ), (0,255,0),2)


#exection de la detection des yeux

eyes = eye_cascade.detectMultiScale(gray_image, 1.1,2)

#affichage des yeux
for (ex,ey,ew,eh) in eyes:
    #dessine le contour des yeux 
    #cv.rectangle(img, (coin sup gauche), (coin inf droit, (COULEUR BRG), EPAISSEUR )
    cv.rectangle(img, (ex , ey), (ex+ew,ey+eh), (255,0,0), 2 )




cv.imshow('image principale', img)
cv.waitKey(0)
cv.destroyAllWindows