from guizero import *

def count():
    chars.value = len(name.value)

def say_hello():
    message.value = "Hello"

def goodbye():
    message.destroy()

app = App(title="What's your name?")
message = Text(app, text="Enter your name!")
name = TextBox(app, command=count)
destroy = PushButton(app, text="Destroy", command=goodbye)

chars = Text(app)
button = PushButton(app, text="Press me", command=say_hello)
app.display()