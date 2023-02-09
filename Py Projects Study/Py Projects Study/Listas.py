"""
    
    Listas funcionam como vetores / matrizes (arrays) com a diferença de serem dinâmicos
    e também de podermos colocar qualquer tipo de dado
    
    Linguagem java: Arrays
        possuem tamanho e tipo de dado fixo.
    
    Linguagem Python
    Dinâmico: não possui tamanho fixo.
    Qualquer tipo de dado : não possuem tipo de dado fixo.
    
    Listas são representadas por colchetes [ ]
    
    list(range()) gera uma lista de quantos elementos você quiser apenas especificando com um número
    dentro do range()
    
    import random é para gerar um número aleatório
    utilizando a função randint() para que os números sejam inteiros
    
"""

import random


type ([])
lista1 = [1,2,3,4,5,6,7]
lista2 = ['g','a','b','y']
lista3 = list(range(11))
list4 = list("Geek University")

print(lista1)
print(lista2)
print(lista3)
print(list4)

# Podemos checar se determinado valor está contido na lista

num = random.randint(0,21)

if num in lista3:
    print('O número está contido')
    print(num)
    
else:
    print('Não foi possível encontrar')
    print(num)