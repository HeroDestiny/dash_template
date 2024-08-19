import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from graficos.graph import (
    ano_text,
    contagem_text,
    grafico_por_mes,
    grafico_por_timeline,
    grafico_por_total,
    mes_text,
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
                            width=12,
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
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4("Grafico 2", className="card-title"),
                                        dcc.Graph(id="grafico-2"),
                                    ]
                                )
                            ),
                            width=9,
                        ),
                    ]
                ),
            ],
        ),
    ]
)
