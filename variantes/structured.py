import numpy as np

# Estrutura do array
dtype_proprio = np.dtype([('nome', 'U30'), ('idade', 'i4'), ('departamento', 'U30'), ('status', 'bool')])
dtype_proprio_com_dict = np.dtype({'names': ['nome', 'idade', 'departamento', 'status'],
                                   'formats': ['U30', 'i4', 'U30', 'bool']})

# Quando um array for criado ele pode ter seu valores acessados via index, chave ou os 2 juntos
funcionario1 = ('Leonardo', 18, 'analise de dados', 1)
funcioario2 = ('Rafael', 29, 'engenharia', 0)
lista_de_funcionarios = [funcionario1, funcioario2]

funcionarios = np.array(lista_de_funcionarios,  dtype=dtype_proprio)
print(funcionarios["nome"])
print(funcionarios[0])
print(funcionarios[1]["idade"])