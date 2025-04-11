#introduçao ao import

import time

print("esperando 5 segundos...")
time.sleep(5)
print("5 segundos se passaram")

#time é um modulo que tem funçoes para trabalhar com tempo
#time.sleep(5) faz o programa esperar 5 segundos antes de continuar
#time é um modulo que ja vem com o python, nao precisa instalar nada

#usando math
import math

raiz = math.sqrt(16)
print("a raiz quadrada de 16 é:", int(raiz))
#math é um modulo que tem funçoes matematicas, como raiz quadrada, seno, cosseno, etc
#math.sqrt(16) calcula a raiz quadrada de 16
#math é um modulo que ja vem com o python, nao precisa instalar nada


# Raiz quadrada
print(math.sqrt(16))  # Saída: 4.0

# Potência
print(math.pow(2, 3))  # Saída: 8.0

# Fatorial
print(math.factorial(5))  # Saída: 120

# Número pi
print(math.pi)  # Saída: 3.141592653589793

# Seno de 90 graus (em radianos!)
print(math.sin(math.radians(90)))  # Saída: 1.0
