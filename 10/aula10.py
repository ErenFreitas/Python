# Introdução ao uso de funções em Python

# Definindo uma função simples
def saudacao():
    print("Olá! Bem-vindo ao mundo das funções em Python.")

# Chamando a função
saudacao()

# Definindo uma função com parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo ao mundo das funções em Python.")

# Chamando a função com um argumento
saudacao_personalizada("Maria")

# Definindo uma função com retorno
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")

# Definindo uma função com parâmetros padrão
def saudacao_personalizada(nome="Visitante"):
    print(f"Olá, {nome}! Bem-vindo ao mundo das funções em Python.")

# Chamando a função sem argumento
saudacao_personalizada()
# Chamando a função com argumento
saudacao_personalizada("João")
# Definindo uma função com número variável de argumentos
def soma_varios(*args):
    return sum(args)

# Chamando a função com vários argumentos
resultado_varios = soma_varios(1, 2, 3, 4, 5)
print(f"A soma de 1, 2, 3, 4 e 5 é: {resultado_varios}")