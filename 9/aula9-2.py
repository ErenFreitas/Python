#introduçao ao desempacotamento de listas
# Criando uma lista de nomes

lista_nomes = ['João', 'Maria', 'José']
nome1, nome2, nome3 = lista_nomes
print(nome2)

lista_nomes2 = ['Ana', 'Bia', 'Carlos']
nome_1, *_ = ['Ana', 'Bia', 'Carlos']
print(nome_1)  # imprime 'Ana'


# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Desempacotando a lista em variáveis
a, b, c, d, e = numeros
print(a, b, c, d, e)


# Desempacotando a lista em variáveis com o operador * (asterisco)
a, *b = numeros
print(a)  # imprime 1
print(b)  # imprime [2, 3, 4, 5]


# Criando uma lista de listas (representando salas com nomes)
salas = [
    # Sala 0 com dois nomes
    ['Maria', 'Helena', ],  # 0
    # Sala 1 com um nome
    ['Elaine', ],  # 1
    # Sala 2 com três nomes
    ['Luiz', 'João', 'Eduarda', ],  # 2
]
print(salas[2, 1])  # imprime 'João'