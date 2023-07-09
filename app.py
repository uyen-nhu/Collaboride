import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd

user_data = pd.read_csv("assets/sample_users.txt", delimiter=",")
user_data['Cluster'] = user_data['Cluster'].astype('int64')
user_data = user_data.to_json(orient="split")
score_data = pd.read_csv("assets/sample_scores.csv", delimiter=",")
score_data['Cluster'] = score_data['Cluster'].astype('int64')
score_data = score_data.to_json(orient="split")

app = dash.Dash(__name__, use_pages=True)

header = html.Header(
    className="header text-center"
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(
            page['name'], href=page["relative_path"]
        ))
        for page in dash.page_registry.values()
    ],
    # brand=html.Img(src=app.get_asset_url("img/Freudenberg_Logo.png"), height="30px"),
    # brand_href="#",
    # color="light",
    # dark=False,
)

app.layout = html.Div(
    [
        header,
        navbar,
        dbc.Container([dash.page_container], className="content")
    ]
)

############ callback functions for home page ############

@app.callback(Output('map_clusters', 'figure'),
              Input('user_data', 'data'))
def update_output_div(df2):
    token = open("assets/token").read().rstrip()

    fig = go.Figure()

    # Add a scattermapbox trace
    fig.add_trace(
        go.Scattermapbox(
            lat=["49.5", "49.405534", "49.651549"],  # Longitude values for the circle centers
            lon=["8.479", "8.692393", "8.813929"],  # Latitude values for the circle centers
            mode='markers+text',
            marker=dict(
                size=[100, 100, 200],  # Size of the circles
                color=['rgba(82, 184, 235, 0.57)', 'rgba(82, 184, 235, 0.57)', 'rgba(0, 42, 85, 0.8)'],
                # Color of the circles (red with 70% opacity)
                opacity=0.7
            ),
            text=['Team 1', 'Team 2', 'Team 3'],
            showlegend=False,
            hoverinfo="none"
        )
    )

    fig.add_trace(
        go.Scattermapbox(
            lat=['49.555787'],  # Replace '<latitude>' with the fixed latitude value
            lon=['8.664191'],  # Replace '<longitude>' with the fixed longitude value
            mode='markers+text',
            marker=dict(
                size=10,  # Size of the dot
                color='red'  # Color of the dot (red)
            ),
            text=['Headquarter'],
            textposition='top center',
            hoverinfo="none"
        )
    )

    # Update the layout
    fig.update_layout(
        mapbox=dict(
            style='light',  # Mapbox style
            zoom=9,  # Zoom level
            center=dict(lat=49.55, lon=8.6),
            accesstoken=token

        ),
        margin={'l': 0, 'r': 0, 't': 0, 'b': 0}
    )
    fig.update_layout(showlegend=False)

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)