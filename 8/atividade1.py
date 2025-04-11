#Contagem Regressiva com Raiz Quadrada
import time # Importando o módulo time para fazer uma contagem regressiva
import math # Importando o módulo math para cálculos matemáticos

try:
    numero = int(input("Digite um número inteiro: "))
    raiz = math.sqrt(numero)

    print("Contagem regressiva:")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    print(f"A raiz quadrada de {numero} é: {raiz}")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
