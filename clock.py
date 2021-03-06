from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import time
import calendar
import datetime
h = 0
m= 0
s = 0
t = "am"
bgColor="Black"
fgColor="Blue"
bgLabColor="Black"
def current_time(h,m,s,t):
    seconds = calendar.timegm(time.gmtime())
    current_seconds = seconds % 60
    minutes = seconds // 60
    current_minutes= minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    #set the time zone 
    current_hour = current_hour - 6
    
    if current_hour >=12:
        tag="PM"
    else:
        tag="AM"
    a = str(h)+":"+str(m)+":"+str(s)+t
    #format the output
    timex = str(current_hour)+":"+ str(current_minutes)+":"+str( current_seconds)+tag
    if timex == a:
        beep()
    #xreturn the output
    return timex

def beep():
    winsound.Beep(540,8000)
    
def quit(*args):
    root.destroy()

def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    # Show the time
    txt.set(time)
    # Trigger the tick after 1000ms
    root.after(1000, show_time)
# Use tkinter lib for showing the clock
def get_alarm(*args):
    global h 
    h = input("set hour")
    global m
    m = input("set min")
    global s
    s = input("set sec")
    global t
    t = input("am or pm").upper()
def change_color(*args):
    global bgColor
    global fgColor
    global bgLabColor
    bgColor = input("what color do you want the background").title()
    fgColor = input("what color do you want the Clock text").title()
    bgLabColor = bgColor
    
root = Tk()
root.attributes("-fullscreen", False)
root.configure(background=bgColor)
root.bind("x", quit)
root.bind("a",get_alarm)
root.bind("c",change_color)
root.after(1000, show_time)
fnt = font.Font(family='Helvetica', size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground=fgColor, background=bgLabColor)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()
