# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:24:18 2021

1) Para o conjunto de dados ex1traindata1.csv:
    a. Carregue o arquivo ex1traindata1.csv e coloque em um dataframe df
    
@author: carol
"""
 
import pandas as pd 

class BuilDataFrame(object):
        
    # # Declarando a variavel data e lendo o arquivo ex1traindata1.csv
    # data = pd.read_csv(r'C:\Users\carol\JorgeAmaral\20211RedesNeurais\Lista1RN\Data\ex1traindata1.csv')
    # # Definido montando e definindo as colunas do dataframe
    # df = pd.DataFrame(data, columns= ['X1','X2','labels'])
    
    # # Exibindo os 10 primeiros registros do DataFrame, para a minha validação visual 
    # df.head(10)
        
    def __init__(self):
        # Declarando a variavel data e lendo o arquivo ex1traindata1.csv
        self.data = pd.read_csv(r'C:\Users\carol\JorgeAmaral\20211RedesNeurais\Lista1RN\Data\ex1traindata1.csv')
        # Definido montando e definindo as colunas do dataframe
        self.df = pd.DataFrame(self.data, columns= ['X1','X2','labels'])
        
    def Get(self):
        return self.df     