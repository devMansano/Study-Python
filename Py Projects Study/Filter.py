"""
Filter

Serve para filtrar dados de uma determinada coleção -> filter()


a diferença entre map() e filter() é :

map() recebe dois parâmetros, uma função e um iterável e retorna um map object (objeto mapeado),
mapeando para cada elemento do iterável

filter() recebe dois parâmetros, uma função e um iterável e retorna um filter object (Objeto filtrado),
que filtrará de acordo com a função

"""

#Biblioteca para trabalhar com dados estatísticos
import statistics


#dados coletados de um sensor
dados = [1.3, 2.5, 0.8, 4.1, 4.3]

media = statistics.mean(dados)

print (media)
#assim como na função map(), o filter() recebe dois parâmetros, sendo eles uma função e um iterável

res = filter(lambda x: x > media, dados)

print(list(res))

#obs : Assim como na função map após ser utilizados os dados de filter() eles são excluidos da memória.

paises = ['', 'Argentina', '', 'Brazil', '', '', 'Equador']

res = filter(None, paises)
print(list(res))

#Outra forma de fazer a filtragem sem usar o none
#Cuidado pois pode haver problemas por considar o 0 como False.
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

#Outra forma de filtrar
res = filter(lambda pais: pais != '', paises )
print(list(res))


#Exemplo mais complexo

usuarios = [
    {"username": "samuel", "Tweets" : ["Eu amo bolos", "Eu quero trabalhar"]},
    {"username": "ana", "Tweets" : ["Eu amo cachorros"]},
    {"username": "Abigail", "Tweets" : []},
    {"username": "José", "Tweets" : []},
    {"username": "Thiago", "Tweets" : ["Eu amo Carros", "Vou sair hoje"]}

]


#filtrar os usuários

inativos = filter(lambda tweet: len(tweet['Tweets']) == 0, usuarios )

res = filter(lambda tw: not tw['Tweets'], usuarios)

print(list(res))

print(list(inativos))

#Como combinar filter e map
nomes = ['Vanessa', 'Ana', 'Jurema']

#Criar uma lista contendo "sua instrutora é" + nome, desde que cada nome tenha menos de 5 caracteres

#Maneira 1 de fazer
res = filter(lambda nome: len(nome) < 5, nomes)
lista = list(map(lambda nome: f'Sua Instrutora é: {nome}',res ))

print(lista)

#Maneira 2 de fazer

lista = list(map(lambda nome: f'Sua Instrutora é: {nome}',filter(lambda nome: len(nome) < 5, nomes) ))

print(lista)
