from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = date.today().year - ano_nascimento

print(f"A idade eh {idade} anos.")