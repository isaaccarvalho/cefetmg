from ast import Num
from curses import flash
from tkinter import N

####  Parte 1 ####
# Crie um programa que atravesse uma lista de palavras e indique em qual 
# vogal ela termina, ou se termina em uma consoante

palavras = ["cadeira", "ventilador", "mesa", "carro"]
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    if(p[-1].lower().startswith(vogais)):
        print(p+" termina com a vogal '"+p[-1]+"'")
    else:
        print(p+" termina com consoante")

# Um programa que determine o primeiro número primo em um intervalo

num1 = 15
num2 = 37
primos = []

for num in range(num1, num2+1): # percorre cada numero
    primo = True
    for i in range(2, num): # verifica se ele é divisivel por numeros a partir de 2 até o numero anterior a ele mesmo
        if(num%i==0):
            primo = False
    if(primo):
        primos.append(num)
        primo = True

print(primos[0])
            
        
    
