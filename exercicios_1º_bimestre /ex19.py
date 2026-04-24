while True:
    entrada = input("Digite a operacao (ex: 10 + 5): ")
    partes = entrada.split()

    try:
        num1 = float(partes[0])                                                    
        operador = partes[1]
        num2 = float(partes[2])
        break  # input válido, sai do loop
    except (IndexError, ValueError):                                               
        print("Formato inválido! Use: numero operador numero")

num1 = float(partes[0])
operador = partes[1]
num2 = float(partes[2])

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 == 0:
        print("Impossivel dividir por zero.")
    else:
        resultado = num1 / num2
else:
    print("Operador desconhecido!")

print(f"Resultado: {resultado:g}")