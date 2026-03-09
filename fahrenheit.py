celsius = int(input("Informe quantos graus celsius: "))
def celsius_fahrenheit():
    transformacao = (celsius * 9/5) + 32
    return transformacao

print (f"{celsius} graus celsius eh equivalente a {celsius_fahrenheit()} graus farenheit")