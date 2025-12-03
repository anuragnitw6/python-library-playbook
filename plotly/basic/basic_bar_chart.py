import plotly.graph_objects as go

fruits = ["Apple", "Banana", "Mango", "Orange"]
values = [10, 6, 8, 14]

fig = go.Figure()
fig.add_trace(go.Bar(x=fruits, y=values, name="Fruits Count"))

fig.update_layout(title="Basic Bar Chart", xaxis_title="Fruit", yaxis_title="Count")

fig.show()
