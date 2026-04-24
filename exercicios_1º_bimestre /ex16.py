idade = int(input("Digite a idade: "))

if idade < 18:
    print("Crianca.")
elif idade < 60:
    print("Adulto.")
else:
    print("Idoso.")