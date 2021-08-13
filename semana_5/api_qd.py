import json
import pprint
import requests

territory_id = "2927408"  # Salvador (BA)
keywords = "dispensa de licitação"
start_date = "2021-01-01"
endpoint = f"https://queridodiario.ok.org.br/api/gazettes/{territory_id}?keywords={keywords}&since={start_date}"

response = requests.get(endpoint)
pprint.pprint(json.loads(response.text))
