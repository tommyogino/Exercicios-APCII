matriz = []
tamanho_matriz = 2
for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

maior_valor = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior_valor:
            maior_valor = valor
print(f"O maior valor da matriz eh: {maior_valor}")