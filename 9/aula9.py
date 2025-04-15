#introduçao ao tipo List
# Listas são mutáveis, ou seja, podem ser alteradas após a criação
# Listas podem conter elementos de diferentes tipos
# Listas podem conter outras listas
# Listas podem conter até 100 elementos
# metodos de listas: append, insert, remove, pop, clear, index, count, sort, reverse


# Criando uma lista vazia
lista_vazia = []
print(lista_vazia)


# Criando uma lista com elementos
lista_com_elementos = [1, 2, 3, 4, 5]
print(lista_com_elementos)


# Criando uma lista com elementos de diferentes tipos
lista_com_diferentes_tipos = [1, "dois", 3.0, True]
print(lista_com_diferentes_tipos)


# Criando uma lista com outras listas
lista_com_outros_listas = [1, 2, [3, 4], 5]
print(lista_com_outros_listas)


# Criando uma lista com 100 elementos
lista_com_100_elementos = list(range(100))
print(lista_com_100_elementos)


# Criando uma lista com 100 elementos de diferentes tipos
lista_com_100_elementos_diferentes_tipos = list(range(100)) + ["um", "dois", "três"]
print(lista_com_100_elementos_diferentes_tipos)


# Criando uma lista com 100 elementos com outras listas
lista_com_100_elementos_com_outros_listas = list(range(100)) + [[1, 2], [3, 4], [5, 6]]
print(lista_com_100_elementos_com_outros_listas)