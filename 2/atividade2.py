# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

# Neste caso, '1 + int(0.5 + 0.5)' é avaliado primeiro devido às regras de precedência
# O valor resultante é 2. Em seguida, '**' (exponenciação) é aplicado a 2 ** 10
# O resultado final é 1024
calculo_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(calculo_1)  # Saída: 1024
