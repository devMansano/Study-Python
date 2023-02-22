"""
Reduce

OBS: a partir do Python 3: a função reduce deve ser importada por não ser mais uma função integrada
e utilizar esta função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se for preciso. Em todo caso, 99% das vezes um loop for
é mais legível


#Entendendo o Reduce

Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

e voce tem uma função que recebe dois parâmetros:

def funcao(x, y)
    return x * y

Assim como map() e filter() a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce() funciona da seguinte forma:

    Passo 1 = res1 = f(a1, a2) #Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2 = res2 = f(res1, a3) #Aplica a função passando o resultado do passo 1 + o terceiro elemento
    e isso é repetido até o fim.
    .
    .
    .
    passo n = resn = f(resn, an) # em cada passo ela aplica a função passando o primeiro argumento 
    da aplicação anterior. No final reduce() irá retornar o resultado final.

alternativamente poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1,a2),a3), ....),an)

"""

#Exemplo

from functools import reduce


dados = [ 3, 5, 2, 56, 1, 7, 8, 9]

#Para utilizar reduce() precisamos de uma função que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

#Utilizando um loop normal

for n in dados:
    res = res * n

print(res)