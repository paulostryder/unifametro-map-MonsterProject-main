import joblib
import cv2
import os

folder = "monster_mix"
num_files = len(os.listdir(folder))
pred_value = 1

###############################################

# Carregar o classificador
clf = joblib.load('modelo_monster.joblib')

# Extrair recursos das imagens
def extract_features(image):
    color_hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    color_hist = cv2.normalize(color_hist, color_hist).flatten()
    return color_hist

# Integrar classificador em um programa de visão computacional
def recognize_monster_can(image):
    features = extract_features(image)
    prediction = clf.predict([features])
    if prediction == pred_value:
        return 'Monster'
    else:
        return 'Other Energy Drink'

for i in range(num_files):
    image = cv2.imread('{}/{}.png'.format(folder, i))
    result = recognize_monster_can(image)
    print(f'Image {i} is {result}')