import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from app import user_data
from app import score_data
import pandas as pd


dash.register_page(__name__, path='/')

header = html.Header(
    children=[
        html.H1('Home')
    ],
    className="header text-center"
)

map_cluster = html.Div(
    dbc.Container(
        [
            html.Div([
                dcc.Store(id='user_data', data=user_data),
                dcc.Store(id='score_data', data=score_data),

                dcc.Graph(id='map_clusters', config={'displayModeBar': False})
            ])
        ],
        fluid=True,
        className="py-3",
    ),
    id="map",
    className="my-4 rounded-3 text-center"
)

placement_users = pd.read_json(user_data, orient="split")[["FirstName", "LastName", "Cluster"]]
score_data = pd.read_json(score_data, orient="split")

cols = ["FirstName", "LastName"]
placement_users['First_LastName'] = placement_users[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
placement_users.First_LastName = placement_users.First_LastName + ", "
placement_users_grouped_by_cluster = placement_users.groupby('Cluster')['First_LastName'].apply(list).reset_index(name='Team members')

placement_users_grouped_by_cluster_scores = pd.merge(placement_users_grouped_by_cluster, score_data, on=["Cluster"])
placement_users_grouped_by_cluster_scores['Cluster'] = placement_users_grouped_by_cluster_scores['Cluster'].map({1:'Team B', 2:'Team A', 3:'Team C'})
placement_users_grouped_by_cluster_scores = placement_users_grouped_by_cluster_scores.rename(columns={'Cluster': 'Team name'})
placement_users_grouped_by_cluster_scores['Rank'] = placement_users_grouped_by_cluster_scores['Score'].rank()

placement_users_grouped_by_cluster_scores = placement_users_grouped_by_cluster_scores[['Rank', 'Team name', "Score"]]

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
        dbc.Table.from_dataframe(placement_users_grouped_by_cluster_scores, bordered=True,id="leaderboard")
    ],
    className="my-4"
)

layout = dbc.Container([header, map_cluster, leaderboard_table], fluid=False)

