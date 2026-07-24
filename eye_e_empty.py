from numpy import eye, identity, full

# Criam a a matriz identidade da algebra linear

identidade = identity(3) # Apenas matrizes quadradas
identidade_olho = eye(3, 5) # Qualquer tipo
print(identidade)
print("\n")
print(identidade_olho)
print("\n")


# Com parametros de desolocamento
matriz_deslocada = eye(3, 5, k=1) # positivo desloca para a direita e negativo para a esquerda
print(matriz_deslocada)

