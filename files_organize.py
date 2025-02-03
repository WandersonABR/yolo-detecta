import os
import shutil
import random

# Aqui: Caminho da pasta original das imagens
origem = r"C:\\Users\\User\Downloads\\patinete - Pesquisa Google"

# Aqui: Novo diretório para armazenar as imagens e anotações
base_dir = r"C:\\Users\\User\Downloads\\YOLO_dataset"

# Criar estrutura do YOLO
subdirs = ["images/train", "images/valid", "images/test", "labels/train", "labels/valid", "labels/test"]
for sub in subdirs:
    os.makedirs(os.path.join(base_dir, sub), exist_ok=True)

# Listar as imagens e dividir entre treino, validação e teste
imagens = [f for f in os.listdir(origem) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(imagens)

# Dividir 70% treino, 20% validação, 10% teste
train_split = int(len(imagens) * 0.7)
valid_split = int(len(imagens) * 0.9)

for i, img in enumerate(imagens):
    src_path = os.path.join(origem, img)
    if i < train_split:
        dst_path = os.path.join(base_dir, "images/train", img)
    elif i < valid_split:
        dst_path = os.path.join(base_dir, "images/valid", img)
    else:
        dst_path = os.path.join(base_dir, "images/test", img)
    shutil.copy(src_path, dst_path)

print("Arquivos organizados no formato YOLO!")
