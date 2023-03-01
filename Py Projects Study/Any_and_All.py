"""
Any and All

all() retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.


all() entende que o iterável convertido em boolean é verdadeiro porém  um iterável em boolean é Falso


Any() retorna True se qualquer elemento do iterável for verdadeiro; se o iterável estiver vazio ele retornará False



"""

#Exemplo

print(all([0,1,2,3,4,5])) #Todos os elementos são verdadeiros ?

#vai dar false pois o 0 é considerado false no Python

print(type(all((1,2,4,5)))) 
# Os Elementos são Verdadeiros pois não contêm o zero ( 0 ) que é considerado false em Python

print(all([Letra for Letra in 'eiof' if Letra in 'aeiou' ]))


print(any([0,1,2,3,4]))

print(any([0, False, {}, [], ()]))

nomes = ['Carlos', 'Miguel', 'Carla', 'Carol', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

