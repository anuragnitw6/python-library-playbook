import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("Salary_dataset.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Salary vs Experience Dashboard"),
    
    dcc.Dropdown(
        id="color_dropdown",
        options=[{"label": col, "value": col} for col in df.columns],
        value="salary",
        clearable=False
    ),

    dcc.Graph(id="scatter_chart")
])

@app.callback(
    Output("scatter_chart", "figure"),
    Input("color_dropdown", "value")
)
def update_chart(selected_color):
    fig = px.scatter(
        df,
        x="yearsExperience",
        y="salary",
        color=selected_color,
        title="Salary vs Experience",
        trendline="ols"
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)
