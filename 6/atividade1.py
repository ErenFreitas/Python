'''Escreva um programa em Python que escolha um número fixo (por exemplo, 25) e peça ao usuário para adivinhar qual é esse número.
O programa deve continuar pedindo um palpite até o usuário acertar.
A cada palpite, o programa informa se o número correto é maior ou menor que o palpite do usuário. '''

print('*Adivinhe o Numero*')

Numero_Certo = 5
Numero_Palpite = int(input('Digite um numero de 0 a 10: '))

while Numero_Palpite != Numero_Certo:
    print('Voce errou, tente novamente')
    if Numero_Palpite > Numero_Certo:
        print('o numero escolhido é maior')
    else: print ('O numero escolhido é menor')

    Numero_Palpite = int(input('Digite novamente: '))

print('voce acertou')