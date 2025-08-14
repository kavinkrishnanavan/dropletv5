import streamlit as st # type: ignore
from datetime import datetime
import time
from PIL import Image # type: ignore
image = Image.open("Sep.png")

image2 = Image.open("Favi2.png")

st.set_page_config(layout="wide", page_title="LICA Login" , page_icon=image2)

col1, col2 = st.columns(2) # Creates two columns of equal width

with col1:

    try:
         # Replace with your image file path
        st.image(image, width=150) # You can adjust width and add a caption
    except FileNotFoundError:
        st.error("Image file not found. Please ensure 'your_image.png' is in the correct directory.")

with col2:

    st.markdown("<p style='text-align: right;'><b>🛢️ Liquid in Gas CarryOver Prediction (LICA Version 1.0)</b></p>", unsafe_allow_html=True)


st.markdown("---")

username = str(st.text_input("Username").split())
password = str(st.text_input("Password", type="password").split())

id = datetime.now()



users = {
    "['alice']": "['pass123']",
    "['bob']": "['123']"
}

def login(u , p):

    username = str(u)
    password = str(p)
    global id

    if username in users:
        if users[username] == password:
            print(f"Login successful for {username}!")

            user = st.success("Login Successful for User : {u}".format(u = username))

            time.sleep(1)

            user.empty()
            with open("u.txt", "w") as file:
                file.write(str(datetime.now()))
            
            page = st.page_link("pages\gogo.py", label="Click to go to Main Application", icon="🛢️")
            progress_text = "Portal expires in 10 seconds for Security Measures"
            my_bar = st.progress(0, text=progress_text)
            
            for i in range(100):

                my_bar.progress(i + 1, text=progress_text)

                time.sleep(0.1)

            my_bar.empty()
            page.empty()
            st.error("Expired. Login Again")
            
        else:
            print("Incorrect password.")
            st.error("Wrong Username or Password")
    else:
        print("Username not found.")
        st.error("Wrong Username or Password")

if st.button("Login"):
    print("Pressed")
    login(username , password)