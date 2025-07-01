from sklearn.metrics.pairwise import euclidean_distances

# Função para encontrar as imagens mais similares
def encontrar_similares(imagem_consulta, database, top_n=5):
    consulta_embeddings = extrair_embeddings(imagem_consulta)
    distancias = {}
    
    # Calcular a distância euclidiana para todas as imagens no database
    for nome, embeddings in database.items():
        distancias[nome] = euclidean_distances([consulta_embeddings], [embeddings])[0][0]
    
    # Ordenar pelas menores distâncias (mais similares)
    similares = sorted(distancias.items(), key=lambda x: x[1])[:top_n]
    return [sim[0] for sim in similares]

# Testar com uma imagem de consulta
imagem_consulta = "sua_imagem.jpg"  # Substitua pelo caminho de uma imagem de consulta
imagens_similares = encontrar_similares(imagem_consulta, database)
print("Imagens mais similares:", imagens_similares)
