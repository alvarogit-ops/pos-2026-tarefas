import json
import os

def carregar_imoveis():
    """Carrega os dados do arquivo imobiliaria.json"""
    try:
        with open("imobiliaria.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            # Retorna a lista de imóveis
            return dados["imobiliária"]["imóveis"]
    except FileNotFoundError:
        print("Erro: O arquivo 'imobiliaria.json' não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar o arquivo JSON.")
        return []

def exibir_menu(imoveis):
    """Exibe a lista simplificada com um índice (ID)"""
    print("\n=== IMOBILIÁRIA - LISTA DE IMÓVEIS ===")
    print(f"{'ID':<5} | {'DESCRIÇÃO'}")
    print("-" * 40)
    for indice, imovel in enumerate(imoveis):
        # Usamos o índice da lista como ID (começando em 1 para facilitar ao usuário)
        print(f"{indice + 1:<5} | {imovel['descrição']}")

def mostrar_detalhes(imoveis, id_escolhido):
    """Mostra todos os detalhes do imóvel selecionado pelo ID"""
    try:
        # Converte a entrada para inteiro e ajusta para índice da lista (0-based)
        index = int(id_escolhido) - 1
        
        if 0 <= index < len(imoveis):
            imovel = imoveis[index]
            print("\n" + "="*40)
            print("DETALHES DO IMÓVEL")
            print("="*40)
            print(f"Descrição:    {imovel['descrição']}")
            print(f"Proprietário: {imovel['proprietário']}")
            print(f"Endereço:     {imovel['endereço']}")
            print(f"Valor:        R$ {imovel['valor']}")
            print("="*40)
        else:
            print("\nID inválido! Por favor, escolha um número da lista.")
    except ValueError:
        print("\nErro: Digite um número válido para o ID.")

def main():
    lista_imoveis = carregar_imoveis()
    
    if lista_imoveis:
        while True:
            exibir_menu(lista_imoveis)
            print("\nOpções: Digite o ID para detalhes ou 'sair' para encerrar.")
            escolha = input("Sua escolha: ").strip().lower()
            
            if escolha == 'sair':
                print("Encerrando o sistema...")
                break
            
            mostrar_detalhes(lista_imoveis, escolha)
            
            # Pausa para o usuário ler antes de limpar/repetir o menu
            input("\nPressione Enter para continuar...")
            # Limpa o console (opcional, dependendo do SO)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()