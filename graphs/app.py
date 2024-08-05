# app.py

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

# Inicializando o aplicativo Dash com o tema Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE], use_pages=True)

# Layout da barra de navegação
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Página 1", href="/")),
        dbc.NavItem(dbc.NavLink("Página 2", href="/page-2")),
        dbc.NavItem(dbc.NavLink("Página 3", href="/page-3")),
    ],
    brand="Meu Aplicativo Dash",
    brand_href="/",
    color="primary",
    dark=True,
)

# Layout principal que inclui a barra de navegação e o conteúdo das páginas
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), navbar, dash.page_container]
)

# Executando o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
