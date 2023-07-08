import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from app import user_data


dash.register_page(__name__, path='/')

map_cluster = html.Div(
    dbc.Container(
        [
            html.Div([
                dcc.Store(id='user_data', data=user_data),

                dcc.Graph(id='map_clusters', config={'displayModeBar': False})
            ])
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

