import streamlit as st
import pickle
import numpy as np 

# streamlit run file_name.py

st.set_page_config(page_title="AI18-Predictor", page_icon="💵")

st.title("AI18 Predictor")

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

yoe = st.number_input("Experience Years", min_value=0.0, max_value=10.0, step=0.5, value=2.0)

if st.button("Predict"):
    predictions = model.predict([[yoe]])
    st.success(np.round(predictions[0], 2))