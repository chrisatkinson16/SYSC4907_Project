# L1-F-4 Water plEase
# @description For the GUI implementation of Water plEase
# @author Kevin Belanger 101121709
# @version Version 5, December 4th 2020

# Import statements
from tkinter import *
from tkinter import ttk
from data_transmission import giveWater, givepHSuppliment, plantName, pH

# Sets our pH value to a string which is read from the data_transmission class.
pH = str(pH)

# Creates the window with title "Water plEase".
window = Tk()
window.geometry("250x110")
window.title("Water plEase")
tab_control = ttk.Notebook(window)

# A function to create a tab for the Sunflower plant type with data comparisons.
def Sunflower():
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Sunflower')
    lbl1 = Label(tab1, text='Plant type: ')
    lbl1.grid(column=0, row=0)
    lbl1 = Label(tab1, text=plantName[0])
    lbl1.grid(column=1, row=0)
    lbl1 = Label(tab1, text='Water status: ')
    lbl1.grid(column=0, row=1)
    lbl1 = Label(tab1, text=giveWater(0))
    lbl1.grid(column=1, row=1)
    lbl1 = Label(tab1, text='pH Status: ')
    lbl1.grid(column=0, row=2)
    lbl1 = Label(tab1, text=givepHSuppliment(0))
    lbl1.grid(column=1, row=2)
    lbl1 = Label(tab1, text='pH: ')
    lbl1.grid(column=0, row=3)
    lbl1 = Label(tab1, text=pH)
    lbl1.grid(column=1, row=3)

# A function to create a tab for the Tulip plant type with data comparisons.
def Tulip():
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Tulip')
    lbl2 = Label(tab2, text='Plant type: ')
    lbl2.grid(column=0, row=0)
    lbl2 = Label(tab2, text=plantName[1])
    lbl2.grid(column=1, row=0)
    lbl2 = Label(tab2, text='Water status: ')
    lbl2.grid(column=0, row=1)
    lbl2 = Label(tab2, text=giveWater(1))
    lbl2.grid(column=1, row=1)
    lbl2 = Label(tab2, text='pH Status: ')
    lbl2.grid(column=0, row=2)
    lbl2 = Label(tab2, text=givepHSuppliment(1))
    lbl2.grid(column=1, row=2)
    lbl2 = Label(tab2, text='pH: ')
    lbl2.grid(column=0, row=3)
    lbl2 = Label(tab2, text=pH)
    lbl2.grid(column=1, row=3)

# A function to create a tab for the Fern plant type with data comparisons.
def Fern():
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='Fern')
    lbl3 = Label(tab3, text='Plant type: ')
    lbl3.grid(column=0, row=0)
    lbl3 = Label(tab3, text=plantName[2])
    lbl3.grid(column=1, row=0)
    lbl3 = Label(tab3, text='Water status: ')
    lbl3.grid(column=0, row=1)
    lbl3 = Label(tab3, text=giveWater(2))
    lbl3.grid(column=1, row=1)
    lbl3 = Label(tab3, text='pH Status: ')
    lbl3.grid(column=0, row=2)
    lbl3 = Label(tab3, text=givepHSuppliment(2))
    lbl3.grid(column=1, row=2)
    lbl3 = Label(tab3, text='pH: ')
    lbl3.grid(column=0, row=3)
    lbl3 = Label(tab3, text=pH)
    lbl3.grid(column=1, row=3)

# A function to create a tab for the Aloe Vera plant type with data comparisons.
def AloeVera():
    tab4 = ttk.Frame(tab_control)
    tab_control.add(tab4, text='Aloe Vera')
    lbl4 = Label(tab4, text='Plant type: ')
    lbl4.grid(column=0, row=0)
    lbl4 = Label(tab4, text=plantName[3])
    lbl4.grid(column=1, row=0)
    lbl4 = Label(tab4, text='Water status: ')
    lbl4.grid(column=0, row=1)
    lbl4 = Label(tab4, text=giveWater(3))
    lbl4.grid(column=1, row=1)
    lbl4 = Label(tab4, text='pH Status: ')
    lbl4.grid(column=0, row=2)
    lbl4 = Label(tab4, text=givepHSuppliment(3))
    lbl4.grid(column=1, row=2)
    lbl4 = Label(tab4, text='pH: ')
    lbl4.grid(column=0, row=3)
    lbl4 = Label(tab4, text=pH)
    lbl4.grid(column=1, row=3)

# A function to create a tab for the Rose plant type with data comparisons.
def rose():
    tab5 = ttk.Frame(tab_control)
    tab_control.add(tab5, text='Rose')
    lbl5 = Label(tab5, text='Plant type: ')
    lbl5.grid(column=0, row=0)
    lbl5 = Label(tab5, text=plantName[4])
    lbl5.grid(column=1, row=0)
    lbl5 = Label(tab5, text='Water status: ')
    lbl5.grid(column=0, row=1)
    lbl5 = Label(tab5, text=giveWater(4))
    lbl5.grid(column=1, row=1)
    lbl5 = Label(tab5, text='pH Status: ')
    lbl5.grid(column=0, row=2)
    lbl5 = Label(tab5, text=givepHSuppliment(4))
    lbl5.grid(column=1, row=2)
    lbl5 = Label(tab5, text='pH: ')
    lbl5.grid(column=0, row=3)
    lbl5 = Label(tab5, text=pH)
    lbl5.grid(column=1, row=3)

# Creates menu for the window and gives each plant name and exit a function to open the respective plant data or exit.
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Sunflower", command=Sunflower)
filemenu.add_command(label="Tulip", command=Tulip)
filemenu.add_command(label="Fern", command=Fern)
filemenu.add_command(label="Aloe Vera", command=AloeVera)
filemenu.add_command(label="Rose", command=rose)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="Choose plant:", menu=filemenu)
window.config(menu=menubar)

# Executes pop up of window
tab_control.pack(expand=1, fill='both')
window.mainloop()
