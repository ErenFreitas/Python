"percorrer a frase e ditar a letra que mais apareceu"

frase = 'Eu gosto do flamengo'
maior_quantidade = 0
maior_letra = ''
indice = 0

while indice < len(frase): 
    letra_atual = frase[indice] 

    quantidade_letras = frase.count(letra_atual)
    if quantidade_letras > maior_quantidade:
        maior_quantidade = quantidade_letras
        maior_letra = letra_atual
    
    print(letra_atual, " ", quantidade_letras)
    indice += 1

    letra_atual == frase


print(f"a letra mais frequente é: '{maior_letra}', e a quantidade de vezes q apareceu: '{maior_quantidade}'")