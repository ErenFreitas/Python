# Atividade
'''
Crie um programa que peça ao usuário para digitar um número inteiro,
informe se o número é par ou ímpar. Se o usuário não
digitar um número inteiro, informe que não é um número inteiro.
'''

# Solicitar ao usuário que insira um número inteiro
entrada_numero = input('Digite um número inteiro: ')

try:
    # Tentar converter a entrada para um número inteiro
    numero_digitado = int(entrada_numero)

    # Verificar se o número é par ou ímpar
    if numero_digitado % 2 == 0:
        print(f'O número {numero_digitado} é par.')
    else: 
        print(f'O número {numero_digitado} é ímpar.')
except ValueError:
    # Se a conversão falhar, informar que não é um número inteiro
    print('Isso não é um número inteiro.')
