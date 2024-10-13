import streamlit as st
import google.generativeai as genai
from apikey import gemini_open_apikey
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=gemini_open_apikey)



# Create the model
generation_config = {
  "temperature": 0.7,
  "top_p": 1,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# Setting the page config
st.set_page_config(layout="wide")

# Title of your page
st.title("The AI Artisan 🤖")

# Sub header -- Descripiton of what the page does
st.subheader("Crafting creative wonders with the help of AI 💡")

# Get input of what the title of the blog and keywords to generate the article/blog

with st.sidebar:
  st.title('Input the creative article details')
  st.subheader('Enter the title and keywords for the article')
  article_input = st.text_input('Title of the article')
  keywords_input = st.text_area('Keywords (Comma separate)')
  num_words =  st.slider('Work Limit', min_value=100, max_value=1000, step=100)
  parts = [
        f"Generate a blog with title {article_input} with keywords {keywords_input}. Make sure to include the keywords and also provide relevant article without any use of jargon language",
      ]
  response = model.generate_content(parts)
  
  submit = st.button('Generate')

if submit:
  st.write(response.text)
