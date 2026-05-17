import requests

API_URL = "https://jsonplaceholder.typicode.com/users/"
def read(user_id):
    request = requests.get(f"{API_URL}{user_id}")
    dados_recebidos = request.json()
    print(dados_recebidos)

    if request.status_code == 200:
        print('Sucesso!')    
    else:
        print("deu ruim :/")

def create(novo_usuario):

    request = requests.post(API_URL, json=novo_usuario)

    if request.status_code == 201:
        print("deu certo criar o usuário :)")
    else:
        print("deu ruim criar o usuário:/")


def update(user_id, dados_atualizados):
    request = requests.put(f"{API_URL}{user_id}", json=dados_atualizados)

    if request.status_code == 200:
        print("Usuário foi atualizado")
    else:
        print("deu ruim ao atualizar :/")

def delete(user_id):

    request = requests.delete(f"{API_URL}{user_id}")

    if request.status_code == 200:
        print("Usuário deletado")
    else:
        print("deu ruim ao deletar :/")

