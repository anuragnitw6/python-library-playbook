import pandas as pd
import plotly.express as px

df = pd.read_csv("Salary_dataset.csv")

fig = px.histogram(df, x="Salary", nbins=15, title="Salary Histogram")

fig.show()
