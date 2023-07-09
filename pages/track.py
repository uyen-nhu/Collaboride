import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
# from dash.dependencies import Input, Output
# from backend.qr_code import make_qr_code_stylish

dash.register_page(__name__)

header = html.Div(
    [
        html.H1('Track a Ride')
    ],
    className="header text-center"
)

add_ride = html.Div(
    [
        html.Button('Track ride', id='track_ride_btn', className="add-ride me-1 my-4 btn-primary"),
]

)

# make_qr_code_stylish() # uncomment this line if you want to create a new qr

qr_code = html.Div(
    dbc.Container(
        [
            html.Div(id='qr_code_div')
        ],
        fluid=True,
        className="py-3",
    ),
    className="qr-container my-4 p-4 rounded-3 text-center"
)

layout = html.Div(
    [
        header,
        dbc.Container([add_ride, qr_code], fluid=False)
    ]
)