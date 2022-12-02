import tkinter as tk
import ast
import types
import inspect

from tk_tools_ext import *




container = {}
important_var = {}

Tester = Testme()
Tester.container = container
Tester.important_var = important_var

notsure = {}
for func in dir(Tester):
    if callable(getattr(Tester, func)) and not func.startswith("__"):
        notsure.update({func: getattr(Tester, func)})

for j in notsure:
    important_var.update({j: ""})


"""_tkinter.TclError: wrong # args: should be "wm attributes window 
?-alpha ?double?? up down/increase decrease
?-transparentcolor ?color?? up down/increase decrease
?-disabled ?bool?? done
?-fullscreen ?bool?? done
?-toolwindow ?bool?? done
?-topmost ?bool?? done
"""

def destroy_window():
    if len(container) == 2:
        container.get(2).destroy()
        container.pop(2)
    else:
        pass

def gui1():
    root1 = tk.Tk()
    container.update({1: root1})

def gui2():
    root2 = tk.Tk()
    container.update({2: root2})
    important_var.update({"width": container.get(2).winfo_width(), "height": container.get(2).winfo_height()})
    print(important_var)

def create_new():
    if len(container) == 1:
        root2 = tk.Tk()
        container.update({2: root2})
        root2.configure()
        important_var.update({"width": container.get(2).winfo_width(), "height": container.get(2).winfo_height()})
        print(important_var)
    else:
        pass

def tools(wow1):
    try:
        wow1.call("wm", "attributes", ".", "?")
    except Exception as e:
        e = e
        print(e)
    tk.Button(wow1, text='Destroy', bd='5',
              command=lambda: destroy_window()).pack()
    tk.Button(wow1, text='Create', bd='5',
              command=lambda: create_new()).pack()
    for i in notsure:
        tk.Button(wow1, text=i, bd='5', command=notsure.get(i)).pack()


gui2()
gui1()
tools(container.get(1))

print(container)
container.get(
    1).mainloop()  # https://stackoverflow.com/questions/48045401/why-are-multiple-instances-of-tk-discouraged/69062053#69062053
