coordenada_x = int(input("Insira o valor da coordenada X: "))
coordenada_y = int(input("Insira o valor da coordenada Y: "))
if coordenada_x > 0 and coordenada_x < 10 and coordenada_y > 0 and coordenada_y < 10:
    print("Dentro do quadro!")
elif coordenada_x == 10 or coordenada_x == 0 or coordenada_y == 10 or coordenada_y == 0:
    print("Ta na beiradinha...")
else:
    print("PASSOU")