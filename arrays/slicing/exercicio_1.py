import numpy as np

def verifica(semana1, semana2):
    numero = semana2 - semana1
    if numero < 0:
        return "Prejuizo"
    elif numero == 0:
        return "Sem diferenca"
    else:
        return "Lucro"

np.random.seed(42)
faturamento = np.random.randint(500, 5000, size=(6, 7))
print(f"Total das semanas: \n{faturamento}\n")

# Desempenho das ultimas 4 semanas
ultimas_4 = faturamento[-4:, :]
print(f"4 ultimas semanas: \n{ultimas_4}\n")

# Valores dos domingos
domingos = ultimas_4[-2:, 0:1]
print(f"2 ultimos domingos \n{domingos}\n")

# Verficando o maior lucro
primeiras = np.sum(faturamento[0:3, :])
ultimas = np.sum(faturamento[-3:, :])
print(f"Lucro das primeiras semanas: \n{primeiras}\n")
print(f"Lucro das ultimas semanas: \n{ultimas}\n")

# Sexta e sabado, do recente pro anitgo
fim_de_semana = faturamento[::-1, 5:7]
print(f"Lucro do fim de semana: \n{fim_de_semana}\n")

# Faturamento terca a quinta
total_terca_quinta = np.sum(faturamento[:, 2:5])
print(f"Lucro do meio da semana \n{total_terca_quinta}\n")

# Comparacao da primeira com a ultima
primeira = faturamento[0, :]
ultima = faturamento[5, :]
faturamento_comparacao = np.array(list(map(verifica, primeira, ultima)))
print(ultima - primeira)
print(f"Comparacao da primeira com a ultima: \n{faturamento_comparacao}\n")