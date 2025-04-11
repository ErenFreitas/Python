"while dentro de while"

while True:  # Loop principal
    numero = int(input("Digite um número para ver a tabuada: "))
    
    x = 1  # Inicia o contador da tabuada
    while x <= 10:  # Loop para calcular a tabuada
        print(f"{numero} x {x} = {numero * x}")
        x += 1  # Aumenta o contador
    
    repetir = input("Deseja ver outra tabuada? (s/n): ")
    if repetir.lower() != "s":
        print("Programa encerrado.")
        break  # Sai do loop principal
