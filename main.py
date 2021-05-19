#Made by Christopher Hatton (558)

# -*-coding: utf-8-*-

from tkinter import *            #for Tk window
import tkinter as tk             #to make Frame
from sys import platform         #to make sure that the os is win32
import ctypes                    #to make sure that the screen size is large enough
import os                        #to allow help button open help web page

name = "Christopher's Caclulator"

def f_main():

    root = Tk()

    root.title(name) 
    equation = ['']

    def on_click_1():
        equation[0] = ''.join((equation[0],'1'))
        answer.configure(text = equation[0])
    def on_click_2():
        equation[0] = ''.join((equation[0],'2'))
        answer.configure(text = equation[0])
    def on_click_3():
        equation[0] = ''.join((equation[0],'3'))
        answer.configure(text = equation[0])
    def on_click_4():
        equation[0] = ''.join((equation[0],'4'))
        answer.configure(text = equation[0])
    def on_click_5():
        equation[0] = ''.join((equation[0],'5'))
        answer.configure(text = equation[0])
    def on_click_6():
        equation[0] = ''.join((equation[0],'6'))
        answer.configure(text = equation[0])
    def on_click_7():
        equation[0] = ''.join((equation[0],'7'))
        answer.configure(text = equation[0])
    def on_click_8():
        equation[0] = ''.join((equation[0],'8'))
        answer.configure(text = equation[0])
    def on_click_9():
        equation[0] = ''.join((equation[0],'9'))
        answer.configure(text = equation[0])
    def on_click_0():
        equation[0] = ''.join((equation[0],'0'))
        answer.configure(text = equation[0])
    def on_click_decimal():
        equation[0] = ''.join((equation[0],'.'))
        answer.configure(text = equation[0])

    def on_click_division():
        equation[0] = ''.join((equation[0],'÷'))
        answer.configure(text = equation[0])
    def on_click_times():
        equation[0] = ''.join((equation[0],'x'))
        answer.configure(text = equation[0])
    def on_click_substract():
        equation[0] = ''.join((equation[0],'-'))
        answer.configure(text = equation[0])
    def on_click_add():
        equation[0] = ''.join((equation[0],'+'))
        answer.configure(text = equation[0])

    def on_click_delete():
        equation[0] = str((equation[0]))[:-1]
        answer.configure(text = equation[0])
    def on_click_open_bracket():
        equation[0] = ''.join((equation[0],'('))
        answer.configure(text = equation[0])
    def on_click_close_bracket():
        equation[0] = ''.join((equation[0],')'))
        answer.configure(text = equation[0])
    def on_click_equals():
        x = equation[0]
        x = x.replace('÷','/')
        x = x.replace('x','*')
        equation[0] = eval(x)
        answer.configure(text = equation[0])

    frame_buttons = tk.Frame(root)
    button_1 = Button(frame_buttons,text = '1',font = 'Helvetica 25 bold',command = on_click_1)
    button_1.grid(row = 0,column = 0,sticky = 'ew')
    button_2 = Button(frame_buttons,text = '2',font = 'Helvetica 25 bold',command = on_click_2)
    button_2.grid(row = 0,column = 1,sticky = 'ew')
    button_3 = Button(frame_buttons,text = '3',font = 'Helvetica 25 bold',command = on_click_3)
    button_3.grid(row = 0,column = 2,sticky = 'ew')
    button_4 = Button(frame_buttons,text = '4',font = 'Helvetica 25 bold',command = on_click_4)
    button_4.grid(row = 1,column = 0,sticky = 'ew')
    button_5 = Button(frame_buttons,text = '5',font = 'Helvetica 25 bold',command = on_click_5)
    button_5.grid(row = 1,column = 1,sticky = 'ew')
    button_6 = Button(frame_buttons,text = '6',font = 'Helvetica 25 bold',command = on_click_6)
    button_6.grid(row = 1,column = 2,sticky = 'ew')
    button_7 = Button(frame_buttons,text = '7',font = 'Helvetica 25 bold',command = on_click_7)
    button_7.grid(row = 2,column = 0,sticky = 'ew')
    button_8 = Button(frame_buttons,text = '8',font = 'Helvetica 25 bold',command = on_click_8)
    button_8.grid(row = 2,column = 1,sticky = 'ew')
    button_9 = Button(frame_buttons,text = '9',font = 'Helvetica 25 bold',command = on_click_9)
    button_9.grid(row = 2,column = 2,sticky = 'ew')
    button_0 = Button(frame_buttons,text = '0',font = 'Helvetica 25 bold',command = on_click_0)
    button_0.grid(row = 3,column = 0,sticky = 'ew')
    button_decimal = Button(frame_buttons,text = '.',font = 'Helvetica 25 bold',command = on_click_decimal)
    button_decimal.grid(row = 3,column = 1,sticky = 'ew')

    division = Button(frame_buttons,text = '÷',font = 'Helvetica 25 bold',command = on_click_division)
    division.grid(row = 0,column = 3,sticky = 'ew')
    times = Button(frame_buttons,text = 'x',font = 'Helvetica 25 bold',command = on_click_times)
    times.grid(row = 1,column = 3,sticky = 'ew')
    substract = Button(frame_buttons,text = '-',font = 'Helvetica 25 bold',command = on_click_substract)
    substract.grid(row = 2,column = 3,sticky = 'ew')
    add = Button(frame_buttons,text = '+',font = 'Helvetica 25 bold',command = on_click_add)
    add.grid(row = 3,column = 3,sticky = 'ew')

    delete = Button(frame_buttons,text = 'DEL',font = 'Helvetica 25 bold',command = on_click_delete)
    delete.grid(row = 0,column = 4,sticky = 'ew')
    open_bracket = Button(frame_buttons,text = '(',font = 'Helvetica 25 bold',command = on_click_open_bracket)
    open_bracket.grid(row = 1,column = 4,sticky = 'ew')
    close_bracket = Button(frame_buttons,text = ')',font = 'Helvetica 25 bold',command = on_click_close_bracket)
    close_bracket.grid(row = 2,column = 4,sticky = 'ew')
    equals = Button(frame_buttons,text = '=',font = 'Helvetica 25 bold',command = on_click_equals)
    equals.grid(row = 3,column = 4,sticky = 'ew')

    answer = Label(text = equation[0],font = 'Helvetica 25 bold')

    answer.grid(row = 0,column = 0)
    frame_buttons.grid(row = 1,column = 0)

    root.mainloop()

def small_monitor(): #displays error message for small screen
    root = Tk()
    warning_label = Label(text = 'Your screen is too small')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()

def f_linux(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Linux version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()  

def f_mac(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = 'Email Christopher@Christopher-Hatton.co.uk for the Mac version')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()  

def f_unknown_os(): #displays error message for wrong os
    root = Tk()
    warning_label = Label(text = name + ' is not available for your operating system.')
    warning_label.grid(row = 0,column = 0)
    root.mainloop()      

def run(): #if screen size big enough, run
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    if width >= 1280 and height >= 720:
        f_main()
    else:
        small_monitor()

if platform == 'win32': #if os = win32, run
    run()
elif platform == 'linux' or platform == 'linux32':
    f_linux() #if os = linux, asks the user to get the linux version
elif platform == 'darwin':
    f_mac() #if os = osx, asks the user to get the osx version
else:
    f_unknown_os() #for unknown os