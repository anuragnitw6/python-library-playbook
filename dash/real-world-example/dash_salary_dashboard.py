import time
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("Salary_dataset.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Live Salary Insights Dashboard"),
    
    dcc.Slider(
        id="experience_filter",
        min=df["yearsExperience"].min(),
        max=df["yearsExperience"].max(),
        step=0.5,
        value=df["yearsExperience"].max()
    ),
    
    html.Br(),
    html.Div(id="selected_value"),

    dcc.Graph(id="salary_chart")
])

@app.callback(
    [Output("salary_chart", "figure"),
     Output("selected_value", "children")],
    Input("experience_filter", "value")
)
def update_chart(max_exp):
    filtered = df[df["yearsExperience"] <= max_exp]
    
    fig = px.line(
        filtered,
        x="yearsExperience",
        y="salary",
        markers=True,
        title=f"Salary Trend (Experience ≤ {max_exp})"
    )
    return fig, f"Showing results for Experience ≤ {max_exp} years"

if __name__ == "__main__":
    app.run(debug=True)
