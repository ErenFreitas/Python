#A função 'print' permite que você imprima informações no console.
print(12, 23,)
print('maçã', 'caneta')

#O parâmetro 'sep' é usado na função print() para especificar o separador entre os diferentes argumentos sendo impressos.
print(12, 23, sep='-')
print('maçã', 'caneta', sep='-')
#A vírgula entre os argumentos na função print() é o que permite a separação dos valores.

#O parâmetro 'end' é usado na função print() em Python para especificar o que será impresso ao final da impressão dos argumentos.
print(12, 23, sep='-', end='\n')#Em Python, o caractere especial \n representa uma nova linha
print('maçã', 'caneta', sep='-', end='?')

#Vamos tentar o mesmo código sem usar \n para ver o resultado.

print(12, 23, sep='-', end='') #sem usar \n
print('maçã', 'caneta', sep='-', end='?')
