#for intermediario

frase = input('digite uma frase: ')
notspace = frase.split()
letra_sem_espaço = 0

for letras in frase :
    if letras != " ":
        letra_sem_espaço += 1

print(f"todas as palavras: {notspace}")
print(f"quantidade de palavras: {len(notspace)}")
print(f"quantidade de letras: {letra_sem_espaço}")
