import streamlit as st
from google import genai
from PIL import Image

st.set_page_config(page_title="AI Inspector", layout="wide")
st.title("🔍 AI Inspector: Gemini 3 Fix-It Assistant")

# API kalitni kiritish
api_key = st.sidebar.text_input("AIzaSyDr1ChIuhiaZsjiVab4yKUSoalP2abOd1U", type="password")

if api_key:
    client = genai.Client(api_key=api_key)
    
    # Rasm yuklash qismi
    uploaded_file = st.file_uploader("Muammoni rasmga olib yuklang...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Yuklangan rasm", width=400)
        
        if st.button("Muammoni aniqlash"):
            with st.spinner("Gemini 3 tahlil qilmoqda..."):
                try:
                    # Rasm bilan birga prompt yuboramiz
                    prompt = "Ushbu rasmdagi muammoni aniqla va uni qanday tuzatish bo'yicha qisqa, tushunarli qo'llanma ber."
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=[prompt, image]
                    )
                    st.subheader("AI Tavsiyasi:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Xatolik: {e}")
else:
    st.warning("Iltimos, chap menyuga API kalitni kiriting.")