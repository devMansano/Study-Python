"""
Sorted 

o sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iterável

sorted() serve para ordenar elementos

Imprime ordenadamente gerando uma nova lista.

OBS: o sorted() só retorna uma lista com os elementos de iterável ordenados.

"""

lista = [1,2,3,4,5]

print(sorted(lista))


#adicionando parâmetros ao sorted() 
#Inversão do maior pro menor da lista com sorted()

print(sorted(lista, reverse = True))


#podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "Tweets" : ["Eu amo bolos", "Eu quero trabalhar"]},
    {"username": "Ana", "Tweets" : ["Eu amo cachorros"]},
    {"username": "Abigail", "Tweets" : []},
    {"username": "José", "Tweets" : []},
    {"username": "Thiago", "Tweets" : ["Eu amo Carros", "Vou sair hoje"]}

]

print(sorted(usuarios, key=lambda usuario: usuario["username"] ))