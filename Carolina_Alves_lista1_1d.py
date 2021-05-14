# -*- coding: utf-8 -*-
"""
Created on Tue May 11 21:19:10 2021

@author: carol
"""
import numpy as np

class Perceptron(object):
    
    def __init__(self, learning_rate=0.01, epochs=50):
        """
        Inicializa o perceptron com os valores de
        learning rate (taxa de aprendizado), epochs
        """ 
        self.learning_rate = learning_rate
        self.epochs = epochs
    
        print("[>] Parâmetros do Perceptron: \n- taxa de aprendizagem: {} \n- # épocas: {}".format(
            self.learning_rate,
            self.epochs
        ))
    
    def _sum(self, X):
        """
        O processo de sum vai multiplicar o input pelo peso.
        """
        dp = np.dot(X, self._weights) + self._bias
         
        print("[!] Agregação ({} e {}) + peso {} = {}".format(
            X,
            self._weights,
            self._bias,
            dp
        ))
        return dp
    
    def _activation(self, value):
        """
        Como função de ativação, escolhi a função degrau.
        Outras funções são bem comuns, mas o ganho entre elas
        faz com que a degrau seja uma das com melhor custo-benefício.
        """
        return np.where(value >= 0.0, 1, -1)
    
    def fit(self, X, y):
        """
        Vamos começar com os pesos como um array
        numpy aleatório, já que não temos pistas sobre
        quais são os pesos corretos.
        """
        self._bias = np.random.uniform(-1, 1)
        self._weights = np.random.uniform(-1, 1, (X.shape[1]))
        self._errors = []
        
        print("[>>] Iniciando a rotina de treinamento: \n- pesos iniciais: {} \n- erros iniciais: {}".format(
            self._weights,
            self._errors
        ))
        print("- conjunto de treinamento (X): {}\n- conjunto de treinamento (y): {}\n ---".format(
            X,
            y
        ))
    
        # Iterando o numero de epochs...
        for epoch_number in range(self.epochs):
            errors = 0
            
            print("[>>] Inserindo época {}\n- pesos: {}\n- erros: {}".format(
                epoch_number,
                self._weights,
                self._errors
            ))
        
            for xi, target in zip(X, y):
                print("[!] Aprendendo xi = {} (alvo {})".format(xi, target))
                
                output = self.predict(xi)
                update = self.learning_rate * (target - output)
                
                print("[!] {} = {}({} - {})".format(
                    update,
                    self.learning_rate,
                    target,
                    output
                ))
                print("[<] os pesos eram {}".format(self._weights))
            
                self._bias += update
                
                self._weights += update * xi
                
                print("[>] os pesos agora são {}".format(self._weights))
                
                errors += int(update != 0.0)
                
                print("-")
                
            self._errors.append(errors)
            
            print("--")
                
        return self
    
    def predict(self, X):
        result = self._activation(self._sum(X))
        
        print("[?] Deve disparar? (é >= 0): {}".format(
            result
        ))
        
        return result