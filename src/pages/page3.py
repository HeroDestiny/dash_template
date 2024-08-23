import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Registra a página
dash.register_page(__name__, path="/page-3")

# Layout da Página 1
layout = html.Div(
    [
        dbc.Row(
            dbc.Col(
                dbc.CardGroup(
                    [
                        # dbc.Card(
                        #     dbc.CardBody(
                        #         [
                        #             html.H4("GRAFICO 1", className="card-title"),
                        #             html.P("LEGENDA 1", className="card-text"),
                        #             dcc.Graph(id="grafico-mapa"),
                        #         ]
                        #     )
                        # ),
                        # dbc.Card(
                        #     dbc.CardBody(
                        #         [
                        #             html.H4("GRAFICO 2", className="card-title"),
                        #             html.P(
                        #                 "LEGENDA 2",
                        #                 className="card-text",
                        #             ),
                        #             dcc.Graph(id="numero-2"),
                        #         ]
                        #     )
                        # ),
                    ]
                ),
                width=6,
            )
        ),
        # dbc.Row(
        #     dbc.Col(
        #         dbc.CardGroup(
        #             [
        #                 dbc.Card(
        #                     dbc.CardBody(
        #                         [
        #                             html.H4("GRAFICO 3", className="card-title"),
        #                             html.P("LEGENDA 3", className="card-text"),
        #                             dcc.Graph(id="numero-3"),
        #                         ]
        #                     )
        #                 ),
        #                 dbc.Card(
        #                     dbc.CardBody(
        #                         [
        #                             html.H4("GRAFICO 4", className="card-title"),
        #                             html.P(
        #                                 "LEGENDA 4",
        #                                 className="card-text",
        #                             ),
        #                             dcc.Graph(id="numero-4"),
        #                         ]
        #                     )
        #                 ),
        #             ]
        #         ),
        #         width=12,
        #     )
        # ),
    ]
)
