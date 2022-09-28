import streamlit as st
import streamlit_authenticator as stauth
from PIL import Image

st.title("WELCOME")

import streamlit as st
import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")
imageUrls = [
        "https://images.unsplash.com/photo-1522093007474-d86e9bf7ba6f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        "https://images.unsplash.com/photo-1610016302534-6f67f1c968d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1075&q=80",
        "https://images.unsplash.com/photo-1516550893923-42d28e5677af?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=872&q=80",
        "https://images.unsplash.com/photo-1541343672885-9be56236302a?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1528728329032-2972f65dfb3f?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1557744813-846c28d0d0db?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1118&q=80",
        "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1595867818082-083862f3d630?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1622214366189-72b19cc61597?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1558180077-09f158c76707?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        "https://images.unsplash.com/photo-1520106212299-d99c443e4568?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        "https://images.unsplash.com/photo-1534430480872-3498386e7856?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1571317084911-8899d61cc464?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        "https://images.unsplash.com/photo-1624704765325-fd4868c9702e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
    ]
selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

if selectedImageUrl is not None:
    st.image(selectedImageUrl)



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaperaccess.com/full/2344101.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def doc():
    st.write("Your Patients are:\n")
    st.markdown("- Reenu Sivadarshini ---> @depressingmsgs")
    st.markdown("- Riya --->@riya68881")
    st.markdown("- Jack --->@Jackkk988")
def doc1():
    st.write("Your Patients are:\n")
    st.markdown("- Ryan---> @ryan3089")
    st.markdown("- Nina --->@Nina12282")
    st.markdown("- Klaus --->@@klaustoon")


st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

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

actual_emailp6 = "pat_klaus@gmail.com"
actual_passwordp6 = "pat_klaus"

# Insert a form in the container
with placeholder.form("login"):   
    st.title("Enter your credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

    
    
    
if submit and email == actual_emaild1 and password == actual_passwordd1:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SHARMELEE KUMAR ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
    doc()
elif submit and email == actual_emaild2 and password == actual_passwordd2:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SHERINA CARMEL ") 
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
    doc()

elif submit and email == actual_emaild3 and password == actual_passwordd3:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. SAMEERA SHAMMA ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
    doc1()
    
elif submit and email == actual_emaild4 and password == actual_passwordd4:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Dr. GLADIN  ")
    st.write("https://reenu123456-tweet-analyzer-app-odaytp.streamlitapp.com/ ")
    doc1()
    
elif submit and email == actual_emailp1 and password == actual_passwordp1:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Miss Reenu Sivadarshini M ")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
    
elif submit and email == actual_emailp2 and password == actual_passwordp2:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mrs Riya")   
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
elif submit and email == actual_emailp3 and password == actual_passwordp3:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr Jack")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
elif submit and email == actual_emailp4 and password == actual_passwordp4:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr Ryan ")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
elif submit and email == actual_emailp5 and password == actual_passwordp5:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Miss Nina")
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
elif submit and email == actual_emailp6 and password == actual_passwordp6:
    placeholder.empty()
    st.success("Login successful")
    st.write("Welcome Mr. KLAUS ") 
    st.write("https://reenusivadarshini-chat-streamlit-ur01z7.streamlitapp.com/ ")
    
elif submit and email != actual_email and password != actual_password:
    st.write("Login failed")
else:
    pass
