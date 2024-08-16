import dash_bootstrap_components as dbc


def navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Página 1", href="/", id="page-1-link")),
            dbc.NavItem(dbc.NavLink("Página 2", href="/page-2", id="page-2-link")),
            dbc.NavItem(dbc.NavLink("Página 3", href="/page-3", id="page-3-link")),
        ],
        brand="Meu Aplicativo Dash",
        brand_href="/",
        color="primary",
        dark=True,
        links_left=False,
    )
