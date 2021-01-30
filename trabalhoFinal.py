import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

img = cv2.imread(r'C:\Users\guilh\Documents\AnaliseImagens\Image.jpg')#(NÃO COMENTAR)
#PARA TESTE DESCOMENTAR CADA DIVISÃO POR VEZ
#MUDAR O CAMINHO DA IMAGEM

#----------------------------------------------- CANAIS RGB ----------------------------------------------(DEIXAR COMENTADO)

(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

cv2.imshow("Normal", img)
cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)
cv2.waitKey(0)
cv2.destroyAllWindows

#---------------------------------------------- TIPOS DE FORMATO DE CORES -----------------------------------(DEIXAR COMENTADO)

#gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#rgb = cv2.imread(r'C:\Users\guilh\Documents\AnaliseImagens\Image.jpg',1)

#cv2.imshow("GRAY", gray)
#cv2.imshow("HSV", hsv)
#cv2.imshow("RGB", rgb)

#cv2.waitKey(0)
#cv2.destroyAllWindows

#-------------------------------------------------- FILTROS --------------------------------------------------(DEIXAR COMENTADO)

#Filtro Media(DEIXAR COMENTADO)

#blur = cv2.blur(img,(10,10))

#plt.subplot(121),plt.imshow(img),plt.title('Proteina')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(blur),plt.title('Proteina Blurred')
#plt.xticks([]), plt.yticks([])
#plt.show()

#Filtro Mediana(DEIXAR COMENTADO)

#median = cv2.medianBlur(img,31)

#plt.subplot(121),plt.imshow(img),plt.title('Proteina')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(median),plt.title('Proteina Median')
#plt.xticks([]), plt.yticks([])
#plt.show()

#Filtro Gaussiano(DEIXAR COMENTADO)

#gaussian = cv2.GaussianBlur(img,(41,41),0)

#plt.subplot(121),plt.imshow(img),plt.title('Proteina')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(gaussian),plt.title('Proteina Gaussian')
#plt.xticks([]), plt.yticks([])
#plt.show()


#------------------------------------------------ REALCE ---------------------------------------------(DEIXAR COMENTADO)

#imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#imgNegativo = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#imgContraste = cv2.equalizeHist(imgCinza)
#imgGama =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#imgLogaritmo = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#for i in range(imgNegativo.shape[0]):
#    for j in range(imgNegativo.shape[1]):
#        imgNegativo[i,j] = 255 - imgNegativo[i,j]

#for i in range(imgGama.shape[0]):
#    for j in range(imgGama.shape[1]):
#        y = 1.3
#        imgGama[i,j] = imgGama[i,j]**(1/y)

#for i in range(imgLogaritmo.shape[0]):
#    for j in range(imgLogaritmo.shape[1]):
#        imgLogaritmo[i,j] = 80 * math.log(imgLogaritmo[i,j]+1)

#cv2.imshow('Cinza',imgCinza)
#cv2.imshow('Negativo',imgNegativo)
#cv2.imshow('Contraste',imgContraste)
#cv2.imshow('Gama',imgGama)
#cv2.imshow('Logaritimico',imgLogaritmo)
#cv2.waitKey(0)
#cv2.destroyAllWindows