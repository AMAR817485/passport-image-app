import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Passport Photo Maker")

bg_color = st.selectbox(
    "Select Background Color",
    ["White", "Blue", "Red", "Light Gray"]
)

color_map = {
    "White": (255, 255, 255),
    "Blue": (0, 102, 204),
    "Red": (255, 0, 0),
    "Light Gray": (220, 220, 220)
}

uploaded_file = st.file_uploader("Photo upload karo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file)

    output_image = remove(input_image)

    output_image = output_image.convert("RGBA")

alpha = output_image.split()[-1]
alpha = alpha.point(lambda p: 255 if p > 200 else 0)

output_image.putalpha(alpha)

    white_bg = Image.new(
    "RGB",
    output_image.size,
    color_map[bg_color]
)
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
