# Pergunte o nome e a idade do usuário
nome = input('Qual é o seu nome? ').capitalize().strip()
idade = input('Qual é a sua idade? ')

# Verifique se tanto o nome quanto a idade foram preenchidos
if nome and idade:
    print(f'Seu nome é {nome}')
    print('Seu nome invertido é:', nome[::-1])
    
    # Verifique se o nome contém espaços
    if " " in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contém espaços')
    
    # Conte o número de caracteres no nome
    tamanho_nome = len(nome)
    print(f'Seu nome tem {tamanho_nome} caracteres!')
    
    # Exiba a primeira e a última letra do nome
    print('A primeira letra do seu nome é:', nome[0])
    print('A última letra do seu nome é:', nome[-1])
else:
    print("Desculpe, você deixou alguns campos vazios.")
