from matplotlib.pyplot import gray
import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    # This will start the camera
    camera_image = st.camera_input("Camera")

with st.expander("Upload Image"):
    # This will upload an image
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        # This will display the image
        img = Image.open(uploaded_image)

        # Convert the image to grayscale
        gray_img = img.convert("L")

        # Display the grayscale image
        st.image(gray_img, caption="Grayscale Image", use_column_width=True)

if camera_image:
    # This will display the image
    img = Image.open(camera_image)

    # Convert the image to grayscale
    gray_img = img.convert("L")

    # Display the grayscale image
    st.image(gray_img, caption="Grayscale Image", use_column_width=True)
