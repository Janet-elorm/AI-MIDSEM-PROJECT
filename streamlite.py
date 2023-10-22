import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model_filename = 'copy_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

st.title("FIFA Player Rating Prediction")
st.write("This app predicts FIFA player ratings.")

# Create input fields for user input
st.sidebar.header("User Input")
dob = st.sidebar.date_input("Date of Birth")
value_eur = st.sidebar.number_input("Value EUR")
movement_reactions = st.sidebar.number_input("Movement Reaction")
potential = st.sidebar.number_input("Potential")
release_clause_eur = st.sidebar.number_input("Release Clause EUR")
sofifa_id = st.sidebar.number_input("Sofifa ID")
gk = st.sidebar.text_input("GK")
rb = st.sidebar.text_input("RB")
wage_eur = st.sidebar.number_input("WAGE EUR")
age=st.sidebar.number_input("Age")

predict = st.sidebar.button("Predict")

if predict:
    # Validate and preprocess input data
    # Validate and preprocess input data
    # Validate and preprocess input data
    if dob is None or dob == "":
        st.sidebar.error("Please enter a valid Date of Birth.")
    else:
        age = (pd.Timestamp.now() - pd.Timestamp(dob)).days // 365
        if gk == "" or rb == "":
            st.sidebar.error("GK and RB should not be empty.")
        else:
            # Add a placeholder value (0) for 'dob'
            input_features = np.array([age, value_eur, movement_reactions, potential, release_clause_eur, sofifa_id, float(gk), float(rb), wage_eur, 0]).reshape(1, -1)
            predicted_rating = model.predict(input_features)
            st.write(f"Predicted Rating: {predicted_rating[0]:.2f}")



# You can also add other content to your Streamlit app
st.sidebar.write("Welcome to the FIFA Player Rating Prediction App!")