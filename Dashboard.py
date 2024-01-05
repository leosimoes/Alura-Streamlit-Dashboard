import streamlit as st
import pandas as pd

st.set_page_config(page_title='Dashboard', page_icon='📊', layout='wide')
st.title("DASHBOARD DE VENDAS :shopping_trolley:")

df = pd.read_csv('Dados/dados.csv')

##############################################################################################
# Barra Lateral do Dashboard

st.sidebar.title("Filtros")

regioes = ['Todas'] + df['Região'].unique().tolist()
filtro_regiao = st.sidebar.selectbox('Regiões', regioes)

vendedores = ['Todos'] + df['Vendedor'].unique().tolist()
filtro_vendedor = st.sidebar.selectbox('Vendedores', vendedores)


def filtrar(df, coluna, valor):
    if valor in ('Todos', 'Todas'):
        return df
    return df[df[coluna] == valor]


df = filtrar(df, coluna='Região', valor=filtro_regiao)
df = filtrar(df, coluna='Vendedor', valor=filtro_vendedor)


##############################################################################################
# Tela do Dashboard

col1, col2 = st.columns(2)

with col1:
    receita = df['Preço'].sum().round(2)
    receita = f'R$ {receita}'.replace('.', ',')
    st.metric('Receita', receita)

with col2:
    quantidade_venda = df.shape[0]
    st.metric('Quantidade de venda', quantidade_venda)

st.divider()

col3, col4 = st.columns(2)

with col3:
    df_receita_categoria = df.groupby(['Categoria do Produto'], as_index=False)['Preço'].sum()
    st.bar_chart(data=df_receita_categoria, y='Preço', x='Categoria do Produto')

with col4:
    df_receita_mensal = df.groupby(['Mês', 'Ano'], as_index=False)['Preço'].sum()
    df_receita_mensal['Ano'] = df_receita_mensal['Ano'].astype(str)
    st.line_chart(data=df_receita_mensal, y='Preço', x='Mês', color='Ano')

st.divider()