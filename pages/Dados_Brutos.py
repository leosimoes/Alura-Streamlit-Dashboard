import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dados Brutos', page_icon='📃', layout='wide')

df = pd.read_csv('Dados/dados.csv')

##############################################################################################
# Barra Lateral do Dashboard

st.sidebar.title("Filtros")

def filtrar(df, coluna, valor):
    if valor in ('Todos', 'Todas'):
        return df
    return df[df[coluna] == valor]

# Nome do Produto
nomes_produtos = ['Todos'] + df['Produto'].unique().tolist()
filtro_nome = st.sidebar.selectbox('Produto', nomes_produtos)
df = filtrar(df, coluna='Produto', valor=filtro_nome)

# Categoria do Produto
categorias_produto = ['Todas'] + df['Categoria do Produto'].unique().tolist()
filtro_categoria = st.sidebar.selectbox('Categoria do Produto', categorias_produto)
df = filtrar(df, coluna='Categoria do Produto', valor=filtro_categoria)

# Região
regiao = ['Todas'] + df['Região'].unique().tolist()
filtro_regiao = st.sidebar.selectbox('Regiões', regiao)
df = filtrar(df, coluna='Região', valor=filtro_regiao)

# Estado
estado = ['Todos'] + df['Local da compra'].unique().tolist()
filtro_estado = st.sidebar.selectbox('Estado', estado)
df = filtrar(df, coluna='Local da compra', valor=filtro_estado)

# Ano
ano = ['Todos'] + df['Ano'].unique().tolist()
filtro_ano = st.sidebar.selectbox('Ano', ano)
df = filtrar(df, coluna='Ano', valor=filtro_ano)

# Mês
mes = ['Todos'] + df['Mês'].unique().tolist()
filtro_mes = st.sidebar.selectbox('Mês', mes)
df = filtrar(df, coluna='Mês', valor=filtro_mes)

# Vendedores
vendedores = ['Todos'] + df['Vendedor'].unique().tolist()
filtro_vendedor = st.sidebar.selectbox('Vendedores', vendedores)
df = filtrar(df, coluna='Vendedor', valor=filtro_vendedor)

# Avaliacao
avaliacao = ['Todas'] + df['Avaliação da compra'].unique().tolist()
filtro_avaliacao = st.sidebar.selectbox('Avaliação', avaliacao)
df = filtrar(df, coluna='Avaliação da compra', valor=filtro_avaliacao)

# Tipo pagamento
pagamento = ['Todos'] + df['Tipo de pagamento'].unique().tolist()
filtro_pagamento = st.sidebar.selectbox('Forma de pagamento', pagamento)
df = filtrar(df, coluna='Tipo de pagamento', valor=filtro_pagamento)

# Parcelas
parcelas = ['Todas'] + df['Quantidade de parcelas'].unique().tolist()
filtro_parcela = st.sidebar.selectbox('Parcelas', parcelas)
df = filtrar(df, coluna='Quantidade de parcelas', valor=filtro_parcela)

##############################################################################################
# Tela Principal

st.title("DADOS BRUTOS")

resultado = f'Resultado: {df.shape[0]} linhas.'
st.write(resultado)

st.dataframe(df)