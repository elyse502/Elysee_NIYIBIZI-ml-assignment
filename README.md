<div align="center">

# 🧠 Machine Learning Tutorial Project 🤖💻ℹ️

![logo](https://github.com/user-attachments/assets/aa7f940a-4a58-4e67-a148-20ef299e7d95)

**University:** [University of Kigali](https://uok.ac.rw/)

**Module:** Artificial Intelligence

**Instructor:** [Mr. Victor MUVUNYI](https://www.linkedin.com/in/muvunyi-victor-4a83342a/?originalSubdomain=rw)

**Author:** [Elysée NIYIBIZI](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/)

**Major:** [Computer Science](https://uok.ac.rw/programs/bachelor-of-science-with-honours-in-computer-science/)

**Reg No:** 2305000921
</div>

---

## 📘 Overview

This repository contains a complete walkthrough tutorial on basic Machine Learning, focusing on **Linear Regression**, using **Pandas**, **Scikit-learn**, **Matplotlib**, and model evaluation metrics like **Mean Squared Error (MSE)**. It is based on hands-on instruction provided by Mr. Victor Muvunyi.

The example used throughout this tutorial involves analyzing the relationship between **Income** and **Cosmetics Spending**.

---

## 📊 Project Objectives

* Understand how to structure and clean real-world data
* Visualize data to determine model suitability
* Apply Linear Regression using Scikit-learn
* Evaluate model performance using MSE
* Build and test a simple prediction app using Gradio (optional)

---

## 🛠 Tools Used

* Python 3
* Pandas
* Matplotlib
* Scikit-learn
* Gradio (optional)

---

## 🧹 1. Data Preparation & Cleaning

### Tasks:

* Load tabular data using Pandas
* Identify and handle missing values

### Key Methods:

```python
pd.DataFrame()
df.fillna()
df.mean(), df.median()
```

### Why?

* Missing values can break regression algorithms
* Filling with median/mean avoids data loss

---

## 📈 2. Exploratory Data Analysis (EDA)

### Tasks:

* Visualize Income vs. Spending

### Code Example:

```python
plt.scatter(df["Income"], df["Spending"])
plt.title("Income vs. Spending")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.show()
```

### Why?

* A linear pattern justifies the use of Linear Regression

---

## 📐 3. Linear Regression Modeling

### Tasks:

* Fit a model that predicts Spending from Income

### Code Example:

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)
```

### Interpretation:

* **Intercept (\u03b2₀)**: Baseline spending
* **Slope (\u03b2₁)**: Increase in spending per \$1 income

---

## ✅ 4. Model Evaluation (MSE)

### Tasks:

* Compare predicted vs. actual values
* Calculate MSE

### Code:

```python
from sklearn.metrics import mean_squared_error
y_pred = model.predict(x)
mse = mean_squared_error(y, y_pred)
```

### Why?

* MSE gives a sense of the model’s accuracy (lower is better)

---

## 🔍 5. Residual Analysis

### Tasks:

* Plot residuals to detect model issues

### Code:

```python
residuals = y - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='red')
plt.title("Residual Plot")
plt.show()
```

### Why?

* Random scatter: model is likely a good fit
* Pattern: model may be missing variables

---

## 🌐 6. Optional: Gradio UI for Prediction

### Tasks:

* Build an interface for predicting spending from income

### Code Example:

```python
import gradio as gr

def predict(income):
    prediction = model.predict([[income]])[0]
    return f"Predicted Spending: ${prediction:.2f}"

gr.Interface(fn=predict, inputs="number", outputs="text").launch()
```

---

## 🗂️ File Structure

```json
├── notebook.ipynb           # Step-by-step tutorial
├── data/                    # Optional dataset storage
├── app.py                   # Optional Gradio UI script
├── requirements.txt         # Python dependencies
├── README.md                # Project overview
```

---

## 📦 How to Run the Project

### 1. Clone the Repo

```console
git clone https://github.com/elyse502/Elysee_NIYIBIZI-ml-assignment
.git
cd Elysee_NIYIBIZI-ml-assignment
```

### 2. Create a virtual environment (Prevents System Pollution)
```console
python -m venv ml-env
source ml-env/bin/activate  # or ml-env\Scripts\activate on Windows
```

### 3. Install Requirements

```console
pip install -r requirements.txt
```

### 4. Open the Notebook

```console
jupyter notebook notebook.ipynb
```

### 5. Run the App (optional)

```console
python app.py
```

---

## 📚 Key Takeaways

* Pandas = spreadsheet-like data handling
* Linear Regression = fits a line to predict Y from X
* MSE = evaluates model error
* Residuals = help debug model assumptions

---

## 🧑‍🏫 Author
- [**NIYIBIZI Elysée**](https://linktr.ee/niyibizi_elysee)👨🏿‍💻 | [Github](https://github.com/elyse502) | [Linkedin](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/) | [Twitter](https://twitter.com/Niyibizi_Elyse).
- _**Email**: <elyseniyibizi502@gmail.com>_
- **Reg No:** 2305000921
- **Course:** [Artificial Intelligence](https://x.com/muvunyiv555/status/1929896159922848225)
- **Instructor:** [Mr. Victor MUVUNYI](https://x.com/muvunyiv555)
- **University:** [University of Kigali](https://uok.ac.rw/)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/niyibizi-elys%C3%A9e/) [![@phenrysay](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Niyibizi_Elyse) [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/elyse502)

---

> This README summarizes a practical ML tutorial that connects theory with implementation using Python. Designed as an academic learning aid.

---

<br />

<div align="center">
  
This project is part of the AI/ML & Big Data assignment at the [University of Kigali](https://uok.ac.rw/) 👨‍🎓📚🏫.

<br />
Made with ❤️ by <b>Elysée NIYIBIZI</b>
</div>




