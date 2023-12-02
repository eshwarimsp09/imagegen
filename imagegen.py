import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}
st.title("My App")
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
prompt = st.text_input("prompt")
image_bytes = query({
	"inputs": prompt,
})
name_button = st.button("submit")
if name_button:
    # You can access the image with PIL.Image for example
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image)
