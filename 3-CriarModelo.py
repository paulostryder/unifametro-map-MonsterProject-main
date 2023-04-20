import cv2
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib
import os
from rembg import remove
from PIL import Image
import shutil

###############################################

folder1 = "monster_sem_fundo-gray"
folder2 = "no_monster_sem_fundo-gray"
folder_mix = "monster_mix"

###############################################

num_files1 = len(os.listdir(folder1))
num_files2 = len(os.listdir(folder2))

output_path = f"{folder_mix}"
shutil.rmtree(folder_mix, ignore_errors=True)
os.mkdir(folder_mix)

###############################################

images = []
labels = []

for i in range(num_files1):
    input_path = f"{folder1}/{i}.png"
    output_path = f"{folder_mix}/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

    image = cv2.imread(input_path)

    if image is None :
        print(f'Não foi possível abrir a imagem {i} da pasta {folder1},')
    images.append(image)
    labels.append(1)


for i in range(num_files2):
    input_path = f"{folder2}/{i}.png"
    output_path = f"{folder_mix}/{num_files1 + i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

    image = cv2.imread(input_path)

    if image is None :
        print(f'Não foi possível abrir a imagem {i} da pasta {folder2},')
    images.append(image)
    labels.append(0)

print("Imagens : ", len(images))
print("Labels : ", len(labels))

x_train, x_test, y_train, y_test = train_test_split(images, labels, test_size=0.2)

def extract_features(imagem):

   color_hist = cv2.calcHist([image], [0,1,2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
   color_hist = cv2.normalize(color_hist, color_hist).flatten()
   return color_hist

x_train_features = [extract_features(image) for image in x_train]
x_test_features = [extract_features(image) for image in x_test]

clf = SVC(kernel='linear', C=1000)

clf.fit(x_train_features, y_train)

acuracia = clf.score(x_test_features, y_test)

print("Acuracia : ", acuracia)

joblib.dump(clf, 'modelo_monster.joblib')