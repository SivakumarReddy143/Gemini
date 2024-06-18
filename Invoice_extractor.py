from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro-vision')

def get_response(input,image,prompt):
    result=model.generate_content([input,image[0],prompt])
    return result.text
def input_image_details(uploaded_file):
    bytes_data=uploaded_file.getvalue()
    image_parts=[
        {
        "mime_type":uploaded_file.type,
        "data":bytes_data
        }
    ]
    return image_parts
st.set_page_config("Multilanguage invoice extractor")
input_text=st.text_input("Enter your prompt")
uploaded_file=st.file_uploader("upload your file",type=['png','jpg','jpeg'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Invoice",use_column_width=True,)
input_prompt="""
you are an expert in understanding invoices.so now you have to extract paricular information
from given invoice.
"""
submit=st.button("Tell me about the invoice")

if submit:
    image_data=input_image_details(uploaded_file)
    response=get_response(input_prompt,image_data,input_text)
    st.write("The response is:")
    st.write(response)
