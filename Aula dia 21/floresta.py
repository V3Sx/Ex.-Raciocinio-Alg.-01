print("Voce esta em uma floresta e precisa escolher um caminho para seguir. Voce pode escolher esquerda ou direita.")
lados = input("direita ou esquerda? ")
if lados == "esquerda":
    print("Indo para a esquerda voce encontra um rio.")
    atravessar = input("Voce escolher atravessar ou permanecer? ")
    if atravessar == "atravessar":
        print("Voce chegou em uma vila segura. viva")
    else:
        print("voce permanece perdido na floresta mane.")
else:
    print("Ao ir para a direita voce encontra uma montanha!")
    subir = input("Voce escolhe subir ou voltar? ")
    if subir == "subir":
        print("Voce encontrou um tesouro perdido!! estamos ricos.")
    else:
        print("Voce permanece perdido na floresta.")
