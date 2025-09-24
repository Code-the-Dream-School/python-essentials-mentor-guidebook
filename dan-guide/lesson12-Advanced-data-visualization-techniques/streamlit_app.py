# setup
# Create a project folder named streamlit_project.
# python -m venv .venv
# After creating the virtual environment, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P), search for "Python: Select Interpreter", and choose the .venv environment.
# Once selected, VSCode will automatically activate the virtual environment in all new terminals. This removes the need to manually activate it every time.
# source .venv/Scripts/activate
# Create requirements.txt file
# pip install -r requirements.txt
# pip install --upgrade setuptools IF ModuleNotFoundError: No module named 'distutils'
# streamlit run streamlit_app.py


import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Set the title and description of the app
st.title("Interactive Data Visualization with Streamlit")
st.write("This app displays an interactive plot of random data. You can change the number of data points.")

# Sidebar with a slider to select the number of data points
num_points = st.sidebar.slider("Number of data points", min_value=10, max_value=1000, value=100)

# Generate random data for plotting
np.random.seed(42)
data = {
    "X": np.random.rand(num_points),
    "Y": np.random.rand(num_points),
    "Category": np.random.choice(["A", "B", "C"], size=num_points)
}

df = pd.DataFrame(data)

# Display the data frame
st.subheader("Data Preview")
st.write(df)

# Create an interactive scatter plot using Plotly
st.subheader("Scatter Plot")
st.caption("Good for showing the relationship between two variables and grouping by categories.")
fig = px.scatter(df, x="X", y="Y", color="Category", title="Random Data Scatter Plot", 
                color_discrete_sequence=["darkmagenta", "aliceblue", "blue"])

#! Colors can be: 
# A hex string (e.g. '#ff0000'), 
# An rgb/rgba string (e.g. 'rgb(255,0,0)'), 
# A named CSS color - 
# An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
# An hsv/hsva string (e.g. 'hsv(0,100%,100%)')

# Show the plot
st.plotly_chart(fig)

# Line plot of X vs Y
st.subheader("Line Plot")
st.caption("Useful for showing trends or changes over continuous data, such as time series.")
line_fig = px.line(df.sort_values("X"), x="X", y="Y", title="Line Plot of X vs Y")
st.plotly_chart(line_fig)

# Bar plot: count of categories
st.subheader("Bar Plot")
st.caption("Best for comparing values across categories, like product sales or survey responses.")
bar_fig = px.bar(df["Category"].value_counts().reset_index(),
                 x="index", y="Category",
                 labels={"index": "Category", "Category": "Count"},
                 title="Bar Plot of Category Counts")
st.plotly_chart(bar_fig)

# Histogram of X values
st.subheader("Histogram")
st.caption("Great for analyzing the distribution of numerical data, spotting patterns or outliers.")
hist_fig = px.histogram(df, x="X", nbins=20, title="Histogram of X Values")
st.plotly_chart(hist_fig)

# Display instructions
st.markdown("""
### How to use:
- Adjust the slider to change the number of data points.
- The plot will update dynamically based on the number of points.
""")
