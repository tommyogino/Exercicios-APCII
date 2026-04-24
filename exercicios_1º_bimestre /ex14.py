num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"{num1:g} eh o maior numero.")
elif num2 > num1 and num2 > num3:
    print(f"{num2:g} eh o maior numero.")
else:
    print(f"{num3:g} eh o maior numero.")