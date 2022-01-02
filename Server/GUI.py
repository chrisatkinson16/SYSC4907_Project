# SYSC 4907 IOT project
# @description For the GUI implementation of Smart Office for User Safety and Comfort
# @author Kevin Belanger 101121709
# @version Version 1, October 15th 2021

# Import statements
from tkinter import *
from tkinter import ttk

# from Server import checkOccupancy, raiseTemp, temp, userName

checkOccupancy = 10
raiseTemp = 0
temp = 21
userName = 'Kevin Belanger'
role = 'Administrator'
luminescence = 1
action = ['Turning lights off', 'Turning on AC', 'Turning off heat']


# Sets our temperature value to a string which is read from the Server class.
temp = str(temp)

# Creates the window with title "Smart Office for User Safety and Comfort".
window = Tk()
window.attributes("-fullscreen", True)
window.title("Smart Office for User Safety and Comfort")
tab_control = ttk.Notebook(window)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Options:", menu=filemenu)
window.config(menu=menubar)


def userInfo():
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='User Information')
    lbl1 = Label(tab1, text='User: ', font=("Arial", 25))
    lbl1.grid(column=0, row=0, padx=50, pady=50)
    lbl1 = Label(tab1, text=userName, font=("Arial", 25))
    lbl1.grid(column=1, row=0, padx=50, pady=50)
    lbl2 = Label(tab1, text='Role: ', font=("Arial", 25))
    lbl2.grid(column=0, row=1, padx=50, pady=50)
    lbl2 = Label(tab1, text=role, font=("Arial", 25))
    lbl2.grid(column=1, row=1, padx=50, pady=50)


def officeData():
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Office Data')
    lbl1 = Label(tab2, text='Occupancy: ', font=("Arial", 25))
    lbl1.grid(column=0, row=0, padx=50, pady=50)
    lbl1 = Label(tab2, text=checkOccupancy, font=("Arial", 25))
    lbl1.grid(column=1, row=0, padx=50, pady=50)
    lbl2 = Label(tab2, text='Temperature: ', font=("Arial", 25))
    lbl2.grid(column=0, row=1, padx=50, pady=50)
    lbl2 = Label(tab2, text=temp, font=("Arial", 25))
    lbl2.grid(column=1, row=1, padx=50, pady=50)
    lbl3 = Label(tab2, text='Luminescence: ', font=("Arial", 25))
    lbl3.grid(column=0, row=2, padx=50, pady=50)
    lbl3 = Label(tab2, text=luminescence, font=("Arial", 25))
    lbl3.grid(column=1, row=2, padx=50, pady=50)


def recommendations():
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='Recommendations')
    lbl1 = Label(tab3, text='Action being carried out: ', font=("Arial", 25))
    lbl1.grid(column=0, row=0, padx=50, pady=50)
    lbl2 = Label(tab3, text=action[0], font=("Arial", 25))
    lbl2.grid(column=1, row=0, padx=50, pady=50)
    btn = Button(tab3, text='Override this recommendation', command=lambda: override(action[0]), font=("Arial", 25))
    btn.grid(column=2, row=0, padx=50, pady=50, ipadx=10)
    lbl3 = Label(tab3, text='Action being carried out: ', font=("Arial", 25))
    lbl3.grid(column=0, row=1, padx=50, pady=50)
    lbl4 = Label(tab3, text=action[1], font=("Arial", 25))
    lbl4.grid(column=1, row=1, padx=50, pady=50)
    btn = Button(tab3, text='Override this recommendation', command=lambda: override(action[1]), font=("Arial", 25))
    btn.grid(column=2, row=1, padx=50, pady=50, ipadx=10)
    lbl5 = Label(tab3, text='Action being carried out: ', font=("Arial", 25))
    lbl5.grid(column=0, row=2, padx=50, pady=50)
    lbl6 = Label(tab3, text=action[2], font=("Arial", 25))
    lbl6.grid(column=1, row=2, padx=50, pady=50)
    btn = Button(tab3, text='Override this recommendation', command=lambda: override(action[2]), font=("Arial", 25))
    btn.grid(column=2, row=2, padx=50, pady=50, ipadx=10)


def override(act):
    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab4, text='Override')
    lbl1 = Label(tab4, text='Override Granted for:         ' + act, font=("Arial", 25))
    lbl1.grid(column=0, row=0, padx=50, pady=50)


# Executes pop up of window
userInfo()
officeData()
recommendations()
tab_control.pack(expand=1, fill='both')
window.mainloop()
