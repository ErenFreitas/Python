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