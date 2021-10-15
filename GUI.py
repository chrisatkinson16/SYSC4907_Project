# SYSC 4907 IOT project
# @description For the GUI implementation of Smart Office for User Safety and Comfort
# @author Kevin Belanger 101121709
# @version Version 1, October 15th 2021

# Import statements
from tkinter import *
from tkinter import ttk
from Server import checkOccupancy, raiseTemp, temp, userName

# Sets our temperature value to a string which is read from the Server class.
temp = str(temp)

# Creates the window with title "Smart Office for User Safety and Comfort".
window = Tk()
window.geometry("540x280")
window.title("Smart Office for User Safety and Comfort")
tab_control = ttk.Notebook(window)


# A function to create a tab for the Sunflower plant type with data comparisons.
def Start():
    # A list for displaying data comparisons.
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Office Data')
    lbl1 = Label(tab1, text='User: ')
    lbl1.grid(column=0, row=0)
    lbl1 = Label(tab1, text=userName[0])
    lbl1.grid(column=1, row=0)
    lbl1 = Label(tab1, text='Occupancy: ')
    lbl1.grid(column=0, row=1)
    lbl1 = Label(tab1, text=checkOccupancy(0))
    lbl1.grid(column=1, row=1)
    lbl1 = Label(tab1, text='Action: ')
    lbl1.grid(column=0, row=2)
    lbl1 = Label(tab1, text=raiseTemp(0))
    lbl1.grid(column=1, row=2)
    lbl1 = Label(tab1, text='Temperature: ')
    lbl1.grid(column=0, row=3)
    lbl1 = Label(tab1, text=temp)
    lbl1.grid(column=1, row=3)


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Start", command=Start)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Start:", menu=filemenu)
window.config(menu=menubar)


# Executes pop up of window
tab_control.pack(expand=1, fill='both')
window.mainloop()

