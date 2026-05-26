matriz = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]
]

busca = int(input("Digite o numero que deseja buscar a posicao na matriz: "))
pos = None

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == busca:
            pos = (i, j)
if pos:
    print(f"Encontrado na posicao: [{pos[0]}, {pos[1]}]")
else:
    print("Numero nao encontrado dentro da matriz!")