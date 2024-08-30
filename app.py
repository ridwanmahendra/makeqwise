import os
import streamlit as st
import openai
from dotenv import load_dotenv

# Load variabel dari file .env
load_dotenv()

# Set API key OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz(topic, num_questions=5, question_type="multiple_choice"):
    # Prompt untuk pilihan ganda
    if question_type == "multiple_choice":
        prompt = f"Buatlah {num_questions} pertanyaan kuis pilihan ganda dengan jawaban tentang {topic}. Sediakan 4 opsi untuk setiap pertanyaan dan tunjukkan jawaban yang benar."
    # Prompt untuk esai
    else:
        prompt = f"Generate {num_questions} pertanyaan kuis bergaya esai dengan model jawaban tentang {topic}."

    # Menggunakan model gpt-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=1500,
        temperature=0.7,
    )

    quiz_text = response.choices[0].message['content'].strip()
    return quiz_text

# Streamlit app title
st.title("Makeqwise AI - Universitas Teknokrat Indonesia")

# User input for topic
topic = st.text_input("Masukkan topik untuk kuis:")

# User input for number of questions
num_questions = st.slider("Jumlah pertanyaan:", 1, 10, 5)

# User selects question type
question_type = st.selectbox("Pilih jenis soal:", ["Pilihan Ganda", "Esai"])

# Generate quiz button
if st.button("Buat Kuis"):
    if topic:
        quiz = generate_quiz(topic, num_questions, question_type)
        st.subheader(f"Kuis tentang: {topic}")
        st.write(quiz)
    else:
        st.warning("Silakan masukkan topik terlebih dahulu.")

# Footer
st.markdown("Dibuat dengan ❤️ oleh Pusat Unggulan Kecerdasan Buatan Universitas Teknokrat Indonesia")
