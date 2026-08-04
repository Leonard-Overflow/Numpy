import numpy as np

vetor1 = np.array([1, 2, 3, 4, 5], dtype=np.int32)
vetor2 = np.array([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]], dtype=np.float64)
vetor3 = np.zeros((3, 4, 2), dtype=np.int8)
vetor4 = np.array([1, 2, 3, 4], dtype=np.bool_)
vetor5 = np.array([1, 2, 3]) # Sem o dype explicito sera o int8

# Valor de memoria individual
print(vetor1.itemsize)
print(vetor2.itemsize)
print(vetor3.itemsize)
print(vetor4.itemsize)
print(vetor5.itemsize)

# N de elementos
print(vetor1.size)
print(vetor2.size)
print(vetor3.size)
print(vetor4.size)
print(vetor5.size)

# Memoria total
print(vetor1.nbytes)
print(vetor2.nbytes)
print(vetor3.nbytes)
print(vetor4.nbytes)
print(vetor5.nbytes)