import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Inicializando o aplicativo Dash com o tema SANDSTONE
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    use_pages=True,
    suppress_callback_exceptions=True,
)
# IMPORTANTE! o callback deve ser importado depois de inicializar o app
from callbacks import *
from layouts.navbar import navbar

# Layout principal que inclui a barra de navegação e o conteúdo das páginas
app.layout = html.Div(
    [
        dcc.Store(id="filtered-data", storage_type="memory"),
        dcc.Location(id="url", refresh=False),
        navbar(),
        html.Div(id="filter-bar-container"),
        dash.page_container,
    ],
    style={"padding": "5px"},
)

# Executando o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
