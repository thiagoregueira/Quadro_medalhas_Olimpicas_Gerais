import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils import contar_medalhas, df_dados


def pagina_visao_especifica():
    st.subheader('Analise específica País')

    # Lista de países únicos
    paises = df_dados['Country_Name'].unique()

    # Encontrar o índice do país "Brazil"
    indice_brazil = paises.tolist().index('Brazil')

    pais = st.selectbox(
        label='Selecione o país',
        options=df_dados['Country_Name'].unique(),
        index=indice_brazil,
    )
    dados_pais = df_dados[df_dados['Country_Name'] == pais]

    # Filtrar dados para a última Olimpíada
    ultimo_ano = df_dados['Year'].max()
    dados_ultima_olimpiada = df_dados[df_dados['Year'] == ultimo_ano]
    total_medalhas_ultima_olimpiada = contar_medalhas(dados_ultima_olimpiada, 'Country_Name')
    total_medalhas_ultima_olimpiada['Total'] = (
        total_medalhas_ultima_olimpiada['Gold']
        + total_medalhas_ultima_olimpiada['Silver']
        + total_medalhas_ultima_olimpiada['Bronze']
    )
    total_medalhas_ultima_olimpiada = total_medalhas_ultima_olimpiada.sort_values(
        by='Total', ascending=False
    ).reset_index(drop=True)
    posicao_ultima_olimpiada = (
        total_medalhas_ultima_olimpiada[total_medalhas_ultima_olimpiada['Country_Name'] == pais].index[0] + 1
    )

    # Filtrar dados para a Olimpíada anterior
    ano_anterior = df_dados['Year'].unique()[-2]
    dados_olimpiada_anterior = df_dados[df_dados['Year'] == ano_anterior]
    total_medalhas_olimpiada_anterior = contar_medalhas(dados_olimpiada_anterior, 'Country_Name')
    total_medalhas_olimpiada_anterior['Total'] = (
        total_medalhas_olimpiada_anterior['Gold']
        + total_medalhas_olimpiada_anterior['Silver']
        + total_medalhas_olimpiada_anterior['Bronze']
    )
    total_medalhas_olimpiada_anterior = total_medalhas_olimpiada_anterior.sort_values(
        by='Total', ascending=False
    ).reset_index(drop=True)
    posicao_olimpiada_anterior = (
        total_medalhas_olimpiada_anterior[total_medalhas_olimpiada_anterior['Country_Name'] == pais].index[0] + 1
    )

    # Calcular o delta
    delta_posicao = int(posicao_olimpiada_anterior - posicao_ultima_olimpiada)

    # Exibir o metric card
    st.metric(
        label=f'Posição do(a) {pais} na última Olimpíada ({ultimo_ano})',
        value=posicao_ultima_olimpiada,
        delta=delta_posicao,
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=dados_pais['Year'],
            y=dados_pais['Gold'],
            mode='lines',
            name='Gold',
            line={'color': 'gold', 'width': 2},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dados_pais['Year'],
            y=dados_pais['Silver'],
            mode='lines',
            name='Silver',
            line={'color': 'silver', 'width': 2},
        )
    )
    fig.add_trace(
        go.Scatter(
            x=dados_pais['Year'],
            y=dados_pais['Bronze'],
            mode='lines',
            name='Bronze',
            line={'color': '#cd7f32', 'width': 2},
        )
    )
    fig.update_layout(title=f'Evolução das medalhas do(a) {pais}', height=400)
    st.plotly_chart(fig)

    medalhas_totais = dados_pais[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    medalhas_totais.columns = ['Medalha', 'Total']

    st.subheader(f'Quadro de medalhas do(a) {pais}')

    fig = px.bar(
        medalhas_totais,
        x='Total',
        y='Medalha',
        orientation='h',
        # title=f'Quadro de medalhas do País {pais}',
        color='Medalha',
        color_discrete_map={
            'Gold': 'gold',
            'Silver': 'silver',
            'Bronze': '#cd7f32',
        },
        text='Total',
    )
    fig.update_layout(height=300)
    st.plotly_chart(fig)
