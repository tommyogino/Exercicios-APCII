registra_senha = input("Digite a senha desejada: ")
valida_senha = input("Digite a sua senha novamente: ")

while registra_senha != valida_senha:
    print("Senha incorreta! Tente novamente: ")
    valida_senha = input()

print("Senha cadastrada com sucesso!")