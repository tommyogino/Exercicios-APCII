# Parte 1 - Arquitetura de Hardware
'''
1. Explique o que é CPU.
    CPU eh o processador do computador, responsavel por executar instrucoes dos programas. 
    Faz operacoes aritmeticas, logicas e de controle, sendo considerado o "cerebro" do computador.

2. Qual a função da memória RAM?
    A RAM seria a memoria de trabalho do computador. Armazena temporariamente os dados de programas
    que estao sendo usados. Nao armazena permanentemente, perde tudo ao desligar o computador.

3. Diferencie armazenamento (HD/SSD) de memória RAM.
    Diferente da memoria RAM, o HD/SSD armazena permanentemente os dados, tendo muito mais espaco, 
    sendo muito mais lenta que a RAM, porem mantem os dados mesmo apos o desligamento do computador.

4. O que são dispositivos de entrada? Cite exemplos.
    Dispositivos de entrada sao tudo que permitem que o usuario interaja e envie dados para o computador.
    Ex: teclado, mouse, microfone, webcam.

5. O que são dispositivos de saída? Cite exemplos.
    Dispositivos de saida sao tudo que permitem que o computador envie informacoes para o usuario.
    Ex: Monitor, fones de ouvido, caixas de som.
'''

# Parte 2 - Variaveis

# Ex 6
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(f"{nome}, {idade}")

# Ex 7

a = float(input("Digite o primeiro numero: "))
b = float(input("Digite o segundo numero: "))
print(f"A soma de {a} e {b} eh: {a + b}")

# Ex 8

num_dobro = float(input("Digite um numero: "))
print(f"O dobro eh: {num_dobro*2}")

#Ex 9 

reais = float(input("Digite um valor em reais: R$"))
print(f"O valor em dolares eh: ${reais * 5.0:.2f}")

# Ex 10

ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2026 - ano_nascimento
print(f"Sua idade eh {idade} anos.")

# Parte 3 - Estruturas condicionais

# Ex 11

verifica_num = float(input("Digite um numero: "))

if verifica_num >= 0:
    print(f"{verifica_num} eh um numero positivo.")
else:
    print(f"{verifica_num} eh um numero negativo.")

# Ex 12

verifica_num_par_impar = float(input("Digite um numero: "))

if verifica_num_par_impar % 2 == 0:
    print(f"O numero {verifica_num_par_impar} eh par!")
else:
    print(f"O numero {verifica_num_par_impar} eh impar!")

# Ex 13

nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

if (nota_1 + nota_2) / 2 >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")

# Ex 14

valor_idade = int(input("Digite sua idade: "))

if valor_idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")

# Ex 15

usuario = "admin"
senha = "1234"

login = input("Digite seu usuario: ")
senha_login = str(input("Digite sua senha: "))

if login == usuario and senha_login == senha:
    print("Login efetuado!")
elif login != usuario:
    print("Usuario incorreto!")
elif senha_login != senha:
    print("Senha incorreta!")
else:
    print("Usuario e senha incorretos!")

# Desafio

nome_financiar = input("Digite seu nome: ")
idade_financiar = int(input("Digite sua idade: "))
salario_financiar = float(input("Digite seu salario: R$"))

if idade >= 18 and salario_financiar > 2000:
    print("Parabens! Vc pode financiar um carro!")
else:
    print("Infelizmente vc nao pode financiar um carro! :(")