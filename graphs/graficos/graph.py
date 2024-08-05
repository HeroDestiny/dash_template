import plotly.express as px

from connection import fetch_data_from_mysql

df = fetch_data_from_mysql()


def grafico():
    contagem = df.groupby("setor").count().reset_index()

    return px.bar(
        contagem, x="setor", y="entrada"
    )
