import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__)

add_ride = html.Div(
    [
        dbc.Button("Add Ride", size="lg", className="me-1 my-4 btn-primary"),
    ],
    id="add-ride",
    className="text-center"
)

qr_code = html.Div(
    dbc.Container(
        [
            html.H1("[QR CODE]")
        ],
        fluid=True,
        className="py-3",
    ),
    className="my-4 p-5 bg-secondary rounded-3 text-center"
)

layout = dbc.Container([add_ride, qr_code], fluid=False)