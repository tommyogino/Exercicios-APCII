while True:
    print("\n--- MENU ---")
    print("1 - Opcao 1")
    print("2 - Opcao 2")
    print("3 - Opcao 3")
    print("4 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        print("Voce escolheu a Opcao 1")
    elif opcao == "2":
        print("Voce escolheu a Opcao 2")
    elif opcao == "3":
        print("Voce escolheu a Opcao 3")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opcao invalida! Tente novamente.")
