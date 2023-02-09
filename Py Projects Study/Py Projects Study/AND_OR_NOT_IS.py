"""

Estrutura lógica: and, or, not, is

Operador unários : not, is

Operador Binário = and, or

and utilizado para uma condição que precisam de ambos os valores True
not utilizado para a condição onde o valor do booleano é invertido
or utilizado para a condição de um ou mais valores True
is utilizado para a condição onde um valor é True

EX: 

if not ativo:
    print('é necessário ativar a conta')
else:
    print('Bem vindo usuário')
print (not ativo)


"""

ativo = True
logado = True

if ativo and logado:
    print('Bem vindo')
else :
    print('é necessário a ativação da conta')