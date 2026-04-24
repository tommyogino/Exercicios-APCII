contador = 0 

while True:                                                                                                
    entrada = input("Digite um numero (ou 'fim' para encerrar): ")                                    
    if entrada == "fim":                                                                                   
        break                                                                                              
    num = float(entrada)
    if num > 0:
        contador += 1
print(f"{contador} dos numeros digitados sao positivos.")