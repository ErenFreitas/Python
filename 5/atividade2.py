# Atividade

'''
Crie um programa que pergunte ao usuário a hora e, com base na 
hora fornecida, exiba a saudação apropriada. Ex.: 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

# Definir os intervalos para as saudações
bom_dia = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
boa_tarde = (12, 13, 14, 15, 16, 17)
boa_noite = (18, 19, 20, 21, 22, 23)

# Obter a hora atual do usuário
try:
    hora = int(input('Qual é a hora atual (0-23)? '))  # Converter entrada para inteiro
    
    # Verificar a saudação com base na hora
    if hora in bom_dia:
        print(f'Bom dia! A hora atual é {hora}.')
    elif hora in boa_tarde:
        print(f'Boa tarde! A hora atual é {hora}.')
    elif hora in boa_noite:
        print(f'Boa noite! A hora atual é {hora}.')
    else:
        print('Por favor, insira uma hora válida entre 0 e 23.')
except ValueError:
    print('Entrada inválida. Por favor, insira um número entre 0 e 23.')
