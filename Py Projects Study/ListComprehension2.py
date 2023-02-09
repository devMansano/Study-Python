"""
List Comprehension Part 2

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension


"""

#Exemplo

#1

numeros = [1,2,3,4,5,6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)


#2 Refatorar
#Qualquer número par módulo de 2 é 0 e em Python é False. Not False = True

pares = [numero for numero in numeros if not numero % 2]

#Qualquer número impar módulo de 2 é 1 e em Python é True.
impares = [numero for numero in numeros if numero % 2] 

print(pares)
print(impares)

#3 

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)