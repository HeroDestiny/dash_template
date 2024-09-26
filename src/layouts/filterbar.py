import calendar
import locale

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc

from connection import fetch_data_from_mysql

locale.setlocale(locale.LC_TIME, "pt_BR")

df = fetch_data_from_mysql()

df["entrada"] = pd.to_datetime(df["entrada"])
df = df.dropna(subset=["entrada"])

meses_cronologicos = [calendar.month_name[i] for i in range(1, 13)]


def filter_bar():
    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Label("Selecione o ano:"),
                    dcc.Dropdown(
                        id="ano-dropdown",
                        options=[
                            {"label": str(ano), "value": ano}
                            for ano in df["entrada"].dt.year.unique()
                        ],
                        placeholder="Selecione o ano",
                        className="mb-3",
                    ),
                ],
                width=2,
            ),
            dbc.Col(
                [
                    dbc.Label("Selecione o mês:"),
                    dcc.Dropdown(
                        id="mes-dropdown",
                        options=[
                            {"label": str(mes), "value": mes}
                            for mes in meses_cronologicos
                        ],
                        placeholder="Selecione o mês",
                        className="mb-3",
                    ),
                ],
                width=2,
            ),
            dbc.Col(
                [
                    dbc.Label("Selecione o Setor:"),
                    dcc.Dropdown(
                        id="setor-dropdown",
                        options=[
                            {"label": str(setor), "value": setor}
                            for setor in df["setor"].unique()
                        ],
                        placeholder="Selecione o setor",
                        className="mb-3",
                    ),
                ],
                width=2,
            ),
        ],
    )
