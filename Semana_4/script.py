import requests
import pandas as pd
from zipfile import ZipFile

r = requests.get("http://www.camara.leg.br/cotas/Ano-2019.csv.zip")

file = open(f"Ano-2019.csv.zip", "wb")
file.write(r.content)
file.close()

zip_file = ZipFile(f"Ano-2019.csv.zip", 'r')
zip_file.extract(member=f"Ano-2019.csv", path=f"reembolso-2019")
zip_file.close()


DTYPE = {
    'txNomeParlamentar': str,
    'ideCadastro': str,
    'nuCarteiraParlamentar': str,
    'nuLegislatura': str,
    'sgUF': str,
    'sgPartido': str,
    'codLegislatura': str,
    'numSubCota': str,
    'txtDescricao': str,
    'numEspecificacaoSubCota': str,
    'txtDescricaoEspecificacao': str,
    'txtFornecedor': str,
    'txtCNPJCPF': str,
    'txtNumero': str,
    'indTipoDocumento': str,
    'datEmissao': str,
    'vlrDocumento': float,
    'vlrGlosa': str,
    'vlrLiquido': float,
    'numMes': str,
    'numAno': str,
    'numParcela': str,
    'txtPassageiro': str,
    'txtTrecho': str,
    'numLote': str,
    'numRessarcimento': str,
    'nuDeputadoId': str,
    'ideDocumento': str,
}
print("lendo csv reembolso...")
df = pd.read_csv(
    "reembolso-2019/Ano-2019.csv", 
    delimiter=";", 
    dtype=DTYPE, 
    low_memory=False
)

print("converte to_datetime...")
df["datEmissao"] = pd.to_datetime(
    df.datEmissao, 
    format='%Y-%m-%d'
)

converters = {
    "0": 'nota_fiscal',
    "1": 'recibo',
    "2": 'despesa_exterior',
    "4": None
}
df.indTipoDocumento.replace(converters, inplace=True)

df["txtCNPJCPF"] = df["txtCNPJCPF"].str.replace(r'\D', '', regex=True)

DTYPE = {
    'cnpj': str,
}
print("lendo csv empresas...")
df_empresas = pd.read_csv(
    '2019-11-19-companies.csv.xz', 
    compression='xz',
    dtype=DTYPE,  
)
df_empresas['situation_date'] = pd.to_datetime(df_empresas['situation_date'], format="%Y-%m-%d")

df_final = df.merge(
    df_empresas,
    how='left',
    left_on='txtCNPJCPF',
    right_on='cnpj'
)

df_final.to_csv("reembolso-2019-completo.csv")