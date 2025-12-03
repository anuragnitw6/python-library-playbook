import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("Salary_dataset.csv")

# --- Scatter Plot ---
scatter_fig = px.scatter(
    df,
    x="Experience",
    y="Salary",
    trendline="ols",
    title="Experience vs Salary (Trendline)",
)

# --- Histogram ---
hist_fig = px.histogram(
    df,
    x="Salary",
    nbins=20,
    title="Salary Distribution Histogram"
)

# --- Box Plot ---
box_fig = px.box(
    df,
    y="Salary",
    title="Salary Boxplot"
)

# --- Combined Dashboard ---
dashboard = go.Figure()

dashboard.add_trace(go.Scatter(
    x=df["Experience"], y=df["Salary"],
    mode="markers", name="Scatter Plot"
))

dashboard.update_layout(
    title="Salary Analysis Mini Dashboard",
    xaxis_title="Experience (Years)",
    yaxis_title="Salary",
)

scatter_fig.show()
hist_fig.show()
box_fig.show()
dashboard.show()
