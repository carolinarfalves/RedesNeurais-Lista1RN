# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:24:18 2021

1) Para o conjunto de dados ex1traindata1.csv:
    b. Plote o conjunto de dados colocando símbolos diferentes para cada classe.

@author: carol
"""
 
# # Declarando a variavel data e lendo o arquivo ex1traindata1.csv
# data = pd.read_csv(r'C:\Users\carol\JorgeAmaral\20211RedesNeurais\Lista1RN\Data\ex1traindata1.csv')
# # Definido montando e definindo as colunas do dataframe
# df = pd.DataFrame(data, columns= ['X1','X2','labels'])

from Carolina_Alves_lista1_1a import BuilDataFrame
df = BuilDataFrame().Get()


# Importando a biblioteca matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

l0 = df.loc[df['labels'] == 0]
ax.scatter(l0['X1'],l0['X2'], marker='^')

l1 = df.loc[df['labels'] == 1]
ax.scatter(l1['X1'],l1['X2'], marker='s')

plt.legend()
plt.title('Visualizacao do Dataset')
plt.show()
