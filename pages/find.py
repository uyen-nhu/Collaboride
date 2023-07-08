import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

dash.register_page(__name__)

vehicle_radioitems = html.Div(
    [
        dbc.Label("How do you go to work?", html_for="vehicle"),
        dbc.RadioItems(
            options=[
                {"label": "Car", "value": "car"},
                {"label": "Bus", "value": "bus"},
                {"label": "Bike", "value": "bike"},
            ],
            value=1,
            id="vehicle",
        ),
    ],
    className="my-4 form-control",
)

time_dropdown = html.Div(
    [
        dbc.Label("What time do you plan to go to work?", html_for="time"),
        dcc.Dropdown(
            options=[
                {"label": "07:00–08:00", "value": 1},
                {"label": "08:00–09:00", "value": 2},
                {"label": "09:00–10:00", "value": 3},
            ],
            id="time",
        ),
    ],
    className="my-4 form-control",
)

interests_badges = html.Div(
    [
        dbc.Label("What are your interests?", html_for="interests"),
        html.Div(
            [
                dbc.Badge(
                    "Sports",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Music",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Cooking",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Traveling",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Reading",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Movies",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Fitness",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Outdoors",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Art",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Socializing",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Volunteering",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
                dbc.Badge(
                    "Learning",
                    href="#",
                    color="secondary",
                    className="me-1 text-decoration-none",
                ),
            ],
            id="interests",
        )
    ],
    className="my-4 form-control",
)

location_select = html.Div(
    [
        dbc.Label("Your colleagues who live nearby:", html_for="location"),
        dcc.Dropdown(
            options=[
                {"label": "Bob", "value": 1},
                {"label": "Ann", "value": 2},
                {"label": "John", "value": 3},
            ],
            multi=True,
            id="location",
        ),
    ],
    className="my-4 form-control",
)

layout = dbc.Container([vehicle_radioitems, time_dropdown, interests_badges, location_select], fluid=False)