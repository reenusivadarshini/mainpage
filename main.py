import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

from PIL import Image

image = Image.open('header.jpg')

st.write("Welcome")

