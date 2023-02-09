"""
Type String(tipo string)

é considerado string quando a resposta estiver em aspas simples '123', 'abc', 'True', ...
Se estiver em aspas duplas também é considerado string


Transforma todos os caracteres em Maiúsculos quando imprimir
nome = 'geek University'
print(nome.upper())

Transforma Todos os caracteres em Minúsculo quando imprimir
print(nome.lower())

Pega cada palavra e transforma em uma lista
print(nome.split())

Acesso a determinada parte da lista -> slice de string
print(nome[0:4])

Transforma as palavras em uma lista de string e faz o acesso na lista
print(nome.split()[0])

Inverter a palavra 
print(nome[::-1])


Substituir letras
print(nome.replace('G','P'))
print(nome.replace('e', 'P'))

"""

nome = 'Geek University'

print(nome)

print(type(nome))