ano = int(input("Informe o ano em que nasceu: "))
ano_atual = 2026
def calculo_meses():
    idade = 2026 - ano
    return idade * 12

print (f"voce tem {calculo_meses()} meses!")