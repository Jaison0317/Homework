# -*- coding: utf-8 -*-

# *Crear un programa que sume una serie de números introducidos por el usuario hasta que
# el usuario introduzca un 0.
# Entonces el programa debe mostrar la suma de todos los números introducidos.



lista = []

   
while True:
    num = int(input("Introduzca un numero: "))
    if num == 0:
        print"El programa finalizó"
        print"La sumatoria es: "
        print(lista)
        break
        
    
    elif num >= 0:
        num = num + num
        print(lista.append(num))
        print(lista)
        