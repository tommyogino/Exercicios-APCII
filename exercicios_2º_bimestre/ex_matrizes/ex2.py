matriz = []
tamanho_matriz = 2
for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nA matriz ficou assim: \n")
for linha in matriz:
    print(linha)