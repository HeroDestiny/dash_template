import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from graficos.graph import (
    grafico_por_mes,
    grafico_por_timeline,
    grafico_por_total,
    contagem_text,
    mes_text,
    ano_text,
)

dash.register_page(__name__, path="/")


layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dbc.CardGroup(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Entradas x Setor", className="card-title"),
                                    dcc.Graph(id="grafico-total"),
                                ]
                            )
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Entradas x Mês", className="card-title"),
                                    # html.P(
                                    #     "Quantidade de Entradas por Mês",
                                    #     className="card-text",
                                    # ),
                                    dcc.Graph(id="grafico-mes"),
                                ]
                            )
                        ),
                    ]
                ),
                width=12,
            )
        ),
        dbc.Row(
            [
                dbc.CardGroup(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                "Entrada por Setor",
                                                className="card-title",
                                            ),
                                            dcc.Graph(id="grafico-timeline"),
                                        ]
                                    )
                                ),
                            ],
                            width=9,
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                className="card-text",
                                                id="entradas-texto",
                                            ),
                                        ]
                                    ),
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                id="mes-texto", className="card-title"
                                            ),
                                        ]
                                    ),
                                ),
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                id="ano-texto", className="card-title"
                                            ),
                                        ]
                                    ),
                                ),
                            ],
                            width=3,
                        ),
                    ]
                ),
            ],
        ),
    ]
)


@dash.callback(
    [
        Output("grafico-total", "figure"),
        Output("grafico-mes", "figure"),
        Output("grafico-timeline", "figure"),
        Output("entradas-texto", "children"),
        Output("mes-texto", "children"),
        Output("ano-texto", "children"),
    ],
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_graficos(ano: int, mes: int) -> tuple:
    return (
        grafico_por_total(ano, mes),
        grafico_por_mes(ano, mes),
        grafico_por_timeline(ano),
        contagem_text(ano, mes),
        mes_text(mes),
        ano_text(ano),
    )
