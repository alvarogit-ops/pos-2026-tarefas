import users_wrapper as users


opcao_valida = True
while opcao_valida:
    opcao = input("Digite uma opção. 1 - Ler usuário \n 2 - Listar Usuário \n 3-Criar usuário \n 4- Atualizar usuário \n 5-Deletar Usuário \n 6 - Sair \n")

    if opcao == "1":
     user_id = input("Digite o ID do usuário")
     dados_do_usuario = users.read(user_id)
     print(dados_do_usuario)


    if opcao == "2":
     dados_do_usuario = users.list()
     print(dados_do_usuario)

     print(dados_do_usuario)

    elif opcao == "3":
     novo_usuario = {
          "name": input("Name: "),
          "username": input("Username: ")    
     }

     novo_usuario = users.create(novo_usuario)
     print(novo_usuario)
         
    
    elif opcao == "4":
     user_id = input("Digite o ID do usuário que")

     dados_do_usuario = {
          "name": input("Nome: "),
          "username": input("Username")
     }
     print(dados_do_usuario)
     dados_do_usuario = users.update(user_id, dados_do_usuario)

     print(dados_do_usuario)
         
    
    elif opcao == "5":
     user_id = input("Digite o ID do usuário")
     dados_do_usuario = users.delete(user_id)

    elif opcao == "6":
          print("fim")
          opcao_valida = False
               

