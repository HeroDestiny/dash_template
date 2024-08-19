import calendar
import locale

import pandas as pd
import plotly.express as px

locale.setlocale(locale.LC_TIME, "pt_BR")

from connection import fetch_data_from_mysql

df = fetch_data_from_mysql()

df["entrada"] = pd.to_datetime(df["entrada"])

df["data"] = df["entrada"].dt.to_period("M").astype(str)

meses = {calendar.month_name[i].lower(): i for i in range(1, 13)}

print(df)


def filtrar(df: pd.DataFrame, ano: int = None, mes: int = None) -> pd.DataFrame:

    if ano:
        df = df[df["entrada"].dt.year == ano]
    if mes:
        mes_numero = meses[mes.lower()]
        df = df[df["entrada"].dt.month == mes_numero]
    return df


def grafico_pizza(
    nome: str, valor: str, groupby: str, ano: int = None, mes: int = None
) -> px.pie:

    df_filtrado = filtrar(df, ano, mes)

    contagem = df_filtrado.groupby(groupby).count().reset_index()

    return px.pie(contagem, names=nome, values=valor)


def grafico_por_mes(ano: int = None, mes: int = None) -> px.bar:

    df_filtrado = filtrar(df, ano, mes)

    contagem_mes = df_filtrado.groupby("data").size().reset_index(name="contagem")

    contagem_mes["data"] = pd.to_datetime(contagem_mes["data"]).dt.strftime("%b %Y")

    return px.bar(contagem_mes, x="data", y="contagem", color="data")


def grafico_por_timeline(ano: int = None) -> px.line:
    # Filtrar o DataFrame com base no ano e mês fornecidos
    df_filtrado = filtrar(df, ano)

    # Agrupar os dados filtrados por setor e data e contar o número de entradas
    contagem_setor = df_filtrado.groupby(["setor", "data"]).count().reset_index()

    return px.line(
        contagem_setor,
        x="data",
        y="entrada",
        color="setor",
        line_shape="spline",
        labels={
            "setor": "País",
            "entrada": "Número de Entradas",
            "data": "Data da Entrada",
        },
    )


def contagem_text(ano: int = None, mes: int = None) -> str:
    df_filtrado = filtrar(df, ano, mes)
    total_entradas = df_filtrado.shape[0]
    return f"Total de Entradas: {total_entradas}"


def mes_text(mes: int = None) -> str:
    if mes is None:
        return "Mês: Todos"
    else:
        return f"Mês: {mes}"


def ano_text(ano: int = None) -> str:
    if ano is None:
        return "Ano: Todos"
    else:
        return f"Ano: {ano}"


def data_table(ano: int = None, mes: int = None) -> pd.DataFrame:
    df_filtrado = filtrar(df, ano, mes)
    return df_filtrado[["nome", "entrada", "saida", "setor"]]
