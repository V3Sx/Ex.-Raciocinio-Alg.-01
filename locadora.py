def valor_cobrado(dias):
    return dias * 100

total_dias = int(input("Quantos dias o carro foi alugado? "))
valor = valor_cobrado(total_dias)

print(f"O valor a ser cobrado eh: {valor}R$")