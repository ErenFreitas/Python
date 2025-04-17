# Introdução a Tuplas

# Tuplas são estruturas de dados imutáveis em Python.
# Elas são definidas usando parênteses () e podem conter qualquer tipo de dado.

# Exemplo de criação de uma tupla
tupla_exemplo = (1, 2, 3, "Python", True)

# Acessando elementos de uma tupla (indexação começa em 0)
print(tupla_exemplo[0])  # Saída: 1
print(tupla_exemplo[3])  # Saída: Python

# Tuplas são imutáveis, ou seja, não podemos alterar seus elementos
# tupla_exemplo[0] = 10  # Isso causará um erro

# Podemos usar tuplas para armazenar múltiplos valores em uma única variável
coordenadas = (10.5, 20.3)
print(f"Coordenadas: {coordenadas}")

# Desempacotamento de tuplas
x, y = coordenadas
print(f"x: {x}, y: {y}")

# Tuplas podem ser usadas como chaves em dicionários (são hasháveis)
dicionario = {(1, 2): "Ponto A", (3, 4): "Ponto B"}
print(dicionario[(1, 2)])  # Saída: Ponto A

# Criando uma tupla com um único elemento (necessário incluir uma vírgula)
tupla_unica = (42,)
print(type(tupla_unica))  # Saída: <class 'tuple'>

# Funções úteis com tuplas
numeros = (10, 20, 30, 40, 50)
print(len(numeros))  # Saída: 5 (tamanho da tupla)
print(max(numeros))  # Saída: 50 (maior valor)
print(min(numeros))  # Saída: 10 (menor valor)
print(sum(numeros))  # Saída: 150 (soma dos valores)