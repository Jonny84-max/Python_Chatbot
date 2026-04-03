import datetime  # to get current date and time
import streamlit as st  # to create the chatbot interface

# simple function that takes user's name and responds
def Simple_chatbot(name):
    wat = datetime.timezone(datetime.timedelta(hours=1))  # set timezone to West Africa Time (UTC+1)
    now = datetime.datetime.now(wat) # get current time in WAT
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%I:%M %p')
    return f"Nice to meet you, {name}! Today's date is {date} and the current time in WAT is {time}." # return greeting + current date and time

# Streamlit interface
st.title("Python_Chatbot")
st.write("A simple chatbot that greets you and reminds you today's date and time in WAT.")

name = st.text_input("Hello! What is your name?")   # Get user input

if st.button("Say Hello") # Respond when button is pressed
    response = Simple_chatbot(name)
    st.text(response)  # chatbot reply
