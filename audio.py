from transformers import  pipeline
import requests
import os
from transformers import AutoTokenizer, AutoModelForCausalLM
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import textwrap
import os
import streamlit as st
from PIL import Image
import json
from streamlit_lottie import st_lottie
from gtts import gTTS


def text_to_speech(text, filename="speech.wav", lang="en"):
    """The gTTS library in Python stands for Google Text-to-Speech. 
    It's a convenient tool that allows you to convert text into audio files using the Google Text-to-Speech API."""
    
    """Converts text to speech and stores it as a WAV file using gTTS.

    Args:
        text (str): The text to convert to speech.
        filename (str, optional): The filename of the output WAV file. Defaults to "speech.wav".
        lang (str, optional): The language code for the voice. Defaults to "en" (English).
    """

    try:
        # Create a gTTS object
        tts = gTTS(text=text, lang=lang)

        # Save the audio to a WAV file
        tts.save(filename)
        print(f"Speech saved to {filename}")
    except Exception as e:
        print(f"Error converting text to speech: {e}")



def to_markdown(text):
   """Converts text to Markdown, indenting lines and replacing asterisks with periods.

   Args:
       text (str): The text to be converted.

   Returns:
       IPython.display.Markdown: A Markdown object representing the formatted text.
   """


   # Then apply Markdown formatting
   markdown_text = textwrap.indent(text, "> ", predicate=lambda _: True)

   # Return the Markdown object
   return Markdown(markdown_text)

os.environ["GOOGLE_API_KEY"] = "AIzaSyAM_VBEDuud6PEmN5kB-KhUAry5L7UYifc"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# # Img - to- text


def img2text(url):
    """1. def img2text(url):

    Defines a function named img2text that takes a URL (string) as input.
    2. image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    Creates a pipeline using the Transformers library.
    The first argument, "image-to-text", specifies the task of extracting text from images.
    The second argument, "Salesforce/blip-image-captioning-base", defines the specific pre-trained model to be used for this task. This example uses a pre-trained model from Salesforce for image captioning.
    
    3. text = image_to_text(url)[0]["generated_text"]

    Invokes the image_to_text pipeline with the provided URL as input.
    image_to_text(url) performs the image-to-text conversion using the chosen model.
    Accesses the first element of the returned list (assuming the pipeline might return multiple outputs in some cases).
    Extracts the key generated_text from the dictionary within the first element, which contains the generated text caption for the image.

    4. return text

    Returns the extracted text caption from the image to the caller of the function.
    In summary:

    This function takes an image URL as input.
    It uses a pre-trained image captioning model to extract text from the image.
    It returns the generated text caption."""

    image_to_text = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    text = image_to_text(url)[0]["generated_text"]
    return text



#LLM


def textgen(message):
    
    model = genai.GenerativeModel("gemini-pro")  # Load a pre-trained Generative Model
    response = model.generate_content(f"write moral story about {message} at last explain moral of it start with title of the story")
    try:
        return response.text
    except:
        st.warning("Don't upload one image twice it would be ambiguous to generate...")






with st.container():
    try:
        @st.cache_data(ttl=(60*60))
        def load_lottie_file(filename):
            with open(filename,"r") as file:
                gif = json.load(file)
            st_lottie(gif, speed=1, width=650, height=450)
            
        load_lottie_file("audio.json")
    except:
        print("dont find any lottie files")

st.title("image story summarization with text to speech")
F = st.file_uploader("select any image: ", type=['jpg', 'png','jpeg'])
if F is not None:
    image = Image.open(F)
    st.image(image)
    img_text = img2text(image)
    story = textgen(img_text)
    speech = text_to_speech(story)

    
    with st.expander("read image text caption"):
        st.markdown(img_text)
    with st.expander("read the story related to the caption"):
        st.markdown(story)
    st.audio("speech.wav")
    
    