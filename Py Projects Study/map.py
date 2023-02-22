"""
Map

fazemos o mapeamnto de valores com map

"""

import math


def area(r):
    """Calcula a área do círculo"""
    return math.pi * (r ** 2)

print(area(2))

print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma comum

areas = []
for r in raios:
    areas.append((area(r)))

print(list(areas))

#Forma Map
#Map é uma função que recebe dois parâmetros: O primeiro é a função e o segundo é um iterável
#Tipo Map Object
areas = map(area, raios)
print(type(areas))
print(list(areas))

#Forma Map com Lambda

print(list(map(lambda r: math.pi *(r ** 2), raios)))

#Após a utilização do map() depois da primeira utilização do resultado ele zera.


#Fixação


#Temos dados iteráveis
#Temos dados: a1, a2, ... , an
#Temos Uma função:  Função f(x)
#Utilizamos a função map(f, dados) onde map vai mapear cada elemento dos dados e aplicar na função

#Map object: f(a1), f(a2), ..., f(an)



#Mais um Exemplo de map

cidades = [('Berlim', 29), ('Buenos Aires',24), ('Los Angeles', 19)]

print(cidades)

#f = 9/5 * c + 32

#Lambda

c_para_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))

print(list(map(c_para_f, cidades)))