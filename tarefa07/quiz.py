import os
import json
import xml.etree.ElementTree as ET

# Lê o XML da tarefa03
tree = ET.parse("tarefa03/quiz.xml")
root = tree.getroot()

quiz = []

for questao in root.findall("questao"):
    q = {
        "id": questao.get("id"),
        "pergunta": questao.find("pergunta").text,
        "alternativas": []
    }

    for alt in questao.findall("alternativa"):
        alternativa = {
            "letra": alt.get("letra"),
            "correta": True if alt.get("correta") == "sim" else False,
            "texto": alt.text
        }
        q["alternativas"].append(alternativa)

    quiz.append(q)

resultado = {"quiz": quiz}

json_str = json.dumps(resultado, indent=4, ensure_ascii=False)

print(json_str)

# Salva na pasta atual (onde o script roda)
base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, "quiz.json")

with open(json_path, "w", encoding="utf-8") as f:
    f.write(json_str)