import calendar
import locale

import pandas as pd
import geopandas as gpd
import plotly.express as px

locale.setlocale(locale.LC_TIME, "pt_BR.UTF-8")

from connection import fetch_data_from_mysql



class Grafico:
    def __init__(self):
        self.df = fetch_data_from_mysql()
        self.df["entrada"] = pd.to_datetime(self.df["entrada"])
        self.df["data"] = self.df["entrada"].dt.to_period("M").astype(str)
        self.meses = {calendar.month_name[i].lower(): i for i in range(1, 13)}


    def filtrar(self, ano: int = None, mes: int = None) -> pd.DataFrame:
        df = self.df
        if ano:
            df = df[df["entrada"].dt.year == ano]

        if mes:
            mes_numero = self.meses[mes.lower()]
            df = df[df["entrada"].dt.month == mes_numero]
        return df

    def contar(self, df: pd.DataFrame, group: str, nome: str) -> pd.DataFrame:
        return df.groupby(group).size().reset_index(name=nome)

    def pizza(
        self, nome: str, valor: str, label_nome: str, ano: int = None, mes: int = None
    ) -> px.pie:
        df_filtrado = self.filtrar(ano, mes)
        contagem = self.contar(df_filtrado, nome, valor)
        return px.pie(contagem, names=nome, values=valor, labels={nome: label_nome})

    def barra(
        self,
        nome: str,
        valor: str,
        group: str,
        rotulos: dict,
        ano: int = None,
        mes: int = None,
        cor: str = None,
    ) -> px.bar:
        df_filtrado = self.filtrar(ano, mes)
        contagem = self.contar(df_filtrado, group, valor)
        contagem[nome] = pd.to_datetime(contagem[nome]).dt.strftime("%b %Y")

        if cor is None:
            cor = nome
        else:
            cor = cor

        return px.bar(
            contagem,
            x=nome,
            y=valor,
            color=cor,
            labels=rotulos,
        )

    def timeline(
        self,
        nome: str,
        valor: str,
        group: str,
        rotulos: dict,
        cor: str,
        ano: int = None,
    ) -> px.line:
        df_filtrado = self.filtrar(ano)

        contagem = self.contar(df_filtrado, group, valor)
        contagem[nome] = pd.to_datetime(contagem[nome]).dt.strftime("%m/%Y")

        return px.line(
            contagem,
            x=nome,
            y=valor,
            color=cor,
            labels=rotulos,
            line_shape="spline",
        )

    def mapa( self, nome: str, valor: str, group: str, rotulos: dict, ano: int = None, mes: int = None,
    ) -> px.scatter_geo:
        
        df_filtrado = self.filtrar(ano, mes)
        contagem = self.contar(df_filtrado, group, valor)
        return px.scatter_geo(
            contagem,
            locations=nome,
            locationmode="ISO-3",
            color=nome,
            size=valor,
            labels=rotulos,
            scope="south america",
        )

    def contagem(self, texto: str, ano: int = None, mes: int = None) -> str:
        df_filtrado = self.filtrar(ano, mes)
        total = df_filtrado.shape[0]
        return f"{texto} {total}"

    def texto(self, texto: str, valor: int = None) -> str:
        if valor is None:
            return f"{texto} Todos"
        else:
            return f"{texto} {valor}"

    def data_table(self, ano: int = None, mes: int = None) -> pd.DataFrame:
        df_filtrado = self.filtrar(ano, mes)
        return df_filtrado[["nome", "entrada", "saida", "setor"]]
