import dash
import dash_bootstrap_components as dbc
from dash import dash_table, html

from graficos.graph import Grafico

# Registra a página
dash.register_page(__name__, path="/page-2")

grafico = Grafico()
# Layout da Página 1
layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Tabela de Visitantes"),
                        dash_table.DataTable(
                            id="table",
                            columns=[
                                {"name": i, "id": i}
                                for i in grafico.data_table().columns
                            ],
                            data=grafico.data_table().to_dict("records"),
                            filter_action="native",  # Adiciona filtros nativos à tabela
                            style_table={
                                "overflowX": "auto",  # Adiciona rolagem horizontal se necessário
                                "maxHeight": "400px",  # Define a altura máxima da tabela
                                "border": "1px solid #ddd",  # Borda ao redor da tabela
                            },
                            style_header={
                                "backgroundColor": "#f5f5f5",  # Cor de fundo dos cabeçalhos
                                "fontWeight": "bold",  # Negrito no texto do cabeçalho
                                "textAlign": "center",  # Alinhamento do texto no cabeçalho
                                "border": "1px solid #ddd",  # Borda inferior dos cabeçalhos
                            },
                            style_data={
                                "backgroundColor": "white",  # Cor de fundo das células
                                "color": "black",  # Cor do texto nas células
                                "fontSize": "14px",  # Tamanho da fonte nas células
                                "textAlign": "center",  # Alinhamento do texto nas células
                                "border": "1px solid #ddd",  # Borda das células
                            },
                            style_data_conditional=[
                                {
                                    "if": {
                                        "row_index": "odd"
                                    },  # Estilo para linhas ímpares
                                    "backgroundColor": "#f9f9f9",  # Cor de fundo para linhas ímpares
                                },
                                {
                                    "if": {
                                        "row_index": "even"
                                    },  # Estilo para linhas pares
                                    "backgroundColor": "#ffffff",  # Cor de fundo para linhas pares
                                },
                                {
                                    "if": {
                                        "state": "selected"
                                    },  # Estilo para linhas selecionadas
                                    "backgroundColor": "#d3d3d3",  # Cor de fundo quando a linha é selecionada
                                    "border": "1px solid #b3b3b3",  # Borda ao redor da linha selecionada
                                },
                            ],
                            page_size=10,  # Define o número de linhas por página
                        ),
                    ],
                    width=12,
                ),
            ],
        ),
    ]
)
