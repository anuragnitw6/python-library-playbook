import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np
from dash import Dash, dcc, html, Input, Output

df = pd.read_csv("Salary_dataset.csv")

X = df[["yearsExperience"]]
y = df["salary"]

model = LinearRegression()
model.fit(X, y)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Salary Prediction App"),

    dcc.Input(
        id="exp_input",
        type="number",
        placeholder="Enter years of experience",
        value=2
    ),
    
    html.Br(), html.Br(),
    html.Div(id="salary_output")
])

@app.callback(
    Output("salary_output", "children"),
    Input("exp_input", "value")
)
def predict(exp):
    pred = model.predict(np.array(exp).reshape(-1, 1))[0]
    return f"Estimated Salary: ₹{pred:,.2f}"

if __name__ == '__main__':
    app.run(debug=True)
