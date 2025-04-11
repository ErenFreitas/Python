"fazendo uma calculadora em uma estrutura de repetiçao"

operadores = ['+', '-', '/', '*']

while True:
    numero1=int(input('digite um numero: '))
    numero2=int(input('digite outro numero: '))
    operador=input('digite um operador(+-/*): ')
    if operador in operadores:
        if operador == "+":
            resultado = numero1 + numero2
        elif operador == "-":
            resultado = numero1 - numero2
        elif operador == "*":
            resultado = numero1 * numero2
        elif operador == "/":
            if numero2 != 0:
                resultado = numero1 / numero2
            else:
                print('erro na divisao')
                continue
        print(f"O resultado é: {resultado}")
    else: print('operador invalido')
