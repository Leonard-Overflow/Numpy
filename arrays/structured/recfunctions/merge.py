import numpy as np
import numpy.lib.recfunctions as rfn

# Padrao
nomes = np.array(['Leonardo', 'Rafael', 'Lucas'])
idades = np.array([18, 20, 24])
funcionarios = rfn.merge_arrays(seqarrays=[nomes, idades], fill_value=-1, flatten=False, usemask=False, asrecarray=False)
# print(funcionarios)

# Com estrutura aninhada
pessoas = np.array(["Leonardo", "Matt", "Charlie"])
series_do_leonardo = ("The big bang theory", "Smiling friends")
series_do_matt = ("The twilight zone", "Bob esponja")
series_do_charlie = ("Smiling friends", "The office")
estrutura = np.dtype({'names': ['series1', 'series2'],
                      'formats': ['U30', 'U30']})
series = np.array([series_do_leonardo, series_do_matt, series_do_charlie], dtype=estrutura)

resultado = rfn.merge_arrays([pessoas, series], fill_value=-1, flatten=False, usemask=False, asrecarray=False)
print(series.shape)

# seqarrays = Os arrays que seram mergeados. 2 formam um dict e 3 ou mais um array de tuplas
# flatten = Decide o que fazer om um array estruturado. Se False aninha a estrutura dentro de uma coluna
# propria, se True adiciona uma nova coluna para cada item novo.
# cada coluna da estrtura ao array final.
# fill_value, usemask e asrecarray = O mesmo do append_fields