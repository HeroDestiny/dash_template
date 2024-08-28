from dash import Input, Output, html

from app import app
from graficos.graph import Grafico
from layouts.filterbar import filter_bar

grafico = Grafico()


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
    ],
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_graficos(ano: int, mes: int) -> tuple:
    return (
        grafico.pizza("setor", "entrada", "País", ano, mes),
        # grafico_barra("data", "entrada", "Data", "Entradas", "data", ano, mes),
        grafico.barra(
            "data", "entrada", "data", {"data": "Data", "entrada": "Entradas"}, ano, mes
        ),
        grafico.timeline(
            "data",
            "entrada",
            ["setor", "data"],
            {"setor": "País", "data": "Data", "entrada": "Número de Entradas"},
            "setor",
            ano,
        ),
        grafico.contagem("Total de Entradas:", ano, mes),
        grafico.texto("Mês:", mes),
        grafico.texto("Ano:", ano),
    )


@app.callback(
    Output("grafico-mapa", "figure"),
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_mapa(ano: int, mes: int) -> tuple:
    return grafico.mapa(
        "setor", "entrada", "setor", {"setor": "Municipio", "entrada": "Visitas"}, ano, mes
    )
