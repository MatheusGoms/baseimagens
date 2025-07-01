import matplotlib.pyplot as plt

# Função para exibir a imagem de consulta e as similares
def exibir_resultados(imagem_consulta, imagens_similares, dataset_path):
    plt.figure(figsize=(15, 5))
    
    # Exibir a imagem de consulta
    plt.subplot(1, len(imagens_similares) + 1, 1)
    imagem = load_img(imagem_consulta, target_size=(224, 224))
    plt.imshow(imagem)
    plt.title("Consulta")
    plt.axis("off")
    
    # Exibir as imagens similares
    for i, similar in enumerate(imagens_similares):
        plt.subplot(1, len(imagens_similares) + 1, i + 2)
        imagem = load_img(os.path.join(dataset_path, similar), target_size=(224, 224))
        plt.imshow(imagem)
        plt.title(f"Similar {i+1}")
        plt.axis("off")
    
    plt.show()

# Testar exibição
exibir_resultados(imagem_consulta, imagens_similares, dataset_path)
