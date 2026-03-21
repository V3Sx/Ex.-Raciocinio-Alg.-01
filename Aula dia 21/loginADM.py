usuario = input("Informe seu nome de usuario: ")
if usuario == "admin":
    senhaADM = input(f"Ola {usuario}, insira a senha: ")
    if senhaADM == "1234":
        print("Bem-vindo!")
    else:
        print("Bloqueado >:c")
else:
    print("Usuario nao encontrado.")

