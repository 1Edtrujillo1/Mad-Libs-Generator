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
Label(master=root, text='Mad Libs Generator \n Have Fun',
      font='arial 20 bold').pack()
Label(master=root, text='Click Ant One :',
      font='arial 15 bold').place(x=40, y=80)


def madlib1():
    animals = input('Enter an animal name: ')
    profession = input('Enter a profession name: ')
    cloth = input('Enter a piece of cloth name: ')
    things = input('Enter a thing name: ')
    name = input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('food name: ')

    print('Say ' + food + ', the photographer said as the camera flashed! ' +
          name + ' and I had gone to ' + place + ' to get our photos taken on my birthday.' +
          'The first photo we really wanted was a picture of us dressed as ' + animals +
          ' pretending to be a ' + profession + '. When we saw the second photo,' +
          'It was exactly what I wanted. We both looked like ' + things + ' wearing ' +
          cloth + ' and ' + verb + ' --exactly what I had in mind.')


Button(root,
       text='The Photographer',
       font='arial 15',
       command=madlib1,
       bg='ghost white').place(x=60, y=120)

root.mainloop()
