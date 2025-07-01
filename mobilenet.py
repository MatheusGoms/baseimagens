import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

# Carregar o modelo MobileNetV2 pré-treinado (sem a última camada de classificação)
model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

# Função para extrair embeddings de uma imagem
def extrair_embeddings(caminho_imagem):
    imagem = load_img(caminho_imagem, target_size=(224, 224))  # Redimensionar a imagem
    imagem = img_to_array(imagem)  # Converter para array
    imagem = np.expand_dims(imagem, axis=0)  # Adicionar dimensão
    imagem = preprocess_input(imagem)  # Pré-processar para MobileNetV2
    embeddings = model.predict(imagem)  # Extrair características
    return embeddings.flatten()

# Testar extração de embeddings
caminho_teste = "sua_imagem.jpg"  # Substitua pelo caminho de uma imagem
embeddings = extrair_embeddings(caminho_teste)
print("Embeddings extraídos:", embeddings.shape)
