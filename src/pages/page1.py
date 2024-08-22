import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

dash.register_page(__name__, path="/")


layout = html.Div(
    [
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
                                                className="card-title",
                                                id="entradas-texto",
                                            ),
                                        ]
                                    ),
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                dbc.Card(
                                    dbc.CardBody(
                                        [
                                            html.H4(
                                                id="mes-texto", className="card-title"
                                            ),
                                        ]
                                    ),
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
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
                            width=4,
                        ),
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
                    ]
                ),
            ],
        ),
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
    ]
)
