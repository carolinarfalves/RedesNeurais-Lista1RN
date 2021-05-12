# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:24:18 2021

1) Para o conjunto de dados ex1traindata1.csv:
    b. Plote o conjunto de dados colocando símbolos diferentes para cada classe.

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

# Importando a biblioteca matplotlib
import matplotlib.pyplot as plt

df.plot(marker=11, x ='X2', y='X1', kind = 'scatter')


#df = pd.DataFrame(data, columns= ['X1','X2'], index= ['labels'])

#plt.show() 


from array import *

arrX = array('d')
arrY = array('d') 
arrC = []

for i in range(len(df)) :
    arrX.insert(i,df.loc[i, "X1"])
    arrY.insert(i,df.loc[i, "X2"])
         
    if df.loc[i, "labels"] == 1:
        arrC.insert(i,str('tab:red')) 
    else:
        arrC.insert(i,str('tab:purple'))   

 
fig, ax = plt.subplots()
ax.scatter(arrX[:-1], arrY[1:], color=arrC[1:], alpha=0.5)

ax.set_xlabel('X1', fontsize=15)
ax.set_ylabel('X2', fontsize=15)
ax.set_title('Nota: Roxo = (X1 > X2) | Vermelho = (X2 > X1)')

ax.grid(True)
fig.tight_layout()

plt.show()
 