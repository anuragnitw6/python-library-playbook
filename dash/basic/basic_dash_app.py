from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Hello Dash!"),
    html.P("Your first Dash web app.")
])

if __name__ == '__main__':
    app.run(debug=True)
