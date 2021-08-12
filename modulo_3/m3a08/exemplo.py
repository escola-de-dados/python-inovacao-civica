import re

texto = "Querido Diário, hoje eu..."

diario = re.search(r"[dD]iário", texto)
print(diario.group())

reticencias = re.search(r"\.{3}", texto)
print(reticencias.group())
print(reticencias)

pontos = re.findall(r"\.", texto)
print(pontos)
