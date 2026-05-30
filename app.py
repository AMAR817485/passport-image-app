import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Passport Photo Maker")

uploaded_file = st.file_uploader("Photo upload karo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file)

    output_image = remove(input_image)

    white_bg = Image.new("RGB", output_image.size, (255, 255, 255))
    white_bg.paste(output_image, mask=output_image.split()[-1])

    st.image(white_bg, caption="Passport Photo", use_container_width=True)

    buf = io.BytesIO()
    white_bg.save(buf, format="JPEG")

    st.download_button(
        "Download Passport Photo",
        data=buf.getvalue(),
        file_name="passport_photo.jpg",
        mime="image/jpeg"
    )