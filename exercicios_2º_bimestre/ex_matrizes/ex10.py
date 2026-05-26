def ler_notas(num_alunos,num_notas):
    notas = []
    for i in range(num_alunos):
        linha = []
        for j in range(num_notas):
            nota = float(input(f"{i + 1}º Aluno | {j + 1}º Nota: "))
            linha.append(nota)
        notas.append(linha)
    return notas

def matriz(notas):
    for i in range(len(notas)):
        print(f"Aluno {i + 1}: {notas[i]}")

def main():
    total_alunos = int(input("Numero de alunos: "))
    total_notas = int(input("Numero de notas: "))
    notas = ler_notas(total_alunos, total_notas)
    matriz(notas)

main()