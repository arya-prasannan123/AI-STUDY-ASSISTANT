import os
import streamlit as st
from google import genai

st.set_page_config(page_title="AI Study Assistant")

st.title("📚 AI Study Assistant")
st.write("Learn smarter with AI!")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Please set your Gemini API key first.")
    st.stop()

client = genai.Client(api_key=api_key)

topic = st.text_input("Enter your study topic")
level = st.selectbox(
    "Choose your study level",
    ["School", "Plus Two", "College"]
)

task = st.selectbox(
    "Choose what you want",
    [
        "Make short notes",
        "Generate 5 questions",
        "Explain in simple words",
        "Create a quiz"
    ]
)

if st.button("Generate"):
    if topic.strip():
        prompt = f"""
        You are a helpful study assistant.
        Study level: {level}
        Topic: {topic}
        Task: {task}
        Explain in simple English.
        Adjust the answer to the selected study level.
        Use headings and clear points.
        """
        try:
            with st.spinner("Preparing your study material..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=prompt
                )
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please enter a topic.")