import cv2
import numpy as np
import os
import shutil

###############################################

folder1 = "monster_sem_fundo"
folder2 = "no_monster_sem_fundo"

###############################################

num_files1 = len(os.listdir(folder1))
output_path1 = f"{folder1}-gray"
shutil.rmtree(output_path1, ignore_errors=True)
os.mkdir(output_path1)

num_files2 = len(os.listdir(folder2))
output_path2 = f"{folder2}-gray"
shutil.rmtree(output_path2, ignore_errors=True)
os.mkdir(output_path2)

###############################################

# Carregar imagens
images1 = []
images2 = []

for i in range(num_files1):
    image = cv2.imread('{}/{}.png'.format(folder1, i)) #lê a imagem

    #Se a imagem não for carregada
    if image is None:
        print('Não foi possível ler a imagem: {}/{}.png'.format(folder1, i))

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converte a imagem para escala de cinza
    resized_image = cv2.resize(gray_image, (64, 128))   #Redimensiona a imagem
    images1.append(resized_image) #adiciona a imagem redimensionada a lista images[]

# Normalizar intensidade de cada pixel
images = np.array(images1) / 255.0

# Armazenar as imagens pré-processadas
for i in range(num_files1):
    cv2.imwrite('{}/{}.png'.format(output_path1, i), images[i] * 255)


####################################

for i in range(num_files2):
    image = cv2.imread('{}/{}.png'.format(folder2, i)) #lê a imagem

    #Se a imagem não for carregada
    if image is None:
        print('Não foi possível ler a imagem: {}/{}.png'.format(folder2, i))

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converte a imagem para escala de cinza
    resized_image = cv2.resize(gray_image, (64, 128))   #Redimensiona a imagem
    images2.append(resized_image) #adiciona a imagem redimensionada a lista images[]

# Normalizar intensidade de cada pixel
images = np.array(images2) / 255.0

# Armazenar as imagens pré-processadas
for i in range(num_files2):
    cv2.imwrite('{}/{}.png'.format(output_path2, i), images[i] * 255)
