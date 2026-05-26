matriz = []
tamanho_matriz = 2
for i in range(tamanho_matriz):
    linha = []
    for j in range(tamanho_matriz):
        valor = int(input(f"[[{i}] [{j}]]: "))
        linha.append(valor)
    matriz.append(linha)

num_pares = []
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            num_pares.append(valor)
print(f"Os numeros pares presentes na matriz sao: {num_pares}")