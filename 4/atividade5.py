# Lista de usuários bloqueados e assentos disponíveis
lista_usuarios_bloqueados = ['John', 'Mary', 'Julia']
assentos_disponiveis = ['A1', 'A3', 'A4']

# Pergunta ao usuário seu nome e escolha de assento
usuario = input('Qual é o seu nome? ').strip().capitalize()
assento = input('Qual é o seu assento? ').upper().strip()

# Verifica se o assento está disponível e o usuário não está bloqueado
if assento in assentos_disponiveis and usuario not in lista_usuarios_bloqueados:
    print(f'Assento {assento} reservado com sucesso para {usuario}.')
# Verifica se o usuário está bloqueado
elif usuario in lista_usuarios_bloqueados:
    print(f'Usuário {usuario} está banido.')
# Verifica se o assento está indisponível ou não existe
elif assento not in assentos_disponiveis:
    print(f'Assento {assento} não está disponível ou não existe.')
# Mensagem de erro genérica
else:
    print(f'Ocorreu um erro ao reservar o assento {assento}.')
