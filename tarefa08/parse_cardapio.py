from xml.dom.minidom import parse
import os

def carregar_cardapio():
    try:
        dom = parse("cardapio.xml") 
        cardapio = dom.documentElement
        pratos = cardapio.getElementsByTagName('prato')
        return pratos
    except FileNotFoundError:
        print("Erro: O arquivo 'cardapio.xml' não foi encontrado.")
        return []

def exibir_menu(pratos):
    print("=== MENU ===")
    for prato in pratos:
        id_prato = prato.getAttribute('id')
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
        print(f"{id_prato} - {nome}")

def mostrar_detalhes(pratos, id_escolhido):
    for prato in pratos:
        if prato.getAttribute('id') == id_escolhido:
            nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
            descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
            preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
            calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
            tempodepreparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
            
            # Tratamento para lista de ingredientes
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print("Ingredientes:")
            ingredientes = prato.getElementsByTagName('ingrediente')
            for ing in ingredientes:
                print(f"    {ing.firstChild.nodeValue}")
            
            print(f"Preço: R${preco}")
            print(f"Calorias: {calorias}kcal")
            print(f"Tempo de preparo: {tempodepreparo}")
            return
    
    print("ID não encontrado no cardápio.")

def main():
    lista_pratos = carregar_cardapio()
    
    if lista_pratos:
        exibir_menu(lista_pratos)
        escolha = input("Digite o id do prato para saber mais: ")
        mostrar_detalhes(lista_pratos, escolha)

if __name__ == "__main__":
    main()