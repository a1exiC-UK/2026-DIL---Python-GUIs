from guizero import *

app = App(title="DIL Week 8/9")

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="GUI DIL (Week 8/9)")

content_box = Box(app, align="top", width="fill", border=True)
Text(content_box, text="Enter your details")

form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)

Text(form_box, grid=[0, 0], text="Enter your forename: ", align="right")
forename = TextBox(form_box, grid=[0, 1], width="fill")

Text(form_box, grid=[0, 2], text="Enter your surname: ", align="right")
surname = TextBox(form_box, grid=[0, 3], width="fill")

Text(form_box, grid=[0, 4], text=" ", align="right")

Text(form_box, grid=[1, 0], text="Select your gender: ", align="right")
gender = Combo(form_box, grid=[1, 1], options=["Male", "Female"], width="fill")

Text(form_box, grid=[2, 0], text="Enter your age: ", align="right")
age = TextBox(form_box, grid=[2, 1], width="fill")

result = Text(app, grid=[3, 0], text="")

def submit():
    result.value = (
        "Hello "
        + forename.value
        + " "
        + surname.value
        + ", you are a "
        + gender.value
        + " and you are "
        + age.value
        + " years old."
    )

PushButton(app, text="Submit", command=submit)

app.display()