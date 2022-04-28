#!/usr/bin/env python3

# Imports
from ctypes import sizeof
import math
from rect import Rect
import matplotlib.pyplot as mpl
import numpy as np

#### Parte 2 ####
# Crie uma função com dois argumentos para calcular a área de um retângulo
# Se apenas um argumento for passado deve-se assumir que é um quadrado

def rarea(x, y=None):
    if y is None:
        return x*x
    else:
        return x*y

if __name__ == '__main__':
    print(rarea(12))
    print(rarea(4, 5))

    # Calcule a raiz quadrada de 4
    print(math.sqrt(4))

    # Crie uma classe com 2 atributos, referentes aos lados de um retângulo
    # Adicione um construtor e dois métodos a essa classe, para calcular a área e o perímetro do retângulo
    # Salve essa classe em um módulo dedicado
    # Em outro módulo, principal, instancie essa classe e calcule o perímetro de um quadrado com lado 2
    
    quadrado = Rect(10, 20)
    print(quadrado.per())

    # Mostre o gráfico de uma curva seno (matplotlib)
    x = np.arange(0, 2*math.pi, 0.1) #Preenche x com uma lista de 0 a 2pi, com passos de 0.1
    y = np.sin(x)

    mpl.plot(x, y)
    mpl.show()

    #### Extras ####
    # Quantos segundos há em 3 horas, 23 minutos e 17 segundos?
    h, m, s = 3, 23, 17
    print((h*3600)+(m*60)+s)

    # Supondo que a cotação do dólar esteja em R$ 3,25, salve esse valor em uma variável e 
    # utilize-o para calcular quanto você teria ao cambiar R$ 65,00 para dólares?
    dollar_real = 3.25
    real = 65
    print(real/dollar_real)
    
    # Dado uma lista de números, faça com que os números sejam ordenados e, em seguida,
    # inverta a ordem da lista usando slicing.
    num_list = [3, 5, 1, 7, 2, 9, 8]
    um_list = num_list.sort()
    print(num_list)
    num_list = num_list[::-1]
    print(num_list)

    # Receba uma lista com números inteiros e devolva um número inteiro correspondente à soma
    # dos números recebidos.
    integer_list = [2, 4, 5, 6, 7, 6, 10, 33]
    sum = 0
    for i in integer_list:
        sum += i
    print(sum)

    # Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana,
    # tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo
    # recebem listas vazias, ou você tem aula?).
    semana = {}
    semana["segunda"] = ["3ECAUT.033"]
    semana["terca"] = ["ELE05", "ETN05", "CTR01", "ETN04"]
    semana["quarta"] = ["ELE04", "IFI01", "CTR01", "GT03AUT001.1"]
    semana["quinta"] = ["GT03AUT001.1", "ETN05"]
    semana["sexta"] = ["FSQ08", "CTR01"]
    semana["sabado"] = []
    semana["doming"] = []

    # Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e
    # o quadrado do número caso ele seja negativo.
    num = int(input("Digite um número inteiro: "))
    if num>=0:
        print(math.sqrt(num))
    else:
        print(num*num)

    # Calcule a tabuada do 13.
    for i in range(0, 13):
        print(i+1, " x 13 = ", (i+1)*13)

    # Faça uma função que determina se um número é par ou ímpar. Use o % para determinar o
    # resto de uma divisão. Por exemplo: 3 % 2 = 1 e 4 % 2 = 0

    def par(a):
        if a%2==0:
            print(a, "é par")
            return True
        else:
            print(a, "é impar")
            return False

    par(3)
    
    #### Extras 2 ####
    # Peça do usuário um valor em graus para um ângulo. Converta-o para radianos e,
    # usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo
    angle = float(input("Digite um ângulo em graus: "))
    angle = math.radians(angle)
    print("sin: ", math.sin(angle), ", cos: ", math.cos(angle), ", tan: ", math.tan(angle))

    # Faça um Python Script que receba um valor t referente a uma quantidade total em
    # segundos. Calcule a quantas horas:minutos:segundos a quantidade total de segundos correspondente.
    sec = int(input("Digite um valor em segundos: "))
    min = 0
    hour = 0
    while sec>=60:
        sec-=60
        min+=1
    while min>=60:
        min-=60
        hour+=1
    print(hour, " horas, ", min, " minutos e ", sec, " segundos.")


    # Faça um código que receba um número n do usuário e imprima os n primeiros
    # números da sequência de Fibonacci
    n = int(input("Fibonacci: digite um número inteiro: "))
    a0, a1 = 0, 1 # números iniciais da série
    seq = []
    
    for i in range(0, n):
        seq.append(a0)
        a0, a1 = a1, a0+a1
    
    print(seq)

    # Calcule 9! usando a estrutura for
    n = 9
    nfat = n
    for i in range(n-1, 0, -1):
        nfat*=i
    print(nfat)
    
    # Calcule 9! usando a estrutura while
    n = 9
    i = 1
    nfat = n
    while i < 9:
        nfat*=i
        i+=1
    print(nfat)

    # Crie um Python Script que conte quantas vezes cada nome está presente em uma
    # lista [’nome1’, ’nome2’, ...] e armazena essa contagem em um dicionário {’nome1’:
    # xvezes, ’nome2’: yvezes, ....}.
    nomes = ["josé", "joão", "maria", "josé", "maria", "maria"]
    dict_nomes = {}
    for nome in nomes:
        dict_nomes[nome] = nomes.count(nome)
    print(dict_nomes)