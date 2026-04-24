import json
import xml.etree.ElementTree as ET
import os

base_dir = os.path.dirname(__file__)

# Lê da tarefa02
xml_path = os.path.join(base_dir, "..", "tarefa02", "imobiliaria.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

imoveis = []

for imovel in root.findall("imovel"):
    # Proprietário
    prop = imovel.find("proprietario")
    contatos = {
        "telefones": [],
        "emails": []
    }

    for tel in prop.findall("telefone"):
        contatos["telefones"].append(tel.text.strip())

    for email in prop.findall("email"):
        contatos["emails"].append(email.text.strip())

    proprietario = {
        "nome": prop.find("nome").text.strip(),
        "contatos": contatos
    }

    # Endereço
    end = imovel.find("endereco")
    endereco = {
        "rua": end.find("rua").text.strip(),
        "bairro": end.find("bairro").text.strip(),
        "cidade": end.find("cidade").text.strip(),
        "numero": end.find("numero").text.strip() if end.find("numero") is not None else None
    }

    # Características
    carac = imovel.find("caracteristicas")
    caracteristicas = {
        "tamanho": carac.find("tamanho").text,
        "quartos": carac.find("numQuartos").text,
        "banheiros": carac.find("numBanheiros").text
    }

    # Monta objeto final
    imoveis.append({
        "descricao": imovel.find("descricao").text.strip(),
        "proprietario": proprietario,
        "endereco": endereco,
        "caracteristicas": caracteristicas,
        "valor": imovel.find("valor").text
    })

resultado = {"imobiliaria": imoveis}

# Salva em tarefa07
json_path = os.path.join(base_dir, "imobiliaria.json")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)

print("JSON gerado com sucesso!")