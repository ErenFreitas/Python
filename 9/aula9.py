# Introdução ao tipo List
# - Listas são mutáveis, ou seja, podem ser alteradas após a criação
# - Podem conter elementos de diferentes tipos
# - Podem conter outras listas (listas aninhadas)
# - Métodos úteis: append, extend, insert, remove, pop, clear, index, count, sort, reverse

# Criando uma lista vazia
lista_vazia = []
print(lista_vazia)

# Criando uma lista com elementos
lista_com_elementos = [1, 2, 3, 4, 5]
print(lista_com_elementos)

# Criando uma lista com elementos de diferentes tipos
lista_com_diferentes_tipos = [1, "dois", 3.0, True]
print(lista_com_diferentes_tipos)

# Criando uma lista com append (adiciona 1 elemento por vez)
lista_com_append = []
lista_com_append.append(1)

# Criando uma lista com append e extend (extend adiciona vários elementos)
lista_com_append.extend([2, 3, 4])
print(lista_com_append)

# Criando uma lista com insert (insere o elemento na posição indicada)
lista_com_insert = [1, 2, 3]
lista_com_insert.insert(1, 4)  # insere o número 4 na posição 1
print(lista_com_insert)

# Criando uma lista com remove (remove o primeiro elemento com o valor especificado)
lista_com_remove = [1, 2, 3, 4, 5]
lista_com_remove.remove(3)  # remove o número 3
print(lista_com_remove)

# Criando uma lista com pop (remove e retorna o último elemento)
lista_com_pop = [1, 2, 3, 4, 5]
elemento_removido = lista_com_pop.pop()
print(lista_com_pop)
print(elemento_removido)

# Criando uma lista com clear (remove todos os elementos da lista)
lista_com_clear = [1, 2, 3, 4, 5]
lista_com_clear.clear()
print(lista_com_clear)

# Criando uma lista com index (retorna o índice do primeiro elemento com valor 3)
lista_com_index = [1, 2, 3, 4, 5]
indice = lista_com_index.index(3)
print(indice)

# Criando uma lista e alterando um valor com [i]
lista_a = ['Joao', 'Maria', 'José']
lista_b = lista_a  # lista_b aponta para a mesma lista que lista_a
lista_a[0] = "Pedro"  # altera o primeiro elemento
print(lista_a)


# Criando uma lista de nomes com range
nomes = ["Ana", "Bia", "Carlos"]
for i in range(len(nomes)):
    print(f"Nome {i}: {nomes[i]}")

