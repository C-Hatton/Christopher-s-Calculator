#Made by Christopher Hatton (558)

# -*-coding: utf-8-*-

from tkinter import *            #for Tk window
import tkinter as tk             #to make Frame
from sys import platform         #to make sure that the os is win32
import ctypes                    #to make sure that the screen size is large enough

name = "Christopher's Caclulator"

def f_main():

    root = Tk()

    root.title(name) 
    root.resizable(False, False) 
    equation = ['']
    font_style = 'Helvetica 25 bold'
    button_background = 'black'
    button_foreground = 'cyan'
    answer_background = 'white'
    answer_foreground = 'black'

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
        equation[0] = ((equation[0]))[:-1]
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
        equation[0] = str(eval(x))
        answer.configure(text = equation[0])

    def on_click_clear():
        equation[0] = ''
        answer.configure(text = equation[0])
        
    def on_press_1(event):
        equation[0] = ''.join((equation[0],'1'))
        answer.configure(text = equation[0])
    def on_press_2(event):
        equation[0] = ''.join((equation[0],'2'))
        answer.configure(text = equation[0])
    def on_press_3(event):
        equation[0] = ''.join((equation[0],'3'))
        answer.configure(text = equation[0])
    def on_press_4(event):
        equation[0] = ''.join((equation[0],'4'))
        answer.configure(text = equation[0])
    def on_press_5(event):
        equation[0] = ''.join((equation[0],'5'))
        answer.configure(text = equation[0])
    def on_press_6(event):
        equation[0] = ''.join((equation[0],'6'))
        answer.configure(text = equation[0])
    def on_press_7(event):
        equation[0] = ''.join((equation[0],'7'))
        answer.configure(text = equation[0])
    def on_press_8(event):
        equation[0] = ''.join((equation[0],'8'))
        answer.configure(text = equation[0])
    def on_press_9(event):
        equation[0] = ''.join((equation[0],'9'))
        answer.configure(text = equation[0])
    def on_press_0(event):
        equation[0] = ''.join((equation[0],'0'))
        answer.configure(text = equation[0])
    def on_press_decimal(event):
        equation[0] = ''.join((equation[0],'.'))
        answer.configure(text = equation[0])

    def on_press_division(event):
        equation[0] = ''.join((equation[0],'÷'))
        answer.configure(text = equation[0])
    def on_press_times(event):
        equation[0] = ''.join((equation[0],'x'))
        answer.configure(text = equation[0])
    def on_press_subtract(event):
        equation[0] = ''.join((equation[0],'-'))
        answer.configure(text = equation[0])
    def on_press_add(event):
        equation[0] = ''.join((equation[0],'+'))
        answer.configure(text = equation[0])

    def on_press_delete(event):
        equation[0] = ((equation[0]))[:-1]
        answer.configure(text = equation[0])
    def on_press_open_bracket(event):
        equation[0] = ''.join((equation[0],'('))
        answer.configure(text = equation[0])
    def on_press_close_bracket(event):
        equation[0] = ''.join((equation[0],')'))
        answer.configure(text = equation[0])
    def on_press_equals(event):
        x = equation[0]
        x = x.replace('÷','/')
        x = x.replace('x','*')
        equation[0] = str(eval(x))
        answer.configure(text = equation[0])

    def on_press_clear(event):
        equation[0] = ''
        answer.configure(text = equation[0])

    frame_buttons = tk.Frame(root)
    button_1 = Button(frame_buttons,text = '1',font = font_style,command = on_click_1,bg = button_background,fg = button_foreground)
    button_1.grid(row = 0,column = 0,sticky = 'ew')
    button_2 = Button(frame_buttons,text = '2',font = font_style,command = on_click_2,bg = button_background,fg = button_foreground)
    button_2.grid(row = 0,column = 1,sticky = 'ew')
    button_3 = Button(frame_buttons,text = '3',font = font_style,command = on_click_3,bg = button_background,fg = button_foreground)
    button_3.grid(row = 0,column = 2,sticky = 'ew')
    button_4 = Button(frame_buttons,text = '4',font = font_style,command = on_click_4,bg = button_background,fg = button_foreground)
    button_4.grid(row = 1,column = 0,sticky = 'ew')
    button_5 = Button(frame_buttons,text = '5',font = font_style,command = on_click_5,bg = button_background,fg = button_foreground)
    button_5.grid(row = 1,column = 1,sticky = 'ew')
    button_6 = Button(frame_buttons,text = '6',font = font_style,command = on_click_6,bg = button_background,fg = button_foreground)
    button_6.grid(row = 1,column = 2,sticky = 'ew')
    button_7 = Button(frame_buttons,text = '7',font = font_style,command = on_click_7,bg = button_background,fg = button_foreground)
    button_7.grid(row = 2,column = 0,sticky = 'ew')
    button_8 = Button(frame_buttons,text = '8',font = font_style,command = on_click_8,bg = button_background,fg = button_foreground)
    button_8.grid(row = 2,column = 1,sticky = 'ew')
    button_9 = Button(frame_buttons,text = '9',font = font_style,command = on_click_9,bg = button_background,fg = button_foreground)
    button_9.grid(row = 2,column = 2,sticky = 'ew')
    button_0 = Button(frame_buttons,text = '0',font = font_style,command = on_click_0,bg = button_background,fg = button_foreground)
    button_0.grid(row = 3,column = 0,sticky = 'ew')
    fill_1 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_1.grid(row = 3,column = 2,sticky = 'nsew')
    button_decimal = Button(frame_buttons,text = '.',font = font_style,command = on_click_decimal,bg = button_background,fg = button_foreground)
    button_decimal.grid(row = 3,column = 1,sticky = 'ew')

    division = Button(frame_buttons,text = '÷',font = font_style,command = on_click_division,bg = button_background,fg = button_foreground)
    division.grid(row = 0,column = 3,sticky = 'ew')
    times = Button(frame_buttons,text = 'x',font = font_style,command = on_click_times,bg = button_background,fg = button_foreground)
    times.grid(row = 1,column = 3,sticky = 'ew')
    substract = Button(frame_buttons,text = '-',font = font_style,command = on_click_substract,bg = button_background,fg = button_foreground)
    substract.grid(row = 2,column = 3,sticky = 'ew')
    add = Button(frame_buttons,text = '+',font = font_style,command = on_click_add,bg = button_background,fg = button_foreground)
    add.grid(row = 3,column = 3,sticky = 'ew')

    delete = Button(frame_buttons,text = 'DEL',font = font_style,command = on_click_delete,bg = button_background,fg = button_foreground)
    delete.grid(row = 0,column = 4,sticky = 'ew')
    open_bracket = Button(frame_buttons,text = '(',font = font_style,command = on_click_open_bracket,bg = button_background,fg = button_foreground)
    open_bracket.grid(row = 1,column = 4,sticky = 'ew')
    close_bracket = Button(frame_buttons,text = ')',font = font_style,command = on_click_close_bracket,bg = button_background,fg = button_foreground)
    close_bracket.grid(row = 2,column = 4,sticky = 'ew')
    equals = Button(frame_buttons,text = '=',font = font_style,command = on_click_equals,bg = button_background,fg = button_foreground)
    equals.grid(row = 3,column = 4,sticky = 'ew')

    clear = Button(frame_buttons,text = 'CL',font = font_style,command = on_click_clear,bg = button_background,fg = button_foreground)
    clear.grid(row = 0,column = 5,sticky = 'ew')
        fill_2 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_2.grid(row = 1,column = 5,sticky = 'nsew')
    fill_3 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_3.grid(row = 2,column = 5,sticky = 'nsew')
    fill_4 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_4.grid(row = 3,column = 5,sticky = 'nsew')
    
    answer = Label(text = equation[0],font = font_style,bg = answer_background,fg = answer_foreground)

    answer.grid(row = 0,column = 0,sticky = 'ew')
    frame_buttons.grid(row = 1,column = 0)
    
    root.bind('1', on_press_1)
    root.bind('2', on_press_2)
    root.bind('3', on_press_3)
    root.bind('4', on_press_4)
    root.bind('5', on_press_5)
    root.bind('6', on_press_6)
    root.bind('7', on_press_7)
    root.bind('8', on_press_8)
    root.bind('9', on_press_9)
    root.bind('0', on_press_0)
    root.bind('.',on_press_decimal)

    root.bind('/', on_press_division)
    root.bind('*', on_press_times)
    root.bind('-', on_press_subtract)
    root.bind('+', on_press_add)

    root.bind('<BackSpace>', on_press_delete)
    root.bind('(', on_press_open_bracket)
    root.bind(')', on_press_close_bracket)
    root.bind('=', on_press_equals)
    root.bind('<Return>', on_press_equals)

    root.bind('c', on_press_clear)

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
