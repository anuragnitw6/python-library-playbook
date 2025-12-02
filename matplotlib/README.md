📊 Matplotlib — Complete Python Guide

A collection of Basic, Mini, and Real-World examples for learning and mastering Matplotlib.

This repository is designed for beginners, students, and developers who want to quickly understand data visualization using Python.

🔧 What is Matplotlib?

Matplotlib is the most widely used Python library for 2D data visualization.
It helps you create:

✔ Line plots
✔ Scatter plots
✔ Bar charts
✔ Histograms
✔ Heatmaps
✔ And much more…
🚀 Getting Started
Install Required Library:
pip install matplotlib pandas

🟢 1. Basic Example

A simple line plot to understand Matplotlib syntax.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 7, 5]

plt.plot(x, y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Basic Line Plot")
plt.show()

🟡 2. Mini Example

Scatter plot using the first 10 rows of a dataset.

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

sample = df.head(10)

plt.scatter(sample["YearsExperience"], sample["Salary"])
plt.title("Mini Scatter Plot (First 10 Rows)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

🔵 3. Real-World Example (Full Dataset)

Using Salary_dataset.csv to create meaningful insights.

📍 A. Scatter Plot — Salary vs Experience
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Salary_dataset.csv")

plt.figure(figsize=(8,5))
plt.scatter(df["YearsExperience"], df["Salary"], alpha=0.8)
plt.title("Salary vs Years of Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

📍 B. Line Plot (Trend)
df_sorted = df.sort_values("YearsExperience")

plt.plot(df_sorted["YearsExperience"], df_sorted["Salary"])
plt.title("Salary Trend by Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

📍 C. Histogram — Salary Distribution
plt.hist(df["Salary"], bins=10)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

📍 D. Bar Chart — First 10 Values
first_10 = df.head(10)

plt.bar(first_10["YearsExperience"], first_10["Salary"])
plt.title("Salary Bar Chart (First 10 Rows)")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.show()

🧠 What You Learn from This Repo

✔ Basics of Matplotlib
✔ Plotting using real datasets
✔ Visualizing trends
✔ Creating scatter, bar, histogram, and line plots
✔ How real data visualizations are structured

⭐ Contribute

Feel free to add more visualizations and improve this repository.
This project is beginner-friendly!
