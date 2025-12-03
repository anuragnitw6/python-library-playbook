import plotly.express as px

x = [5, 10, 15, 20, 25]
y = [50, 60, 55, 70, 80]

fig = px.scatter(x=x, y=y, title="Basic Scatter Plot")

fig.show()
