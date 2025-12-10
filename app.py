import os, streamlit as st, google.generativeai as genai
from PIL import Image; from dotenv import load_dotenv
load_dotenv(); genai.configure(api_key=os.getenv("GENAI_API_KEY"))
m = genai.GenerativeModel("gemini-2.5-flash")
st.title("Plant Health Checker")
f = st.file_uploader("Upload leaf image", type=["jpg","jpeg","png"])
if f:
    img = Image.open(f); st.image(img, caption="Uploaded leaf")
    r = m.generate_content(["You are a plant doctor. Say if this leaf is healthy; if not, guess disease and give 3 simple fixes.", img])
    st.write(r.text)
