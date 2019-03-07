
# -*- coding: utf-8 -*-

#*Crear un programa que pida al usuario un número e imprima una lista de números
# desde el 1 hasta el número introducido y su raiz cuadrada.
#Por ejemplo, 
#si el usuario introduce un 3 el programa debe imprimir:
#1 raiz cuadrada 1
#2 raiz cuadrada 4
#3 raiz cuadrada 9

import math

num = int(input("Introduce un numero: "))
lista = []

print("La raiz cuadrada es: ")

for num in range(num):
    if num >= 0:
        num = num **2
        
        print(num)
        