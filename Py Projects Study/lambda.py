"""
Lambdas

Conhecidas por expressões Lambdas, são funções sem nome, ou seja, funções anônimas



"""

#Função em Python

def função(x):
    return 3*x+1

print(função(4))
print(função(7))

#função Lambda

calc = lambda x: 3 * x + 1

print(calc(4))



#Podemos ter expressões lambdas com multiplas entradas


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print (nome_completo(' angelina', 'jolie'))


#Em funções Python podemos ter nenhuma ou várias entradas.

amar = lambda : 'como nao amar python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: 3* x + y * 2

tres = lambda x,y, a: 3* 1 + x * y + a

print(amar())
print(uma(4))
print(duas(3,4))
print(tres(3,5,7))



#Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Frank Herbert', 'Arthur C. Clarke', 'H. G. Wells' ]

print(autores)

autores.sort(key = lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
