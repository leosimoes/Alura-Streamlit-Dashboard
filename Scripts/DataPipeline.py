import pandas as pd
import requests as rq

URL = 'https://labdados.com/produtos'

response = rq.get(URL)
df = pd.DataFrame.from_dict(response.json())

assert df.isna().sum().sum() == 0
assert df.duplicated().sum() == 0

regioes_por_estado = {
    'Norte': ['AM', 'RR', 'AP', 'PA', 'TO', 'RO', 'AC'],
    'Nordeste': ['MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA'],
    'Centro-Oeste': ['MT', 'MS', 'GO', 'DF'],
    'Sudeste': ['SP', 'RJ', 'MG', 'ES'],
    'Sul': ['PR', 'SC', 'RS']
}

def obter_regiao(estado):
    for regiao, estados in regioes_por_estado.items():
        if estado in estados:
            return regiao
    return 'Desconhecida'

df['Região'] = df['Local da compra'].apply(obter_regiao)
assert 'Região' in df.columns.values
assert df['Região'].nunique() == 5


df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
assert df['Data da Compra'].dtype.str != '|O'

df['Ano'] = df['Data da Compra'].dt.year
assert 'Ano' in df.columns.values

df['Mês'] = df['Data da Compra'].dt.month
assert 'Mês' in df.columns.values

df.to_csv('../Dados/dados.csv', index=False)