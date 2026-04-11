nmr_inicial = int(input("manda um numero inicial: "))
final = int(input("manda um numero final: "))

for i in range(nmr_inicial, final + 1):
    print(f"tabuada do {i}: ")
    for z in range(1, 11):
        print(f"{i} x {z} = {i*z}")