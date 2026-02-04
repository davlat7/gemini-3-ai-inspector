import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="AI Inspector", layout="wide")
st.title("🔍 AI Inspector: Gemini 2 Fix-It Assistant")

# API kalitni kiritish
api_key = st.sidebar.text_input("AIzaSyAp2j2FJlPJNmPnQVsoqlUX41e6_k317jo", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    # Rasm yuklash qismi
    uploaded_file = st.file_uploader("Image fix...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image", width=400)
        
        if st.button("Find The Problem"):
            with st.spinner("Gemini 3 fixing ..."):
                try:
                    prompt = "This picture problem to fix give me promt."
                    response = client.models.generate_content(model="gemini-2.0-flash", contents=[image, prompt])
                    st.write(response.text)
                except Exception as e:
                    if "429" in str(e):
                        st.error("API limit is exceeded Please wait a minute.")
                    else:
                        st.error(f"Error: {e}")
else:

    st.warning("Enter your API key on the left side.")
