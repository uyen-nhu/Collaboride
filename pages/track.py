import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
# from dash.dependencies import Input, Output
# from backend.qr_code import make_qr_code_stylish

dash.register_page(__name__)

header = html.Header(
    children=[
        html.H1('Track a Ride')
    ],
    className="header text-center"
)

add_ride = html.Div(
    [
        dbc.Button("Add Ride", size="lg", className="me-1 my-4 btn-primary"),
    ],
    id="add-ride",
    className="text-center"
)

# make_qr_code_stylish() # uncomment this line if you want to create a new qr

qr_code = html.Div(
    dbc.Container(
        [
            html.Img(src='assets/qr_code.png', alt='QR Code')
        ],
        fluid=True,
        className="py-3",
    ),
    className="my-4 p-5 bg-secondary rounded-3 text-center"
)

layout = dbc.Container([header, add_ride, qr_code], fluid=False)