from dash import Dash
from layout import create_layout
from callback import register_callbacks

# Créer l'application Dash
app = Dash(__name__, suppress_callback_exceptions=True)

# Définir le layout
app.layout = create_layout()

# Enregistrer les callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
