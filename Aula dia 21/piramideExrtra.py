print("Vamos montar um triangulo juntos, pra isso preciso que me informe as seguintes medidas:")
lado_a = float(input("O valor do lado A: "))
lado_b = float(input("O valor do lado B: "))
lado_c = float(input("Informe o valor do terceiro lado: "))
print()
if lado_a == lado_b == lado_c:
    print("Seu triangulo eh equilatero!")
elif (lado_a == lado_b != lado_c) or \
     (lado_a == lado_c != lado_b) or \
     (lado_b == lado_c != lado_a):
     print("O seu triangulo eh isosceles (dois lados iguais, um diferente.)")
else:
     print("O seu triangulo eh escaleno (todos os lados sao diferentes.)")

    