import json
import xml.etree.ElementTree as ET
import os

base_dir = os.path.dirname(__file__)

# Lê da tarefa01
xml_path = os.path.join(base_dir, "..", "tarefa01", "cardapio.xml")

tree = ET.parse(xml_path)
root = tree.getroot()

cardapio = []

for prato in root.findall("prato"):
    p = {
        "id": prato.get("id"),
        "nome": prato.find("nome").text.strip(),
        "descricao": prato.find("descricao").text.strip(),
        "ingredientes": [],
        "precos": [],
        "calorias": prato.find("calorias").text,
        "tempoPreparo": prato.find("tempoPreparo").text
    }

    # Ingredientes
    for ing in prato.find("ingredientes").findall("ingrediente"):
        p["ingredientes"].append(ing.text.strip())

    # Preços
    for preco in prato.findall("preco"):
        valor = preco.text.replace("&reais;", "").strip()
        p["precos"].append({
            "moeda": preco.get("moeda"),
            "valor": valor
        })

    cardapio.append(p)

resultado = {"cardapio": cardapio}

# Salva em tarefa07
json_path = os.path.join(base_dir, "cardapio.json")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(resultado, f, indent=4, ensure_ascii=False)

print("JSON gerado com sucesso!")