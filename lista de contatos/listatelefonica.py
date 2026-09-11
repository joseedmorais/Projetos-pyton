
contatos = []

while True:
    print("\n-------- MENU PRINCIPAL --------")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Pesquisar contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    
    if opcao == "1":
        print("\n-------- ADICIONAR CONTATO --------")

        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o número de telefone do contato: ")
        email = input("Digite o email do contato: ")

        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        contatos.append(contato)

        print("Contato adicionado com sucesso!")

    
    elif opcao == "2":
        print("\n-------- LISTAR CONTATOS --------")

        if len(contatos) == 0:
            print("Nenhum contato cadastrado.")

        else:
            for contato in contatos:
                print("----------------------")
                print(f"Nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")

    
    elif opcao == "3":
        print("\n-------- PESQUISAR CONTATO --------")

        nome_pesquisa = input("Digite o nome do contato cadastrado: ")

        encontrado = False

        for contato in contatos:
            if contato["nome"].lower() == nome_pesquisa.lower():
                print("----------------------")
                print("Contato encontrado!")
                print(f"Nome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")

                encontrado = True
                break

        if encontrado == False:
            print("Contato não encontrado.")

    
    elif opcao == "4":
        print("\n-------- EDITAR CONTATO --------")

        nome_pesquisa = input(
            "Digite o nome do contato que deseja editar: "
        )

        encontrado = False

        for contato in contatos:

            if contato["nome"].lower() == nome_pesquisa.lower():

                print("----------------------")
                print("Contato encontrado!")
                print("O que deseja editar?")
                print("1 - Nome")
                print("2 - Telefone")
                print("3 - Email")

                opcao_editar = input("Escolha uma opção: ")

                if opcao_editar == "1":
                    novo_nome = input("Digite o novo nome: ")

                    contato["nome"] = novo_nome

                    print("Nome atualizado com sucesso!")

                elif opcao_editar == "2":
                    novo_telefone = input("Digite o novo telefone: ")

                    contato["telefone"] = novo_telefone

                    print("Telefone atualizado com sucesso!")

                elif opcao_editar == "3":
                    novo_email = input("Digite o novo email: ")

                    contato["email"] = novo_email

                    print("Email atualizado com sucesso!")

                else:
                    print("Opção inválida.")

                encontrado = True
                break

        if encontrado == False:
            print("Contato não encontrado.")

    
    elif opcao == "5":
        print("\n-------- EXCLUIR CONTATO --------")

        nome_pesquisa = input(
            "Digite o nome do contato que deseja excluir: "
        )

        encontrado = False

        for contato in contatos:

            if contato["nome"].lower() == nome_pesquisa.lower():

                contatos.remove(contato)

                print("Contato excluído com sucesso!")

                encontrado = True
                break

        if encontrado == False:
            print("Contato não encontrado.")

    
    elif opcao == "0":
        print("Saindo do programa...")
        break

    
    else:
        print("Opção inválida!")

