valor_hora = float(input("Qual o valor pago pela hora: R$"))
horas_trabalhadas = float(input("Quantas horas foram trabalhadas no mes: "))

salario = horas_trabalhadas * valor_hora
inss = salario * 0.11
salario_liquido = salario - inss

print(f"Salario bruto: R${salario:.2f} | Salario liquido: R${salario_liquido:.2f}")