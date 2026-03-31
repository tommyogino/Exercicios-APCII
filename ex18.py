login = "admin"
senha = "1234"

entrada_login = input("Digite seu login: ")
entrada_senha = input("Digite sua senha: ")

if entrada_login == login and entrada_senha == senha:
    print("Login efetuado com sucesso!")
elif entrada_login != login and entrada_senha != senha:
    print("Usuario e senha incorretos!")
elif entrada_login != login:
    print("Usuario incorreto!")
elif entrada_senha != senha:
    print("Senha incorreta!")