#Atividade: Contagem de Letras e Vogais

palavra = input('digite uma palavra: ').strip().lower()
vogais = ['a', 'e', 'i', 'o', 'u']

total_vogais = 0

for caracteres in palavra:
    total_letras = caracteres
    if caracteres in vogais:
        total_vogais += 1

print(f"Quantidade de letras: {len(palavra)}")
print(f"Quantidade de vogais: {total_vogais}")