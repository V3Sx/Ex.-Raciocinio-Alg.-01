banana, ameixa, uva = 2, 5, 4

print(f"""Tabela de valores:
banana: {banana} R$
ameixa: {ameixa} R$
uva: {uva} R$""")

quantidade_kilos = float(input("Informe a quantidade de kilos do produto: "))
fruta_escolhida = input("Agora escolha uma fruta da tabela: ")

def preco_kilo():
    if fruta_escolhida == "banana":
        preco = banana
    elif fruta_escolhida == "ameixa":
        preco = ameixa
    elif fruta_escolhida == "uva":
        preco = uva
    else:
        print("Fruta inválida")
        return 0
    
    preco_total = quantidade_kilos * preco
    return preco_total

print(f"O preço total é: {preco_kilo()}R$")