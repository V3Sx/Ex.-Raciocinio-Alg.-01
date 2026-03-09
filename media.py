def calc_media():
    nota1 = float(input("Informe a primera nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    return media

print (f"A media foi de {calc_media(): .1f} pontos")