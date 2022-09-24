import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image

image = Image.open('header.jpg')

st.write("Welcome")
import streamlit as st

# Create an empty container
placeholder = st.empty()

actual_emaild1 = "dr_sharmelee99@gmail.com"
actual_passwordd1 = "dr_sharmelee123"

actual_emaild2 = "dr_sherina@gmail.com"
actual_passwordd2 = "dr_sherina123"

actual_emaild3 = "dr_sammera@gmail.com"
actual_passwordd3 = "dr_sammera123"

actual_emaild4 = "dr_gladin@gmail.com"
actual_passwordd4 = "dr_gladin123"

actual_emaild4 = "dr_angellina@gmail.com"
actual_passwordd4 = "dr_angellina123"

actual_emailp1 = "pat_reenu@gmail.com"
actual_passwordp1 = "pat_reenu"

actual_emailp2 = "pat_riya@gmail.com"
actual_passwordp2 = "pat_riya1"

actual_emailp3 = "pat_jack@gmail.com"
actual_passwordp3 = "pat_jack"

actual_emailp4 = "pat_ryan@gmail.com"
actual_passwordp4 = "pat_ryan"

actual_emailp5 = "pat_nina@gmail.com"
actual_passwordp5 = "pat_nina"

actual_emailp5 = "pat_klaus@gmail.com"
actual_passwordp5 = "pat_klaus"

# Insert a form in the container
with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email == actual_emaild1 and password == actual_passwordd1:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SHARMELEE KUMAR ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
elif submit and email == actual_emaild2 and password == actual_passwordd2:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SHERINA CARMEL ") 
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/")

elif submit and email == actual_emaild3 and password == actual_passwordd3:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SAMEERA SHAMMA ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/")
    
elif submit and email == actual_emaild4 and password == actual_passwordd4:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. GLADIN  ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/")
    
elif submit and email == actual_emaild5 and password == actual_passwordd5:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. ANGELLINA K JOB ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
    
elif submit and email == actual_emailp1 and password == actual_passwordp1:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Miss Reenu Sivadarshini M ")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email == actual_emailp2 and password == actual_passwordp2:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mrs Riya")   
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email == actual_emailp3 and password == actual_passwordp3:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr Jack")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email == actual_emailp4 and password == actual_passwordp4:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr Ryan ")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email == actual_emailp5 and password == actual_passwordp5:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Miss Nina")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email == actual_emailp6 and password == actual_passwordp6:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr Klaus") 
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/")
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    pass
