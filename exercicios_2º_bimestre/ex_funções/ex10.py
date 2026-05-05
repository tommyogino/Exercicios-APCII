def auth():
    user = "admin"
    pswd = "admin"
    
    while True:
        login = input("Digite seu user: ")
        senha = input("Digite sua senha: ")

        if login != user or senha != pswd:
            print("User/Senha nao encontrados!")
        else:
            print("Login efetuado com sucesso!")
            break

auth()