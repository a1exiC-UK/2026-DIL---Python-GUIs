from guizero import *

def open_window():
    window.show(wait=True)

def close_window():
    window.hide()

app = App(title="Main Window")

window = Window(app, title="Second Window")
window.hide()

open = PushButton(app, text="Open", command=open_window)
close = PushButton(window, text="Close", command=close_window)

app.display()