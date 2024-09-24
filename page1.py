import plotly.express as px
import streamlit as st
from utils import contar_medalhas, df_dados


def pagina_visao_geral():
    st.subheader(
        'Quadro geral de medalhas por ano (Escolha o intervalo de tempo)'
    )
    filtro_ano = st.slider(
        label='Escolha o intervalo entre os anos',
        min_value=int(df_dados['Year'].min()),
        max_value=int(df_dados['Year'].max()),
        value=(
            int(df_dados['Year'].min()),
            int(df_dados['Year'].max()),
        ),  # Define um valor padrão como um intervalo
        step=4,
    )
    df_filtro_ano = df_dados[
        (df_dados['Year'] >= filtro_ano[0])
        & (df_dados['Year'] <= filtro_ano[1])
    ]
    total_medalhas = contar_medalhas(df_filtro_ano, 'Country_Name')
    total_medalhas['Total'] = (
        total_medalhas['Gold']
        + total_medalhas['Silver']
        + total_medalhas['Bronze']
    )
    top_paises = total_medalhas.sort_values(by='Total', ascending=False).head(
        30
    )
    st.subheader('Top 30 paises com mais medalhas')
    fig = px.bar(
        top_paises,
        x='Total',
        y='Country_Name',
        labels={'Total': 'Total', 'Country_Name': 'País'},
        orientation='h',
        text='Total',
        # title='Top 20 paises com mais medalhas',
        color='Country_Name',
        color_discrete_sequence=px.colors.qualitative.Prism,
    )
    fig.update_layout(showlegend=False, height=800)
    st.plotly_chart(fig)
