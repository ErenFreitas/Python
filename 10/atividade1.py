# Atividade 1 com tratamento de exceções
print("Bem-vindo à calculadora simples!")
print("Operações disponíveis:")
print("1. Adição (+) subtração (-) multiplicação (*) divisão (/)")

# Recebendo os números e operação do usuário
try:
    numeros = input("Digite dois números separados por espaço: ")
    numeros = numeros.split()  # Divide os números inseridos em uma lista
    numero1 = float(numeros[0])  # Tenta converter o primeiro número
    numero2 = float(numeros[1])  # Tenta converter o segundo número
except ValueError:
    print("Erro: Você deve inserir números válidos!")
    exit()  # Se houver erro, sai do programa

# Recebendo a operação do usuário
operadores = input("Digite a operação desejada (+, -, *, /): ")

# Função da calculadora
def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        return numero1 + numero2
    elif operacao == '-':
        return numero1 - numero2
    elif operacao == '*':
        return numero1 * numero2
    elif operacao == '/':
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."

# Exibindo o resultado
print("Resultado: ", calculadora(numero1, numero2, operadores))
# Fim do programa