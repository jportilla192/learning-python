''' crear una calculadora que reciba dos valores por consola y que 
realice las operaciones aritmeticas basicas'''

import os

os.system('clear')

#inputs
print("ingrese primer valor: ")
n1 = int(input())

n2 = int(input("ingrese el segundo valor: \n "))

suma = n1 + n2
print("suma: ", suma)

print(type(n1))
