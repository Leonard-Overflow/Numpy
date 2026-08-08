import numpy as np

np.random.seed(42)
vendas = np.random.randint(50, 500, size=(12, 30))  # 12 produtos, 30 dias

def diagnostico_matriz(matriz: np.ndarray):
    """Imprime propriedade estruturais da matriz"""
    print(f"{'Propriedade':<25} | {'Valor':<5}")
    print("-"*40)
    print(f"{'Forma':<25} | {str(matriz.shape):<5}")
    print(f"{'Dimensao':<25} | {str(matriz.ndim):<5}")
    print(f"{'Tipo da matriz':<25} | {str(matriz.dtype):<5}")
    print(f"{'Tamanho':<25} | {str(matriz.size):<5}")
    print(f"{'Byte por elemento':<25} | {str(matriz.itemsize):<5}")
    print(f"{'Total de bytes da matriz':<25} | {str(matriz.nbytes):<5}")

def

diagnostico_matriz(vendas)