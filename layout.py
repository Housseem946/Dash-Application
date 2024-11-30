from dash import html, dcc

def create_layout():
    return html.Div([
        html.H1("Bienvenue sur ma première application Dash", style={'textAlign': 'center'}), # Titre

        # Zone de texte
        html.Div([
            dcc.Input(id='input-text', type='text', placeholder='Entrez un texte', style={'marginRight': '10px'}),
            html.Button("Soumettre", id='submit-button', n_clicks=0),
            html.Div(id='output-text', style={'marginTop': '20px'}),
        ], style={'textAlign': 'center'}),

        # Graphe
        dcc.Graph(
            id='example-graph',
            config={'displayModeBar': False}  # Supprime la barre d'outils pour le graph
        ),

        # Dropdown
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Option 1', 'value': 'opt1'},
                {'label': 'Option 2', 'value': 'opt2'},
                {'label': 'Option 3', 'value': 'opt3'}
            ],
            placeholder="Sélectionnez une option",
        ),

        html.Div(id='dropdown-output', style={'marginTop': '20px'})
    ])
