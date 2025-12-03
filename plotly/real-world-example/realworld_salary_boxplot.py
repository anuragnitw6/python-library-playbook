import pandas as pd
import plotly.express as px

df = pd.read_csv("Salary_dataset.csv")

fig = px.box(df, y="Salary", title="Salary Distribution")

fig.show()
