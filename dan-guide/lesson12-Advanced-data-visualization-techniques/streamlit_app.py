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

# Display instructions
st.markdown("""
### How to use:
- Adjust the slider to change the number of data points.
- The plot will update dynamically based on the number of points.
""")
