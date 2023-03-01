"""
Generators

Tuple comprehension é chamado de Generators

"""

#Exemplo List Comprehension
nomes = ['Carlos', 'Miguel', 'Carla', 'Carol', 'Vanessa']
 
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)


#Exemplo Generator

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(list(res))

