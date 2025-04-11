# Atividade

"""
Crie um programa que peça ao usuário seu primeiro nome. Se o nome tiver 4 letras ou 
menos, exiba "Seu nome é curto"; se tiver entre 5 e 6 letras, exiba 
"Seu nome é normal"; se tiver mais de 6 letras, exiba "Seu nome é muito longo."
"""

# Programa para avaliar o comprimento do nome do usuário

# Solicitar ao usuário que insira seu primeiro nome
nome = input("Digite seu primeiro nome: ")

# Verificar o comprimento do nome e exibir a mensagem apropriada
if len(nome) <= 4:
    print("Seu nome é curto.")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal.")
else:
    print("Seu nome é muito longo.")
