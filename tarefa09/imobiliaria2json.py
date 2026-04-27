import xml.dom.minidom as minidom
import json

def xml_pra_json():
    try:
        dom = minidom.parse("imobiliaria.xml")
        imobiliaria = dom.documentElement
        lista_imoveis = []
        imoveis_obtidos = imobiliaria.getElementsbyTagName("imovel")

        for imovel_obtido in imoveis_obtidos:
            dados_imovel = {
                "id": imovel_obtido.getAttribute("id"),
                "tipo": imovel_obtido.getElementsByTagName("tipo")[0].firstChild.nodeValue,
                "endereço": imovel_obtido.getElementsByTagName("endereço")[0].firstChild.nodeValue,
                "valor": imovel_obtido.getElementsByTagName("valor")[0].firstChild.nodeValue,
            } 
            lista_imoveis.append(dados_imovel)

        dados_finais = {"imobiliária": {"imóveis": lista_imoveis}}

        with open("imobiliaria.json", "w", encoding="utf-8") as arquivo_json:
                json.dump(dados_finais, arquivo_json, indent=4, ensure_ascii=False)
                
        print("Sucesso! O arquivo 'imobiliaria.json' foi criado.")

    except FileNotFoundError:
            print("Erro: O arquivo 'imobiliaria.xml' não foi encontrado nesta pasta.")
    except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
if __name__ == "__main__":
    xml_pra_json()