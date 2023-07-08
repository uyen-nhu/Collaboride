import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/')

map_cluster = html.Div(
    dbc.Container(
        [
            html.H1("[MAP]")
        ],
        fluid=True,
        className="py-3",
    ),
    id="map",
    className="my-4 p-5 bg-secondary rounded-3 text-center"
)

table_header = [
    html.Thead(html.Tr([html.Th("#"), html.Th("Name")]))
]

row1 = html.Tr([html.Td("1"), html.Td("Bob")])
row2 = html.Tr([html.Td("2"), html.Td("Ann")])
row3 = html.Tr([html.Td("3"), html.Td("John")])

table_body = [html.Tbody([row1, row2, row3])]

leaderboard_table = html.Div(
    [
        dbc.Label("Leaderboard:", html_for="leaderboard"),
        dbc.Table(
            table_header + table_body, bordered=True,
            id="leaderboard"
        )
    ],
    className="my-4"
)

layout = dbc.Container([map_cluster, leaderboard_table], fluid=False)