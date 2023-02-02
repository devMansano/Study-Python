"""
Tuplas(tuple)
são parecidas com listas porém há diferenças
1- Tuplas são representadas por parênteses ( ) 
2- As Tuplas são imutáveis -> toda operação de uma Tupla gera uma nova Tupla.
É possível gerar tuplas com range(distância) como por exemplo:
tupla = tuple(range(11))
print(tupla)
print(type(tupla))
Tuplas podem ser Desempacotadas
tupla = ('Geek University' , 'Programação em python')
escola, curso = tupla
print(escola)
print(curso)
OBS : gera erro se colocarmos um tipo diferente de elementos para desempacotar.
Adição e remoção em tuplas não existem por conta de serem imutáveis.
Concatenação de tuplas
tupla1 = (1,2,3)
tupla2 = (2,3,4)
print(tupla1)
print(tupla2)
tupla3 = (tupla1 + tupla2)
"""

#cuidado 1: as tuplas são representadas por parênteses, mas veja:

tupla1 = (1,2,3,4,5)
print(tupla1)
print(type(tupla1))


tupla2 = 1,2,3,4,5
print (tupla2)
print(type(tupla2))

#cuidado 2: tuplas com 1 elemento não é considerado, mas se houver uma vírgula acaba sendo considerado

tupla3 = (4)
print (tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))
