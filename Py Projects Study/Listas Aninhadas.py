"""
Listas Aninhadas

-Algumas linguagens possuem estruturas de dados conhecidos como arrays
    -Unidimensional
    -Multidimensional
    
Em Python temos as Listas

numeros = [ 1, 'b', 3.245, True, 5]


"""

#Exemplo

Listas = [[1,2,3], [4,5,6],[7,8,9]] # Matriz 3x3

print(Listas)


#Como podemos acessar os dados ?

print(Listas[0]) #Acessa o local da primeira lista
print(Listas [0] [2])

#iterando com loop em uma lista Aninhada

for lista in Listas:
    for num in lista:
        print(num)
        
# Usando o List Comprehension

[[print(valor) for valor in lista] for lista in Listas]


#Gerando um tabuleiro/Matrix 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]

velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)] for valor in range(1, 4)]

print(tabuleiro)
print(velha)

#Gerando valores iniciais

print([['*' for i in range(1,4) ] for j in range(1,4)])