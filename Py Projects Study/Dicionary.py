"""

Dicionários

Em algumas linguagens de programação os dicionários Python são conhecidos como mapas

São coleções do tipo chave / valor

[1, 2, 3]

Dicionários são representados por chaves 

    OBS: 
        - Chave e valor são preparados por dois pontos 'Chave : valor';
        - Tanto chave quanto valor podem ser de qualquer tipo de dado
        - Podemos misturar os tipos de dados

Caso tentar fazer um acesso utilizando uma chave que não existe vai dar KeyError

"""

#Forma1 Mais comum de ser utilizada

paises = {'br': 'Brazil', 'eua': 'Estados Unidos', 'Py': 'Paraguai'}
print(paises)
print(type(paises))

#Forma2 Menos comum de ser utilizada

paises = dict(br = 'Brazil', eua = 'Estados Unidos', Py = 'Paraguai')
print(paises)
print(type(paises))

#Acessando via chave

print(paises['br'])
print(paises['eua'])

#Acessando via get
print(paises.get('br'))
print(paises.get('eua'))
#print(paises.get('eu')) gera o tipo None


#Podemos definir um valor padrão para caso não encontrado o objeto com a chave não informada
#Caso não encontre o objeto da chave informada vai retornar o valor None e não irá gerar KeyError

pais = paises.get('ru', 'não encontrado')

print(pais)