'''
Lista de Exercícios - Busca e Ordenação
1. Implemente busca linear.
2. Implemente busca binária.
3. Compare resultados das duas buscas.
4. Implemente bubble sort.
5. Implemente selection sort.
6. Implemente insertion sort.

'''
#ex1
def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

#ex2
def busca_binaria(lista, alvo): 
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        centro = (esquerda + direita) // 2

        if lista[centro] == alvo:
            return alvo
        elif lista[centro] < alvo:
            esquerda = centro + 1
        else:
            direita = centro - 1

    return -1

#ex3
'''
lista_ex3 = [1,2,3,4,5,10,9,8,7,6]

print(busca_linear(lista_ex3, 10))
Retorna a posicao correta do valor
print(busca_binaria(lista_ex3, 10))
N retorna a posicao correta do valor pela lista nao estar ordenada
'''

#ex4
def bubble_sort(lista):
    valor = len(lista)

    for i in range(valor):
        trocou = False
        for j in range(0, valor - i - 1):
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        
        if not trocou:
            break

    return lista

#ex5
def selection_sort(lista):
    valor = len(lista)

    for i in range(valor):
        index_min = i
        for j in range(i + 1, valor):
            
            if lista[j] < lista[index_min]:
                index_min = j
        
        lista[i], lista[index_min] = lista[index_min], lista[i]
    
    return lista

#ex6
def insertion_sort(lista):

    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave
    
    return lista
