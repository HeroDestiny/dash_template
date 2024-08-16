import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from layouts.filterbar import filter_bar
from layouts.navbar import navbar

# Inicializando o aplicativo Dash com o tema Bootstrap
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SANDSTONE],
    use_pages=True,
    suppress_callback_exceptions=True,
)

# Layout principal que inclui a barra de navegação e o conteúdo das páginas
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        navbar(),
        html.Div(id="filter-bar-container"),
        dash.page_container,
    ],
    style={"padding": "5px"},
)


@app.callback(
    Output("filter-bar-container", "children"),
    Output("page-1-link", "active"),
    Output("page-2-link", "active"),
    Output("page-3-link", "active"),
    Input("url", "pathname"),
)
def update_ui(pathname):
    # Configura a visibilidade da barra de filtros com base na URL
    if pathname == "/page-2":
        filter_bar_content = html.Div()  # Ocultar a barra de filtros em "/page-2"
    else:
        filter_bar_content = (
            filter_bar()
        )  # Mostrar a barra de filtros nas outras páginas

    # Atualiza o estado ativo dos links
    return (
        filter_bar_content,
        pathname == "/",
        pathname == "/page-2",
        pathname == "/page-3",
    )


# Executando o aplicativo
if __name__ == "__main__":
    app.run_server(debug=True)
