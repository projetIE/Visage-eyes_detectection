import cv2 as cv

# charger les classificateur en cascade pré-entrainés

face_cascade =   cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#charger les images

img = cv.imread('obama.jpg')
gray_image = cv.cvtColor(img,cv.COLOR_BGR2GRAY) 

#executer la detection d'image
faces = face_cascade.detectMultiScale(gray_image,1.1,8)         #(image,scale factor(10%=1.1),nb_voisins)

#affichage des visages      format = (x,y,longueur,largeur)


i=0
print('size faces=', len(faces),len(faces[0]))
for face in faces:      
    print (face)
    x,y,w,h = face
    

    #dessiner le resctangle     
    cv.rectangle(img , (x, y ) ,(x + w , y + h ), (0,255,0),2)

    #extraire les visages de l'image principale
    #opencv et numpy y=lignes et x pour les collones
    face = img[y:y+h,x:x+w]

    #afficher les face0 ,1 , 2 
    cv.imshow('face{}'.format(i),face )
    i+= 1   

cv.imshow('image principale', img)
cv.waitKey(0)
cv.destroyAllWindows