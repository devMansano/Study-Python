"""
List Comprehension

- utilizando List Comprehension podemos gerar novas listas com dados processados a partir de outro iterável.

#Sintaxe da List comprehension

[dado for dado in terável]



#Exemplo 1
numeros = [1,2,3,4,5]

res= [numero * 10 for numero in numeros]

print(res)



Para entender melhor o que aconteceu, será dividido a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte : numero * 10

Exemplo 2
res = [numero / 2 for numero in numeros]
print(res)

def funcao(valor):
    return valor * valor

res = [funcao(numero) for numero in numeros ]
print(res)



"""

"""
#List Comprehension versus Loop

#Loop
numeros = [1,2,3,4,5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
    
print(numeros_dobrados)


#List Comprehension
print([numero * 2 for numero in [1,2,3,4,5]])


#Outro Exemplo

#1 Colocando as letras em maiúsculo
 
nome = 'Geek University'

print([letra.upper() for letra in nome])

"""

#2 Letra inicial em maiúsculo

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = 'julia', 'geovana', 'lucas', 'josé'

print([caixa_alta(amigo) for amigo in amigos])

#OBS : se a primeira letra for repetida mais de 1 vez em outra posição do nome ambas serão alteradas

#Exemplo 
amigos = 'julia', 'geovana', 'abigail', 'josé'

print([caixa_alta(amigo) for amigo in amigos])


#3 Vai gerar a tabuada do 3 até a 3x9

print([numero * 3 for numero in range (1,10)])

#4 Gerando uma lista para cada valor dentro da lista e convertendo para boolean

print([bool(valor) for valor in [0, [], '', True, 1 , 3.14]])

#5 Vai gerar uma lista de strings com a lista de inteiros 

print([str(numero) for numero in [1,2,3,4,5]])