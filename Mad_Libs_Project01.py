# Test Module ----
# Verify that module is installed:
# # import tkinter
# # tkinter._test()
# Verify the version:
# tkinter.Tcl().eval('info patchlevel')

# Import Modules ----
import numpy as np
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('ED Mad Libs Generator')
Label(master=root, text='Mad Libs Generator \n Have Fun',
      font='arial 20 bold').pack()
Label(master=root, text='Click Ant One :',
      font='arial 15 bold').place(x=40, y=80)


def madlib1():

    vars_inputs = ["food", "name",
                   "place", "animals",
                   "profession", "things",
                   "cloth", "verb"]

    inputs = ['food'] + ['Enter ' + i for i in ["a", "a place", "an animal",
                                                "a profession", "a thing", "a piece of cloth",
                                                'a verb in ing form: ']]
    inputs[0:-1] = [i + ' name: ' for i in inputs[0:-1]]

    dic = {}
    for i in range(0, len(vars_inputs)):
        dic[vars_inputs[i]] = input(inputs[i])

    print('Say ' + list(dic)[0] + ', the photographer said as the camera flashed! ' +
          list(dic)[1] + ' and I had gone to ' + list(dic)[2] + ' to get our photos taken on my birthday.' +
          'The first photo we really wanted was a picture of us dressed as ' + list(dic)[3] +
          ' pretending to be a ' + list(dic)[4] + '. When we saw the second photo,' +
          'It was exactly what I wanted. We both looked like ' + list(dic)[5] + ' wearing ' +
          list(dic)[6] + ' and ' + list(dic)[7] + ' --exactly what I had in mind.')


Button(root,
       text='The Photographer',
       font='arial 15',
       command=madlib1,
       bg='ghost white').place(x=60, y=120)

root.mainloop()
