import re
# Atividade 2 - Validação de CPF


cpf = input("Digite seu CPF: ")

cpf = re.sub(r'[^0-9]', '', cpf)  # Remove caracteres não numéricos
if len(cpf) != 11 or cpf == cpf[0] * 11:
    print("CPF inválido")

else:
    soma = 0
    contador = 10
    for digito in cpf[:9]:
        soma += int(digito) * contador
        contador -= 1
    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
    
    cpf_com_digito_1 = cpf[:9] + str(digito_1)
    soma = 0
    contador = 11
    for digito in cpf_com_digito_1:
        soma += int(digito) * contador
        contador -= 1
    digito_2 = (soma * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    cpf_completo = cpf_com_digito_1 + str(digito_2)

    if cpf == cpf_completo:
        print("CPF válido")
    else:
        print("CPF inválido")

