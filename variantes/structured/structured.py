import numpy as np

# Estrutura do array
dtype_proprio = np.dtype([('nome', 'U30'), ('idade', 'i4'), ('departamento', 'U30'), ('status', 'bool')])
dtype_proprio_com_dict = np.dtype({'names': ['nome', 'idade', 'departamento', 'status'],
                                   'formats': ['U30', 'i4', 'U30', 'bool']})

# Quando um array for criado ele pode ter seu valores acessados via index, chave ou os 2 juntos
funcionario1 = ('Leonardo', 18, 'analise de dados', 1)
funcioario2 = ('Rafael', 29, 'RH', 0)
funcioario3 = ('Bianca', 31, 'marketing', 1)
funcioario4 = ('Pedro', 25, 'engenharia', 1)
funcioario5 = ('Kaua', 25, 'marketing', 0)
funcioario6 = ('Fernando', 21, 'analise de dados', 1)
lista_de_funcionarios = np.array([funcionario1, funcioario2, funcioario3, funcioario4, funcioario5, funcioario6])

funcionarios = np.array(lista_de_funcionarios, dtype=dtype_proprio)
print(funcionarios["nome"])
print(funcionarios[0])
print(funcionarios[1]["idade"])

# E possivel ver os campos da estrutura do array
print(funcionarios.dtype)

# E possivel ordenar os itens do array com o attr order
for i in np.sort(funcionarios, order=['status', 'nome']):
    print(i)