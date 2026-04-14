fatorial = int(input("Digite um numero para saber o fatorial dele: "))
resultado = 1
i = fatorial

while i > 1:

    resultado *= i
    i -= 1

print(f"O fatorial eh: {resultado}")