matriz = []
tamanho_matriz = 2
total = 0

for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    for valor in linha:
        total += valor
print(f"A soma da matriz eh: {total}")
