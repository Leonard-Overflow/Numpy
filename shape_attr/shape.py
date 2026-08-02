import numpy as np

# Shapes iguais são compativeis e as operacoes se aplicam elemento a elemento

# Shapes diferentes, mas compativeis
vetor1 = np.array([1, 2, 3])
vetor2 = np.array([[10],
                   [20]])

print(vetor1.shape)
print(vetor2.shape)
print(vetor1 + vetor2)

# As qtds de linhas e colunas do primeiro e do segundo devem ser iguais.
# O resultado e uma tabela formada com os valores de cada um dos arrays
# Quando linhas e colunas nao coinscidem os arrays nao sao compativeis.

# Para ver a dimensao
print(vetor1.ndim)
print((vetor1 + vetor2).ndim)

# Qunatidade de elementos
print((vetor1 + vetor2).size)
print(vetor1.size)