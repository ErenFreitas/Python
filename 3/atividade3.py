# Definindo variáveis
nome = "John"
idade = 25
a = 5
b = 3
pi = 3.14159
numero_grande = 1000000
texto = "Python"
pessoa = {"nome": "Anna", "idade": 30}

# 1. Sintaxe básica com f-strings
print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# 2. Expressões dentro de f-strings
print(f"A soma de {a} e {b} é {a + b}.")

# 3. Formatação numérica (decimais e separadores de milhar)
print(f"O valor de pi é {pi:.2f}.")
print(f"O número formatado é {numero_grande:,}.")

# 4. Alinhamento de texto
print(f"{texto:>10}")  # Alinhado à direita
print(f"{texto:<10}")  # Alinhado à esquerda
print(f"{texto:^10}")  # Centralizado

# 5. Acessando valores de dicionário dentro de f-strings
print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")

# 6. Usando expressões mais complexas
altura = 1.75
print(f"Olá, {nome.upper()}! Sua altura é {altura * 100:.1f} cm.")

# Exemplo completo: combinando múltiplos aspectos em uma frase
print(f"{nome} tem {idade} anos, gosta de {texto:^10}, e o número grande é {numero_grande:,}. Pi é aproximadamente {pi:.2f}.")
