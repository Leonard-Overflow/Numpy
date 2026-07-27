from numpy.lib import recfunctions as rfn
import numpy as np

estrutura = np.dtype([('nome', 'U30'),
                      ('idade', 'i4'),
                      ('departamento', 'U30'),
                      ('status', 'bool')])

nova_coluna = np.dtype([('salario', 'f4'),
                        ('beneficios', 'bool')])

funcionario1 = ('Leonardo', 18, 'analise de dados', 1)
funcioario2 = ('Rafael', 29, 'RH', 0)
funcioario3 = ('Bianca', 31, 'marketing', 1)
funcioario4 = ('Pedro', 25, 'engenharia', 1)
funcioario5 = ('Kaua', 25, 'marketing', 0)
funcioario6 = ('Fernando', 21, 'analise de dados', 1)

lista_de_funcionarios = [funcionario1, funcioario2, funcioario3, funcioario4, funcioario5, funcioario6]

funcionarios = np.array(lista_de_funcionarios, dtype=estrutura)

salarios = [2500.0, 3000.0, 2500.0, 3000.0, 3000.0, 3500.0]
beneficios = [1, 0, 0, 1, 0, 1]

print(funcionarios.dtype)

# novo_array = rfn.append_fields(base=funcionarios,
#                                names=['salario','beneficios'],
#                                data=[np.array(salarios), np.array(beneficios)],
#                                dtypes=[np.dtype('f4'), np.dtype('bool')],
#                                fill_value=-1
#                                usemask=False,
#                                asrecarray=False)

novo_array2 = rfn.append_fields(funcionarios, ['salario', 'beneficios'], [np.array(salarios), np.array(beneficios)], [np.dtype('f4'), np.dtype(bool)], -1, False, False)

print(novo_array2.dtype)

# base = Array que vai ser modificado
# names = Nome dos novos campos da estrtura
# data = Dados que vao ser inseridos nos campos de cada espaco existente no array original
# dtype = Tipo de cada campo
# fill_value = Insere um valor padrao caso nao exista valores pra preencher. -1 por padrao
# usemask = Transforma em masked array
# asrecarry = Transforma em recarray permitindo acessar os valores como attr. Ergonomia apenas