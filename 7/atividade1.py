#Atividade: Contador de Vogais

vogais = ('a', 'e', 'i', 'o', 'u')
palavra = input('Digite uma palavra: ').lower().strip()

tem_vogal = False

vogais_encontradas = []  # Lista para armazenar as vogais encontradas

for caracteres in palavra:
    if caracteres in vogais:
        vogais_encontradas.append(caracteres)  # Adiciona a vogal à lista
        tem_vogal = True

if tem_vogal:
    print("As vogais são:", " ".join(vogais_encontradas))
else:
    print("Nenhuma vogal encontrada!")
