import streamlit as st
from page1 import pagina_visao_geral
from page2 import pagina_visao_especifica
from page3 import mapa_mundi


def main():
    st.sidebar.title('Análise quadro de medalhas das Olimpíadas')
    page = st.sidebar.radio('---', ['Visão Geral', 'Visão País', 'Mapa Mundi'])

    if page == 'Visão Geral':
        pagina_visao_geral()
    elif page == 'Visão País':
        pagina_visao_especifica()
    elif page == 'Mapa Mundi':
        mapa_mundi()


if __name__ == '__main__':
    main()
