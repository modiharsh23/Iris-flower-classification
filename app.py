import streamlit as st
import numpy as np
import joblib

# Load saved pipeline
model = joblib.load("/Users/harshmodi/PROGRAMMING/ML/MY PROJECTS/Iris Flower Classification/iris_pipeline.pkl")

st.title("Iris Flower Classification")
st.write("Predict the species of Iris flower using ML model")

# User input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# Predict button
if st.button("Predict"):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)
    species = ["Setosa", "Versicolor", "Virginica"][prediction[0]]

    st.success(f"The predicted species is: **{species}**")