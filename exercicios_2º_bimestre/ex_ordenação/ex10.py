def insertion_sort_nomes(lista):

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j].lower() > chave.lower():  # compara ignorando caixa
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

def criar_lista_nomes():

    n = int(input("Digite a quantidade de nomes: "))
    nomes = []

    for i in range(n):
        nome = input(f"Digite o {i + 1}º nome: ")
        nomes.append(nome)
   
    return nomes

nomes = criar_lista_nomes()
nomes_ordenados = insertion_sort_nomes(nomes)
print(f"Nomes ordenados: {nomes_ordenados}")