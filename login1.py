import streamlit as st
from PIL import Image
import pandas as pd

import matplotlib.pyplot as plt
# Add text
st.title("Heart Disease Information")
st.markdown("## Overview")
st.markdown("Heart disease refers to a range of conditions that affect the heart and blood vessels.")

# Add images
img = Image.open("E:\PILLAI COLLEGE\MLPROJECT\heart.png")
st.image(img, width=300)

# Add tables
st.markdown("## Risk Factors")
risk_factors = ["High blood pressure", "High cholesterol", "Smoking", "Diabetes", "Obesity", "Physical inactivity", "Age", "Family history"]
st.table(risk_factors)




# Load the heart disease data set
df = pd.read_csv("E:\PILLAI COLLEGE\MLPROJECT\datasets\dataset\heart.csv")

# Create a bar chart of the number of cases for each type of heart disease
st.bar_chart(df['target'].value_counts())

# Create a histogram of age
st.histogram(df['age'],bins=30)

# Create a scatter plot of age vs. cholesterol
st.scatter_plot(df['age'], df['chol'])

# Create a box plot of blood pressure by heart disease status
st.box_plot(df['trestbps'], df['target'])