import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
# from dash.dependencies import Input, Output
# from backend.send_emails import send_email_to_emails
from app import user_data
import pandas as pd

dash.register_page(__name__)

header = html.Header(
    children=[
        html.H1('Find a Rider')
    ],
    className="header text-center"
)

vehicle_radioitems = html.Div(
    [
        dbc.Label("What kind of transportation do you use?", html_for="vehicle"),
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
        dbc.Label("What time do you plan to travel?", html_for="time"),
        dcc.Dropdown(
            options=[
                {"label": "07:00–08:00", "value": 1},
                {"label": "08:00–09:00", "value": 2},
                {"label": "09:00–10:00", "value": 3},
                {"label": "10:00–11:00", "value": 3},
                {"label": "16:00–17:00", "value": 3},
                {"label": "17:00–18:00", "value": 3},
                {"label": "18:00–19:00", "value": 3}
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

placement_users = pd.read_json(user_data, orient="split")[["FirstName", "LastName"]]
cols = ["FirstName", "LastName"]
placement_users['First_LastName'] = placement_users[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)

location_select = html.Div(
    [
        dbc.Label("Your colleagues who live nearby:", html_for="location"),
        dcc.Dropdown(placement_users['First_LastName'].tolist(),
        multi=True,
        id="location",
        ),
    ],
    className="my-4 form-control",
)

send_invite = html.Div(
    [
        dbc.Button("Invite", size="lg", className="me-1 my-4 btn-primary"),
    ],
    id="send-invite",
    className="text-center"
)

layout = dbc.Container([header, vehicle_radioitems, time_dropdown, interests_badges, location_select, send_invite], fluid=False)