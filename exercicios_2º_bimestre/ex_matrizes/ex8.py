matriz_identidade = []

for i in range(3):
    linha = []
    for j in range(3):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)

print("A matriz identidade eh:")
for linha in matriz_identidade:
    print(linha)