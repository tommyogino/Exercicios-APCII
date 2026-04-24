salario = float(input("Digite seu salario: R$"))

if salario > 5000:
    print(f"Desconto de 10%: R${salario * 0.9:.2f}")
else:
    print(f"Desconto de 5%: R${salario * 0.95:.2f}")