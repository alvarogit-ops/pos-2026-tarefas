import users_wrapper as users


opcao_valida = True
while opcao_valida:
    opcao = input("Digite uma opção. 1 - Listar Usuário \n 2-Criar usuário \n 3- Atualizar usuário \n 4-Deletar Usuário \n 5 - Sair")

    if opcao == "1":
         user_id = input("Digite o ID do usuário")
         dados_do_usuario = users.read(user_id)

         print(dados_do_usuario)

    elif opcao == "2":
         novo_usuario = {
              "name": input("Name: "),
              "username": input("Username: ")    
         }

         novo_usuario = users.create(novo_usuario)
         
    
    elif opcao == "3":
         user_id = input("Digite o ID do usuário")

         dados_do_usuario = {
              "name": input("Nome: "),
              "username": input("Username")
         }

         dados_do_usuario = users.update(user_id, dados_do_usuario)

         print(dados_do_usuario)
         
    
    elif opcao == "4":
          user_id = input("Digite o ID do usuário")

          dados_do_usuario = users.delete(user_id)
         
    else:
         print("fim")
         opcao_valida = False
               

