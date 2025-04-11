# Lista de frutas disponíveis
frutas_disponiveis = ['maçã', 'banana', 'laranja', 'uva']

# Solicita ao usuário que insira o nome de uma fruta
fruta = input('Por favor, insira o nome de uma fruta: ').strip().lower()

# Usando 'in' para verificar se a fruta está na lista
if fruta in frutas_disponiveis:
    print(f'{fruta.capitalize()} está disponível.')
else:
    print(f'{fruta.capitalize()} não está disponível.')

# Verificando se uma fruta específica NÃO está na lista usando 'not in'
if 'abacaxi' not in frutas_disponiveis:
    print('Abacaxi não está disponível.')
