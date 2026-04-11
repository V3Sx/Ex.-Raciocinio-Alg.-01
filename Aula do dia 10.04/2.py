soma = 0
expressao = ""
count = 0

inteiro_positivo = int(input("manda um numero positivo: "))

while inteiro_positivo <= 0:
    inteiro_positivo = int(input("manda um numero POSITIVO: "))

while count <= inteiro_positivo:
    soma += count
    
    if count == inteiro_positivo:
        expressao += str(count)
    else:
        expressao += str(count) + " + "
    count += 1
print(expressao, "=", soma)