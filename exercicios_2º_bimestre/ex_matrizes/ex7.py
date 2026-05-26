matriz = []
tamanho_matriz = 2
for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

valor_coluna_0 = 0
valor_coluna_1 = 0
for linha in matriz:
    for j in range(len(linha)):
        if j == 0:
            valor_coluna_0 += linha[j]
        if j == 1:
            valor_coluna_1 += linha[j]
print(f"Soma da 1º coluna: {valor_coluna_0}\nSoma da 2ª coluna: {valor_coluna_1}")