import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from graficos.graph import grafico

# Registra a página
dash.register_page(__name__, path="/")

# Layout da Página 1
layout = html.Div(
    [
        html.Div(
            [
                dbc.CardGroup(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Titulo Bacana", className="card-title"),
                                    html.P(
                                        "Cadvis x Ugtsic",
                                        className="card-text",
                                    ),
                                    html.Div(
                                        dcc.Graph(figure=grafico()),
                                        className="col-12",
                                    ),
                                ]
                            )
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Card title", className="card-title"),
                                    html.P(
                                        "This card has supporting text below as a natural lead-in to additional content.",
                                        className="card-text",
                                    ),
                                    html.Div(
                                        dcc.Graph(id="graph-page-2"),
                                        className="col-12",
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ],
            className="row",
        ),
        html.Div(
            [
                dbc.CardGroup(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Card title", className="card-title"),
                                    html.P(
                                        "This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.",
                                        className="card-text",
                                    ),
                                    html.Div(
                                        dcc.Graph(id="grafico2"),
                                        className="col-12",
                                    ),
                                ]
                            )
                        ),
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Card title", className="card-title"),
                                    html.P(
                                        "This card has supporting text below as a natural lead-in to additional content.",
                                        className="card-text",
                                    ),
                                    html.Div(
                                        dcc.Graph(id="graph-page-3"),
                                        className="col-12",
                                    ),
                                ]
                            )
                        ),
                    ]
                )
            ],
            className="row",
        ),
    ]
)
