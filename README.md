# Iris Flower Classification

This repository contains a machine learning project for classifying Iris flowers into three species: Setosa, Versicolor, and Virginica. The project includes a Jupyter Notebook for model training and evaluation, and a Python script for a simple web application to demonstrate the classification.

## Files in this Repository

- `training_model.ipynb`: This Jupyter Notebook contains the code for data loading, preprocessing, model training (using a Support Vector Machine), evaluation, and saving the trained model.
- `app.py`: This Python script implements a basic web page using Streamlit. It loads the pre-trained model and provides an interface to predict the species of an Iris flower based on user-provided measurements.
- `iris_model.pkl`: This file is the serialized (pickled) machine learning model trained in `training_model.ipynb`. It's used by `app.py` for making predictions.

## `training_model.ipynb` - Model Training and Evaluation

This notebook covers the following steps:

1.  **Data Loading**: Loads the Iris dataset.
2.  **Data Exploration**: Basic exploration of the dataset.
3.  **Data Preprocessing**: Splits the data into training and testing sets.
4.  **Model Training**: Trains a Support Vector Machine (SVC) classifier on the training data.
5.  **Model Evaluation**: Evaluates the model's performance using accuracy and a classification report.
6.  **Model Saving**: Saves the trained model to `iris_model.pkl` for later use.

## `app.py` - Web Page for Prediction

This Streamlit Page provides a simple web interface to interact with the trained Iris classification model.

### How to Run `app.py`

1.  **Ensure you have the trained model**: Make sure `iris_model.pkl` is present in the same directory as `app.py`. If not, run `training_model.ipynb` first to generate it.
2.  **Install Streamlit**: If you don't have Streamlit installed, you can install it using pip:
    ```bash
    pip install streamlit scikit-learn
    ```
3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

App Over Views
<img a='https://github.com/modiharsh23/Iris-flower-classification/blob/main/README.md?plain=1#:~:text=Screenshot%202025%2D09%2D-,17,-at%2012.12.55.png'>
<img a=''>
<img a=''>
<img a=''>
