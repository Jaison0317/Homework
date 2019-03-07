# -*- coding: utf-8 -*-

# *Crear un programa que cuente desde el 10 hasta el 0,
# indicando cuánto falta para llegar a 0. 
# Cuando llegue a 0 debe mostrar un mensaje que indique que el programa ha finalizado.


i = 10
while i <= 10:
    print(i)
    print'Falta para llegar a cero: '
    i -= 1
    if i == 0:
        print(i)
        print'Ha llegado al cero.'
        break
print"Programa terminado."
