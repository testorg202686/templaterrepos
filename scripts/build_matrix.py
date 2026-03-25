import csv
import json
import re

def normalize(name):
    name = name.lower().replace(" ", "-")
    return re.sub(r"[^a-z0-9-]", "", name)

rows = []

with open("repos.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for r in reader:
        tipo = (r.get("type") or "").strip()

        if tipo in ["source", "documentation"]:
            types = [tipo]
        elif tipo in ["source+documentation", "documentation+source"]:
            types = ["source", "documentation"]
        else:
            raise Exception(f"Tipo inválido: {tipo}")

        for t in types:
            name = normalize(r["name"])
            mxapm = (r.get("mxapm") or "").strip()
            desc = (r.get("description") or "").strip()

            if t == "source":
                template = (r.get("template_source") or "").strip()
                final_name = f"{mxapm}-source-{name}"
            else:
                template = (r.get("template_docs") or "").strip()
                final_name = f"{mxapm}-documentation-{name}"

            if not template:
                raise Exception(f"Template faltante para tipo '{t}' en {name}")

            rows.append({
                "name": final_name,
                "description": desc,
                "template": template
            })

print(json.dumps(rows))
