import plotly.express as px
import streamlit as st
from utils import contar_medalhas, df_dados


def mapa_mundi():
    st.subheader('Mapa de medalhas')

    # Ordenar os anos do maior para o menor
    anos_ordenados = sorted(df_dados['Year'].unique(), reverse=True)

    ano = st.selectbox(
        label='Selecione o ano',
        options=anos_ordenados,
        index=0,
        key='ano_selecionado',
    )
    dados_ano = df_dados[df_dados['Year'] == ano]

    total_medalhas = contar_medalhas(dados_ano, 'Country_Name')
    total_medalhas['Total'] = total_medalhas['Gold'] + total_medalhas['Silver'] + total_medalhas['Bronze']
    st.subheader(f'Distribuição de medalhas no ano {ano}')

    fig = px.choropleth(
        total_medalhas,
        locations='Country_Name',
        locationmode='country names',
        color='Total',
        hover_name='Country_Name',
        color_continuous_scale=px.colors.sequential.YlOrBr,
    )
    fig.update_layout(height=500)
    st.plotly_chart(fig)

    total_medalhas_ordenadas = total_medalhas.sort_values(by='Total', ascending=False).reset_index(drop=True)
    total_medalhas_ordenadas = total_medalhas_ordenadas.rename({'Country_Name': 'País'}, axis=1)

    st.subheader(f'Medalhas por país no ano {ano}')
    # Criar a coluna de posição
    total_medalhas_ordenadas['Posição'] = total_medalhas_ordenadas.index + 1
    # Colocar a coluna de posição na primeira posição
    total_medalhas_ordenadas = total_medalhas_ordenadas[['Posição', 'País', 'Gold', 'Silver', 'Bronze', 'Total']]
    st.dataframe(total_medalhas_ordenadas, hide_index=True)
