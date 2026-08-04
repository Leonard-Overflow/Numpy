import numpy as np

grade = np.empty([6, 10]) # Grade de sensores(sensor x tempo)
grade[0] = np.full(10, -999) # Sensor quebrado
tempo = np.arange(0, 10) # Tempo em minutos
ultimos_minutos = grade[:, tempo[-3:]] # 3 ultimos minutos
grade[1] = np.linspace(0, 100, 10) # Sensor calibrado
grade[2] = np.logspace(0, 3, 10)
identidade = np.eye(6)
np.allclose(grade.T, grade.T @ identidade)