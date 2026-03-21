ano = int(input("Insira um ano: "))
if ano % 4 == 0 and ano % 100 != 0:
    print(f"{ano} eh um ano bissexto!")
else:
    print(f"{ano} nao eh um ano bissexto!")