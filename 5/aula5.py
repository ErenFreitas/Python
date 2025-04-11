# Introdução ao tratamento de exceções com try e except
# O bloco try contém o código que pode gerar uma exceção.
# O bloco except contém o código que será executado se uma exceção ocorrer.


try:
    numero1 = int(input('Digite um número inteiro: '))
    print(f'Você digitou o número: {numero1}')
except ValueError:
    print('Isso não é um número inteiro válido.')
