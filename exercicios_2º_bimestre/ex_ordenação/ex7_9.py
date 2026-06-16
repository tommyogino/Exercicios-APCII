"""
7. Ordene lista de números digitados.
8. Busque elemento após ordenar.
9. Conte número de comparações.

"""
#ex7
import ex1_6

def criar_lista():
    lista = []

    tamanho_lista = int(input("Digite o numero de valores desejados a adicionar: "))

    for i in range(tamanho_lista):
        valor = int(input(f"Digite o {i + 1}º valor: "))
        lista.append(valor)
    
    return lista

lista = criar_lista()
print(f"Lista desordenada: {lista}")

lista_ordenada = ex1_6.bubble_sort(lista)
print(f"Lista ordenada: {lista_ordenada}")

#ex8
buscar_elemento = int(input("Digite o valor a ser buscado na lista: "))
pos_elemento = ex1_6.busca_linear(lista_ordenada, buscar_elemento)
print(f"O elemento esta na posicao {pos_elemento}")

#ex9
def comp_bubble_sort(lista):
    comparacoes = 0
    valor = len(lista)

    for i in range(valor):
        trocou = False
        for j in range(0, valor - i - 1):
            comparacoes += 1
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        if not trocou:
            break
    
    return lista, comparacoes