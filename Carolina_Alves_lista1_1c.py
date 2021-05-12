# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:24:18 2021

1) Para o conjunto de dados ex1traindata1.csv:
    c. Apresente uma tabela descrevendo as estatísticas de cada classe. A Tabela deve
conter pelo menos: média, desvio padrão, valor máximo e mínimo de cada variável.

@author: carol
"""

# Importando a biblioteca PANDAS
import pandas as pd 
# Declarando a variavel data e lendo o arquivo ex1traindata1.csv
data = pd.read_csv(r'C:\Users\carol\JorgeAmaral\20211RedesNeurais\Lista1RN\Data\ex1traindata1.csv')
# Definido montando e definindo as colunas do dataframe
df = pd.DataFrame(data, columns= [0,'X1','X2','labels'])

# Exibindo os 10 primeiros registros do DataFrame, para a minha validação visual 
#df.head(10)

# print(df['X1'].mean()) 
# print(df['X1'].std())
# print(df['X1'].min())
# print(df['X1'].max())

selected = df.loc[df['labels'] == 0]
print (selected)

from tabulate import tabulate

print('Versão LEO')
x1= df['X1']
x2= df['X2']
       
table = [['Classe', 'média', 'desvio padrão', 'valor máximo','valor mínimo'], 
          ['X1', x1.mean(), x1.std(), x1.max(), x1.min()], 
          ['X2', x2.mean(), x2.std(), x2.max(), x2.min()]]
print(tabulate(table, tablefmt='fancy_grid'))


print('Versão Carol')
labels_0 = df.loc[df['labels'] == 0]
# print (labels_0)
labels_1 = df.loc[df['labels'] == 1]
# print (labels_1)

c0x1= labels_0['X1']
c0x2= labels_0['X2']
c1x1= labels_1['X1']
c1x2= labels_1['X2']
 
table = [['Classe', 'média', 'desvio padrão', 'valor máximo','valor mínimo'], 
          ['0-x1', c0x1.mean(), c0x1.std(), c0x1.max(), c0x1.min()], 
          ['0-x2', c0x2.mean(), c0x2.std(), c0x2.max(), c0x2.min()], 
          ['1-x1', c1x1.mean(), c1x1.std(), c1x1.max(), c1x1.min()], 
          ['1-x2', c1x2.mean(), c1x2.std(), c1x2.max(), c1x2.min()]]
print(tabulate(table, tablefmt='fancy_grid'))


