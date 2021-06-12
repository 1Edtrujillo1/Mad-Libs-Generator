# Test Module ----
# Verify that module is installed:
# # import tkinter
# # tkinter._test()
# Verify the version:
# tkinter.Tcl().eval('info patchlevel')

# Import Modules ----
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('ED Mad Libs Generator')
Label(master = root, text = 'Mad Libs Generator \n Have Fun', font = 'arial 20 bold').pack()
Label(master = root, text = 'Click Ant One :', font = 'arial 15 bold').place(x = 40, y = 80)