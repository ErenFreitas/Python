# Introdução ao while e break

contador = 0
while True:  # Loop infinito
    print("O contador é:", contador)
    contador += 1
    
    if contador >= 5:
        print("O contador chegou a 5, saindo do loop")
        break  # Encerra o loop quando o contador é 5
