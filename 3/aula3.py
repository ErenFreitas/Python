# introdução às f-strings
# F-strings são uma forma de formatar strings no Python, introduzida na versão 3.6.

nome = 'Eren Freitas'
altura = 1.70
peso = 60 

# Calcular IMC
imc = peso / (altura * altura) 

# Imprimir os dados sem usar f-strings
print(nome, 'tem', altura, 'metros de altura.')
print('Ele pesa', peso, 'quilogramas e seu IMC é', imc)

# Introduzindo f-strings

# Imprimir os dados usando f-strings
print(f"{nome} tem {altura} metros de altura.")
# A próxima linha imprime o peso, arredondando o IMC para 2 casas decimais
print(f"Pesa {peso} quilogramas e seu IMC é {imc:.2f}.")
