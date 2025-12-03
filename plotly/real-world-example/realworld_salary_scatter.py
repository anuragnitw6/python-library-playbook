import pandas as pd
import plotly.express as px

df = pd.read_csv("Salary_dataset.csv")

fig = px.scatter(
    df,
    x="Experience",
    y="Salary",
    trendline="ols",
    title="Experience vs Salary (with Trendline)",
)

fig.show()
