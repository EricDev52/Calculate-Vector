import tkinter as tk
from math import *

window = tk.Tk()   # Start Tkinter

window.title("Calculate Vector")

canvas = tk.Canvas(window, width=400, height=500)   # Tkinter window
canvas.pack()
canvas.create_rectangle(50, 150, 350, 450, fill='#cccccc')
canvas.create_line((200,170),(200,430),fill="blue",width=2) # Y-Axis
canvas.create_line((70,300),(330,300),fill="red",width=2) # X-Axis
canvas.create_line((200,170),(190,185),fill="blue",width=2) # Arrow Y-Axis Left
canvas.create_line((200,170),(210,185),fill="blue",width=2) # Arrow Y-Axis Right
canvas.create_line((315,290),(330,300),fill="red",width=2) # Arrow X-Axis Top
canvas.create_line((315,310),(330,300),fill="red",width=2) # Arrow X-Axis Bottom
canvas.create_text(340,300,text="X") # X axis text
canvas.create_text(200,160,text="Y") # Y axis text

canvas.create_text((100, 20), text="X Position")   #Input windows
XInput = tk.Entry (window)
canvas.create_window(200, 20, window=XInput)
canvas.create_text((100, 40), text="Y Position")
YInput = tk.Entry (window) 
canvas.create_window(200, 40, window=YInput)
canvas.create_text((100, 60), text="Vector Length")
LengthInput = tk.Entry (window) 
canvas.create_window(200, 60, window=LengthInput)
canvas.create_text((100, 80), text="Angle Degree")
DegreeInput = tk.Entry (window) 
canvas.create_window(200, 80, window=DegreeInput)
canvas.create_text((100, 100), text="Angle Radiant")
RadiantInput = tk.Entry (window) 
canvas.create_window(200, 100, window=RadiantInput)

TempCanvas = []
def UpdateUI(X,Y,Length,Degree,Radiant):
    for Element in TempCanvas:
        canvas.delete(Element)
    if not (X == 0 and Y == 0):
        TempCanvas.append(canvas.create_line((200,300),((100*cos(atan2(Y,X)))+200,(100*sin(atan2(-Y,X)))+300),fill="black",width=3)) # Display vector direction
        TempCanvas.append(canvas.create_text(((100*cos(atan2(Y,X)))+200,(100*sin(atan2(-Y,X)))+290),text="(" + str(round(X,3)) + "," + str(round(Y,3)) + ")")) # Display vector position
    else:
        TempCanvas.append(canvas.create_text(230,280,text="(" + str(round(X,3)) + "," + str(round(Y,3)) + ")")) # If youve entered 0 and 0
    TempCanvas.append(canvas.create_text(200,465,text="Length: " + str(round(Length,3))))
    TempCanvas.append(canvas.create_text(200,485,text="Angle Degree: " + str(round(Degree,3)) + "°"))

    ClearInputs()

    XInput.insert(0,round(X,3))    # Input values in entry windows
    YInput.insert(0,round(Y,3))
    LengthInput.insert(0,round(Length,3))
    DegreeInput.insert(0,round(Degree,3))
    RadiantInput.insert(0,round(Radiant,3))

def CalculateDirection(X,Y):
    Radiant = atan2(Y,X)
    if Radiant < 0:
        Radiant = 2*pi + Radiant
    UpdateUI(X,Y,pow(pow(X,2)+pow(Y,2),0.5),Radiant*180/pi,Radiant)

def CalculatePosition (Length,Radiant):
    UpdateUI(Length*cos(Radiant),Length*sin(Radiant),Length,Radiant*180/pi,Radiant)


def TestInput():   # Find out what we want to calculate
    if not (XInput.get() == "" or YInput.get() == ""):
        CalculateDirection(float(XInput.get()),float(YInput.get()))
    else:
        if RadiantInput.get() == "":
            CalculatePosition(float(LengthInput.get()),float(DegreeInput.get())*pi/180)   # If we entered only degree or only radiant
        else:
            CalculatePosition(float(LengthInput.get()),float(RadiantInput.get()))

def ClearInputs():
    XInput.delete(0,len(XInput.get()))
    YInput.delete(0,len(YInput.get()))
    LengthInput.delete(0,len(LengthInput.get()))
    DegreeInput.delete(0,len(DegreeInput.get()))
    RadiantInput.delete(0,len(RadiantInput.get()))

def enter(event):
    TestInput()
window.bind("<Return>", enter)  # So that we can also calculate on enter key
CalculateButton = tk.Button(text='Calculate (Enter)', command=TestInput)   # Display Calculate button and on click do TestInput () function
canvas.create_window(200, 130, window=CalculateButton)
def delete(event):
    ClearInputs()
window.bind("<Delete>", delete)  # So that we can also clear on delete key
ClearButton = tk.Button(text='Clear (Delete)', command=ClearInputs)   # Clear inputs button
canvas.create_window(100, 130, window=ClearButton)

window.mainloop()