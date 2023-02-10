"""
Dictionary Comprehension

Se quisermos criar uma lista fazemos:

Lista = [1,2,3,4]

Se quisermos criar uma tupla: 

tupla = 1, 2, 3, 4

Se quisermos criar um conjunto:

Conjunto = {1, 2, 4 ,5}

Se quisermos criar um dicionário:

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}


#Sintaxy Dictionary

{chave: valor for valor in iterável}

#Sintaxy List Comprehension
[valor for valor in iterável]


#Exemplo

numeros = {'a': 1, 'b':32, 'c': 4, 'd':5 }
tupla = (1,2,3,4,5)


quadrado = {chave:valor ** 2 for chave, valor in numeros.items()}
quadrado = {valor:valor ** 2 for valor in tupla}


print(numeros)
print(quadrado)


"""
#Mistura entre uma lista e uma string para gerar um dicionário
chaves = 'abcde'
valores = [1,2,3,4,5]

mistura = {chaves[i]:valores[i] for i in range(0, len(chaves)) }

print(mistura)



#Exemplo com lógica condicional

numeros = [1,2,3,4,5]

res = {num:('par' if num % 2 == 0 else 'impar')for num in numeros}

print(res)