# Variáveis de entrada
idade = int(input('Qual é a sua idade? '))
membro_registrado_input = input('Você é um membro registrado? (sim/não) ').strip().lower()
membro_registrado = membro_registrado_input == 'sim'

# Verificando condições usando operadores lógicos
if idade >= 18 and membro_registrado:
    print("Acesso concedido: Você é maior de idade e um membro registrado.")
elif idade >= 18 and not membro_registrado:
    print("Acesso negado: Você é maior de idade, mas não é um membro registrado.")
elif idade < 18 and membro_registrado:
    print("Acesso negado: Você é um membro registrado, mas é menor de idade.")
else:
    print("Acesso negado: Você é menor de idade e não é um membro registrado.")
