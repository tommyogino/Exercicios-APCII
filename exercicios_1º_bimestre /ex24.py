i = 0
resultado = 0
while i < 5:
    num = float(input("Digite um numero: "))
    resultado += num
    i += 1
media = resultado / 5
print(f"A media dos numeros eh: {media:g}")