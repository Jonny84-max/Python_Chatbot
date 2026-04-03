import datetime  # to get current date and time
import gradio as gr  # to create the chatbot interface

# simple function that takes user's name and responds
def Simple_chatbot(name):
    wat = datetime.timezone(datetime.timedelta(hours=1))  # set timezone to West Africa Time (UTC+1)
    now = datetime.datetime.now(wat) # get current time in WAT
    date = now.strftime('%B %d, %Y')
    time = now.strftime('%I:%M %p')
    return f"Nice to meet you, {name}! Today's date is {date} and the current time in WAT is {time}." # return greeting + current date and time

# build the interface
iface = gr.Interface(
    fn=Simple_chatbot,  # function to run
    inputs=gr.Textbox(label="Hello! What is your name?"),  # user input
    outputs=gr.Textbox(label="Response"),  # chatbot reply
    title="Python_Chatbot",
    description="A simple chatbot that greets you and reminds you today's date and time in WAT."
)

iface.launch()  # lunch the app
