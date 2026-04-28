import xml.dom.minidom as minidom
import json

def xml_pra_json():
    try:
        dom = minidom.parse("imobiliaria.xml")
        imobiliaria = dom.documentElement
        lista_imoveis = []
        imoveis_obtidos = imobiliaria.getElementsByTagName("imovel")

        for imovel_obtido in imoveis_obtidos:
            def obter_texto(no, tag_nome):
                elementos = no.getElementsByTagName(tag_nome)
                if elementos and elementos[0].firstChild:
                    return elementos[0].firstChild.nodeValue
                return ""
            
            descricao = obter_texto(imovel_obtido, "descricao")

            # Proprietário
            prop_node = imovel_obtido.getElementsByTagName("proprietario")[0]
            nome_proprietario = obter_texto(prop_node, "nome")

            # Endereço
            end_node = imovel_obtido.getElementsByTagName("endereco")[0]
            rua = obter_texto(end_node, "rua")
            bairro = obter_texto(end_node, "bairro")
            cidade = obter_texto(end_node, "cidade")
            endereco_completo = f"{rua}, {bairro}, {cidade}"

            # Valor
            valor = obter_texto(imovel_obtido, "valor")

            dados_imovel = {
                "descrição": descricao,
                "proprietário": nome_proprietario,
                "endereço": endereco_completo,
                "valor": valor,
            }
            
            # --- O PONTO CHAVE: ---
            lista_imoveis.append(dados_imovel) 

        dados_finais = {"imobiliária": {"imóveis": lista_imoveis}}

        with open("imobiliaria.json", "w", encoding="utf-8") as arquivo_json:
            json.dump(dados_finais, arquivo_json, indent=4, ensure_ascii=False)
                
        print("Sucesso! O arquivo 'imobiliaria.json' foi criado com os dados.")

    except FileNotFoundError:
        print("Erro: O arquivo 'imobiliaria.xml' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    xml_pra_json()