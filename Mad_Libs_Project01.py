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

    dic = list(dic.values())

    print('Say ' + dic[0] + ', the photographer said as the camera flashed! ' +
          dic[1] + ' and I had gone to ' + dic[2] + ' to get our photos taken on my birthday.' +
          'The first photo we really wanted was a picture of us dressed as ' + dic[3] +
          ' pretending to be a ' + dic[4] + '. When we saw the second photo,' +
          'It was exactly what I wanted. We both looked like ' + list(dic)[5] + ' wearing ' +
          dic[6] + ' and ' + dic[7] + ' --exactly what I had in mind.')


def madlib2():

    vars_inputs = ["person", "color", "foods", "adjective", "thing",
                   "place", "verb", "adverb", "food", "things"]

    inputs = [i + " name :"
              for i in ["Enter " + i
                        for i in ["a person", "a color", "food", "an adjective", "a thing",
                                  "a place", "a verb", "an adverb", "a food", "a thing"]]]

    dic = {}
    for i in range(0, len(vars_inputs)):
        dic[vars_inputs[i]] = input(inputs[i])

    dic = list(dic.values())

    print("Today we picked apple from " + dic[0] + "´s Orchard. I had no idea there" +
          " were so many different varieties of apples. I ate " + dic[1] + "apples straight" +
          " off the tree that tested like " + dic[2] + ". Then there was a " +
          dic[3] + " apple that looked like a " + dic[4] + ". When our bag were´" +
          "full, we went on a free ride to " + dic[5] + " and back. It ended at" +
          "a pile where we got to " + dic[6] + " " + dic[7] + ". I can hardly" +
          "wait to get home and cook with the apples. We are going to make apple" +
          dic[8] + " and " + dic[9] + " pies!")


Button(root,
       text='The Photographer',
       font='arial 15',
       command=madlib1,
       bg='ghost white').place(x=60, y=120)

Button(root,
       text='The Butterfly',
       font='arial 15',
       command=madlib2,
       bg='ghost white').place(x=70, y=180)

root.mainloop()
