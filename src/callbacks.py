from dash import Input, Output, html
from app import app

from graficos.graph import (
    ano_text,
    contagem_text,
    grafico_por_mes,
    grafico_por_timeline,
    grafico_pizza,
    mes_text,
)

from layouts.filterbar import filter_bar


# chamada de função para atualizar as rotas
@app.callback(
    Output("filter-bar-container", "children"),
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    Input("url", "pathname"),
)
def update_ui(pathname):
    pages = {
        "/": (filter_bar(), [True, False, False]),
        "/page-2": (html.Div(), [False, True, False]),
        "/page-3": (filter_bar(), [False, False, True]),
    }
    filter_bar_content, active_states = pages.get(
        pathname, (filter_bar(), [False, False, False])
    )

    return [filter_bar_content] + active_states


# chamada de função para atualizar os gráficos
@app.callback(
    [
        Output("grafico-total", "figure"),
        Output("grafico-mes", "figure"),
        Output("grafico-timeline", "figure"),
        Output("entradas-texto", "children"),
        Output("mes-texto", "children"),
        Output("ano-texto", "children"),
        Output("grafico-2", "figure"),
    ],
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_graficos(ano: int, mes: int) -> tuple:
    return (
        grafico_pizza("setor", "entrada", "setor", ano, mes),
        grafico_por_mes(ano, mes),
        grafico_por_timeline(ano),
        contagem_text(ano, mes),
        mes_text(mes),
        ano_text(ano),
        grafico_pizza("data", "entrada", "data", ano, mes),
    )
