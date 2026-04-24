valor = float(input("Digite o valor em reais: R$"))
cotacao = float(input("Digite a cotacao do dolar atual(x Reais = 1 dolar): R$ "))

dolares = valor / cotacao

print(f"R${valor:.2f} reais equivale a ${dolares:.2f} dolares.")