"""
Set Comprehension

Lista = [1,2,3,4,5]

Set = {1, 2, 3, 4, 5}


"""

numeros = {num for num in range(1, 7)}
print(numeros)

#Desafio! faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {num: num for num in range(1, 7)}
print(numeros)

#para finalizar

letras = {letra for letra in 'Geek University'}
print(letras)