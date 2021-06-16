# Test Module ----
# Verify that module is installed:
# # import tkinter
# # tkinter._test()
# Verify the version:
# tkinter.Tcl().eval('info patchlevel')

# 0.0 Import Modules ----
import numpy as np
from tkinter import *

# 1.0 Import script reference ----
from inputs_reference import vars_inputs, inputs, specific_dic


# 2.0 Dialog Box Generator ----

root = Tk()
root.geometry('300x300')
root.title('ED Mad Libs Generator')

list(map(lambda func, args: func(args),
         [lambda x: x.pack(), lambda x: x.place(x=40, y=80)],
         list(map(
             lambda text, font:
             Label(master=root, text=text, font=font),
             ['Mad Libs Generator \n Have Fun', 'Click Ant One :'],
             ['arial 20 bold', 'arial 15 bold']
         ))
         ))

# 3.0 Button commands ----


def madlib1():

    dic = specific_dic(vars=vars_inputs[0], elements=inputs[0])

    print('Say ' + dic[0] + ', the photographer said as the camera flashed! ' +
          dic[1] + ' and I had gone to ' + dic[2] + ' to get our photos taken on my birthday.' +
          'The first photo we really wanted was a picture of us dressed as ' + dic[3] +
          ' pretending to be a ' + dic[4] + '. When we saw the second photo,' +
          'It was exactly what I wanted. We both looked like ' + list(dic)[5] + ' wearing ' +
          dic[6] + ' and ' + dic[7] + ' --exactly what I had in mind.')


def madlib2():

    dic = specific_dic(vars=vars_inputs[1], elements=inputs[1])

    print("Today we picked apple from " + dic[0] + "´s Orchard. I had no idea there" +
          " were so many different varieties of apples. I ate " + dic[1] + "apples straight" +
          " off the tree that tested like " + dic[2] + ". Then there was a " +
          dic[3] + " apple that looked like a " + dic[4] + ". When our bag were´" +
          "full, we went on a free ride to " + dic[5] + " and back. It ended at" +
          "a pile where we got to " + dic[6] + " " + dic[7] + ". I can hardly" +
          "wait to get home and cook with the apples. We are going to make apple" +
          dic[8] + " and " + dic[9] + " pies!")

# 3.1 Buttons to execute commands ----


list(map(
    lambda text, command, x, y:
    Button(root,
           text=text,
           font='arial 15',
           command=command,
           bg='ghost white').place(x=x, y=y),
    ['The Photographer', 'The Butterfly'],
    [madlib1, madlib2],
    [60, 70],
    [120, 180]
))

# 4.0 Execution ----

root.mainloop()
