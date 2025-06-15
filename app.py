import pandas as pd
from sklearn.linear_model import LinearRegression
import gradio as gr

# Load x and y
x = pd.read_csv('x.csv')
y = pd.read_csv('y.csv').values.ravel()  # Convert to 1D array if needed

# Train model
model = LinearRegression()
model.fit(x, y)

# Predict function
def predict(income):
    spending = model.predict([[income]])[0]
    return f"Predicted Spending: ${spending:.2f}"

# Gradio interface
gr.Interface(
    fn=predict,
    inputs="number",
    outputs="text",
    title="Income vs. Spending Predictor"
).launch()
