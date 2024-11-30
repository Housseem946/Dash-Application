from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Exemple de données
df = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Values': [10, 20, 30]
})

def register_callbacks(app):
    # Callback pour mettre à jour le texte
    @app.callback(
        Output('output-text', 'children'),
        Input('submit-button', 'n_clicks'),
        Input('input-text', 'value')
    )
    def update_text(n_clicks, value):
        if n_clicks > 0 and value:
            return f"Vous avez entré : {value}"
        return "Aucune entrée soumise."

    # Callback pour mettre à jour le graphique
    @app.callback(
        Output('example-graph', 'figure'),
        Input('dropdown', 'value')
    )
    def update_graph(option):
        # Exemple d'un graphique dynamique
        if option == 'opt1':
            fig = px.bar(df, x='Category', y='Values', title="Graphique en barres")
        elif option == 'opt2':
            fig = px.line(df, x='Category', y='Values', title="Graphique en lignes")
        else:
            fig = px.pie(df, names='Category', values='Values', title="Graphique circulaire")
        return fig

    # Callback pour afficher la sélection du dropdown
    @app.callback(
        Output('dropdown-output', 'children'),
        Input('dropdown', 'value')
    )
    def update_dropdown_output(value):
        if value:
            return f"Vous avez sélectionné : {value}"
        return "Aucune option sélectionnée."
