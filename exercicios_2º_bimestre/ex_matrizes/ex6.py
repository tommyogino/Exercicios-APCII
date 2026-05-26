matriz = []
tamanho_matriz = 2
for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    soma_linha = 0
    for valor in linha:
        soma_linha += valor
    print(f"A soma do elementos da linha eh: {soma_linha}")