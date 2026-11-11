from guizero import *

def say_goodbye(firstname, surname):
    text.value = firstname + " " + surname

app = App()
text = Text(app)
button = PushButton(app, command=say_goodbye, args=['John', 'Doe'])
app.display()