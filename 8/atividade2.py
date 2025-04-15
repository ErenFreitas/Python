palavra_secreta = "python"
letras_adivinhadas = ""
chances = 10

print("Adivinhe a palavra secreta!")

while chances > 0:
    tentativas = input("Digite uma letra: ").strip()

    try:
        if tentativas == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra secreta!")
            break

        if len(tentativas) == 0:
            print("Você não digitou nada!")

        elif len(tentativas) > 1:
            print("Digite apenas uma letra!")

        elif tentativas in palavra_secreta:
            print(f"Tem a letra '{tentativas}'!")
            letras_adivinhadas += tentativas
            chances -= 1
            print(f"Você ainda tem {chances} chances!")
            print(f"Letras adivinhadas: {letras_adivinhadas}")

        else:
            print(f"Não tem a letra '{tentativas}'!")
            chances -= 1

            print(f"Você ainda tem {chances} chances!")

    except ValueError:
        print("Por favor, digite uma letra válida.")
else:
    print("Você perdeu! A palavra secreta era:", palavra_secreta)
