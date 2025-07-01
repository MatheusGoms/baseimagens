# Caminho para o dataset de imagens
dataset_path = "caminho_para_sua_pasta_de_imagens"
imagens = os.listdir(dataset_path)

# Dicionário para armazenar embeddings
database = {}

# Extração de embeddings para todas as imagens
for imagem_nome in imagens:
    caminho_imagem = os.path.join(dataset_path, imagem_nome)
    embeddings = extrair_embeddings(caminho_imagem)
    database[imagem_nome] = embeddings

print("Embeddings extraídos para todas as imagens.")
