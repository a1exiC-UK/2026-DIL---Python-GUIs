from guizero import *

def change_message():
    message.value = "You pressed the button!"

app = App(title="Hello World")
message = Text(app, text="Wilkommen!")
button = PushButton(app, text="Press me", command=change_message)

app.display()