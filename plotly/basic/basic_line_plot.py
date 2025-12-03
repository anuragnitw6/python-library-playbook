import plotly.graph_objects as go

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name="Line Example"))

fig.update_layout(title="Basic Line Plot", xaxis_title="X", yaxis_title="Y")

fig.show()
