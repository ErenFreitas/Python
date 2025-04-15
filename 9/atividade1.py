#atividade 1
#lista de compras 

lista_de_compras = []

while True:
    print("\nEscolha uma opção:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Sair")
    
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(item)
        print(f"{item} foi adicionado à lista.")

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print(f"{item} foi removido da lista.")
        else:
            print(f"{item} não está na lista.")

    elif opcao == "3":
        print("Itens na sua lista:")
        for i, item in enumerate(lista_de_compras):
            print(f"{i + 1}. {item}")

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
