num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

if num2 == 0:
    divisao = "n eh possivel dividir por 0"
    div_inteira = "n eh possivel dividir por 0"
    resto = "n eh possivel dividir por 0"
else:
    divisao = num1 / num2
    div_inteira = num1 // num2
    resto = num1 % num2

print(f"Soma: {soma} | Subtracao: {subtracao} | Multiplicacao: {multiplicacao} | Divisao: {divisao} | Divisao inteira: {div_inteira} | Resto: {resto}.")