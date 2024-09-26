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


@app.callback(
    [
        Output("entradas-texto", "children"),
        Output("mes-texto", "children"),
        Output("ano-texto", "children"),
    ],
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_texto_entradas(ano: int, mes: int) -> tuple:
    return (
        grafico.contagem("Total de Entradas:", ano, mes),
        grafico.texto("Mês:", mes),
        grafico.texto("Ano:", ano),
    )


@app.callback(
    Output("grafico-timeline", "figure"),
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_grafico_timeline(ano: int, mes: int) -> tuple:
    return grafico.timeline(
        "data",
        "entrada",
        ["setor", "data"],
        {"setor": "País", "data": "Data", "entrada": "Número de Entradas"},
        "setor",
        ano,
    )


@app.callback(
    Output("grafico-mes", "figure"),
    [Input("ano-dropdown", "value"), Input("mes-dropdown", "value")],
)
def update_grafico_mes(ano: int, mes: int) -> tuple:
    return grafico.barra(
        "data", "entrada", "data", {"data": "Data", "entrada": "Entradas"}, ano, mes
    )


@app.callback(
    Output("grafico-total", "figure"),
    [
        Input("ano-dropdown", "value"),
        Input("mes-dropdown", "value"),
        Input("setor-dropdown", "value"),
    ],
)
def update_grafico_total(ano: int, mes: int, setor: str) -> tuple:
    return grafico.pizza("setor", "entrada", "País", ano, mes, setor)


@app.callback(
    Output("grafico-mapa", "figure"),
    [
        Input("ano-dropdown", "value"),
        Input("mes-dropdown", "value"),
        Input("setor-dropdown", "value"),
    ],
)
def update_mapa(ano: int, mes: int, setor: str) -> tuple:
    return grafico.mapa(
        "setor",
        "entrada",
        "setor",
        {"setor": "Municipio", "entrada": "Visitas"},
        ano,
        mes,
        setor,
    )
