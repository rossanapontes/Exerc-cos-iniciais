# -*- coding: utf-8 -*-
"""Numero n menor e maior .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17pbWMdQi1jP4GbQBaZORpVaAqI4NW2Oe
"""

quantidade = maior = menor = 0
resposta = "s"
while resposta == "s":
  num = int (input("Digite um numero: "))
  quantidade += 1
  if quantidade == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num    
  resposta = str (input("Deseja continuar ? [s/n] "))
print ("Fim")
print("{} \n {}".format(menor, maior))