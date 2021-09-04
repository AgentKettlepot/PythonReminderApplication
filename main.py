from calendar import c
from tkcalendar import Calendar
from tkinter import *
import tkinter as tk
from SendEmail import *
import time
import datetime
#GUI
def CreateGUI():
    global frame
    frame = tk.Tk()
    frame.geometry('800x730')
    color = '#dcf3fa'
    frame.config(bg = color)
    global ToAddr
    ToAddr = Label(frame, text='Who is the receiver of this reminder?', bg= color, font='bold')
    ToAddr.pack()
    global TextField
    TextField = Entry(frame, bg= color, relief = 'solid')
    TextField.pack() 
    global Reminder
    Reminder = Label(frame, text='What is the reminder?', bg= color, font='bold')
    Reminder.pack()
    global TextField1
    TextField1 = Entry(frame, bg= color, relief = "solid")
    TextField1.pack() 
    global TimeDate
    TimeDate = Label(frame, text='When is the event/reminder?', bg= color, font='bold')
    TimeDate.pack()
    global calendar
    curr_year = datetime.datetime.now().year
    curr_month = datetime.datetime.now().month
    calendar = Calendar(frame, selectmode = 'day',
               year = curr_year, month = curr_month)
    calendar.pack(fill="both", expand=True)
    global LargeMessage 
    LargeMessage= Label(frame, text="Longer message:")
    LargeMessage.pack()
    global TextField2
    TextField2 = Entry(frame, bg= color, width = 200, relief = "solid")
    TextField2.pack()   
    B = Button(frame, text = "OK", command = Function)
    B.pack()
    frame.mainloop()

def Function():
    if len(TextField.get()) ==0 or len(TextField1.get()) == 0 or len(calendar.get_date()) == 0:
        global ErrorMessage
        ErrorMessage = Label(frame, text = "Please input something in every field")
        ErrorMessage.pack()
    else:
        PassedTest()

def PassedTest():
    date = calendar.get_date()
    big_mess = TextField2.get()
    SendEmail (TextField.get(), TextField1.get(), date, big_mess)
    time.sleep(2)
    frame.destroy()


if __name__ == "__main__":
    CreateGUI()
