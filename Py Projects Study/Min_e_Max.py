"""
Min and Max

max() retorna o maior valor de um iterável ou o maior de dois ou mais elementos
min() retorna o menor valor de um iterável ou o menor de dois ou mais elementos

"""

lista = [1517, 525484, 3651, 28492, 656548, 21615]

conjunto = {1517, 525484, 3651, 28492, 656548, 21615}

tupla = (1517, 525484, 3651, 28492, 656548, 21615)

dicionario = {'a':1517, 'b': 525484,'c': 3651,'d': 28492,'e': 656548,'f': 21615}


print(max(lista))
print(max(tupla))
print(max(conjunto))
print(max(dicionario.values()))


#Faça um programa que receba dois valores de um usuário e retorne o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))


