def fibonacci(n):
    
    a, b = 0, 1
    sequencia = []

    for _ in range(n + 1):
        sequencia.append(a)
        a, b = b, a + b
    print(sequencia)
    
fibonacci(int(input("Digite o valor para a sequencia de fibonacci: ")))

