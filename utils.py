import pandas as pd

# carregar dados
caminho_dados = 'Summer_olympic_Medals.csv'
df_dados = pd.read_csv(caminho_dados)


# função para contar as medalhas
def contar_medalhas(df, agrupar_por_coluna):
    return (
        df.groupby([agrupar_por_coluna])[['Gold', 'Silver', 'Bronze']]
        .sum()
        .reset_index()
    )
