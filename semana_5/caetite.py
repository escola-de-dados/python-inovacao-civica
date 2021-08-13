import datetime
import json
import re
import requests
from bs4 import BeautifulSoup

start_page = requests.get("http://www.procedebahia.com.br/ba/caetite/edicoes")
soup = BeautifulSoup(start_page.content, "html.parser")
editions = soup.find(id="edicoes").find_all("ul")

outputs = []
for edition in editions[1:]:
    link = edition.find_all("li")[1].find("a")["href"]
    title = edition.find_all("li")[1].text
    edition_number = re.search(r"Edição Nº. (\d+)", title).group(1)
    date_text = edition.find_all("li")[0].find("a").text.strip()
    date = datetime.datetime.strptime(date_text, "%d/%m/%Y").date()
    item = {
        "date": str(date),
        "edition_number": edition_number,
        "file_urls": [link],
        "power": "executive",
    }
    outputs.append(item)

with open("output.json", "w") as jsonfile:
    json.dump(outputs, jsonfile)
