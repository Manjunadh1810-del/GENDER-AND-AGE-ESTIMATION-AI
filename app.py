
import streamlit as st
from PIL import Image
import numpy as np
from src.predict import predict_image

st.title("Gender & Age Estimation AI")

file = st.file_uploader("Upload Face Image", type=["jpg","png","jpeg"])
if file:
    img = Image.open(file)
    st.image(img)
    gender, age = predict_image(np.array(img))
    st.success(f"Gender: {gender}")
    st.success(f"Estimated Age: {age}")
