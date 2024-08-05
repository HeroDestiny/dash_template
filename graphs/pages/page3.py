import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output

# Registra a página
dash.register_page(__name__, path="/page-3")

# Layout da Página 1
layout = html.Div(
    [
        html.H1("Página 3", className="text-center my-4"),
        html.Div(
            [
                html.Div(
                    dcc.Graph(id="graph-page-1"),
                    className="col-6",
                ),
            ],
            className="row",
        ),
        html.Div(
            [
                html.Div(
                    dcc.Graph(id="graph-page-1"),
                    className="col-6",
                ),
            ],
            className="row",
        ),
    ]
)
