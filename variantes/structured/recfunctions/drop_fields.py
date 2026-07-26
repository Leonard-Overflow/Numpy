from numpy.lib import recfunctions as rfn
import numpy as np

estrutura = np.dtype([('nome', 'U30'),
                      ('idade', 'i4'),
                      ('departamento', 'U30'),
                      ('status', 'bool')])

funcionario1 = ('Leonardo', 18, 'analise de dados', 1)
funcioario2 = ('Rafael', 29, 'RH', 0)
funcioario3 = ('Bianca', 31, 'marketing', 1)
funcioario4 = ('Pedro', 25, 'engenharia', 1)
funcioario5 = ('Kaua', 25, 'marketing', 0)
funcioario6 = ('Fernando', 21, 'analise de dados', 1)

lista_de_funcionarios = [funcionario1, funcioario2, funcioario3, funcioario4, funcioario5, funcioario6]

funcionarios = np.array(lista_de_funcionarios, dtype=estrutura)

print(funcionarios.dtype)

anonimos = rfn.drop_fields(funcionarios, ['nome', 'idade'])

print(anonimos.dtype)

# base = array de entrada
# drop_nanmes = campos que vao ser apagados
# usemask e asrecarry = o mesmo do append_fields