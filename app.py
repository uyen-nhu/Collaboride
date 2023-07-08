import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, use_pages=True)

header = dbc.Container(
    html.Img(src=app.get_asset_url("img/Freudenberg_Logo.png"), height="30px"),
    className="text-center"
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(
            page['name'], href=page["relative_path"]
        ))
        for page in dash.page_registry.values()
        # dbc.NavItem(dbc.NavLink("Home", href="#")),
        # dbc.NavItem(dbc.NavLink("Find a Rider", href="#")),
        # dbc.NavItem(dbc.NavLink("Track", href="#")),
    ],
    brand=html.Img(src=app.get_asset_url("img/Freudenberg_Logo.png"), height="30px"),
    brand_href="#",
    color="light",
    dark=False,
)

app.layout = dbc.Container([header, navbar, dash.page_container])

if __name__ == '__main__':
    app.run_server()