from rembg import remove
from PIL import Image
import shutil
import os

###############################################

folder1 = "monster"
folder2 = "no_monster"

###############################################

num_files1 = len(os.listdir(folder1))
output_path1 = f"{folder1}_sem_fundo"
shutil.rmtree(output_path1, ignore_errors=True)
os.mkdir(output_path1)

num_files2 = len(os.listdir(folder2))
output_path2 = f"{folder2}_sem_fundo"
shutil.rmtree(output_path2, ignore_errors=True)
os.mkdir(output_path2)


for i in range(num_files1):
    input_path = f"{folder1}/{i}.jpg"
    output_path = f"{output_path1}/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


for i in range(num_files2):

    input_path = f"{folder2}/{i}.jpg"
    output_path = f"{output_path2}/{i}.png"

    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)