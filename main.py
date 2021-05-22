#Made by Christopher Hatton (558)

# -*-coding: utf-8-*-

from tkinter import *            #for Tk window
import tkinter as tk             #to make Frame
from sys import platform         #to make sure that the os is win32
import ctypes                    #to make sure that the screen size is large enough

name = "Christopher's Caclulator" #Name

def f_main():

    root = Tk()

    root.title(name) #Sets title
    root.resizable(False, False) #Stops user changing window size
    equation = [''] #Sets the equation variable
    
    #Sets the font:
    font_style = 'Helvetica 25 bold'
    button_background = 'lightgray'
    button_foreground = 'black'
    answer_background = 'lightgray'
    answer_foreground = 'black'


    #Functions:
    
    #Onclick

    #On click(numbers + decimal)

    #Onclick 1
    def on_click_1():
        equation[0] = ''.join((equation[0],'1')) #Adds 1 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 2
    def on_click_2():
        equation[0] = ''.join((equation[0],'2')) #Adds 2 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 3
    def on_click_3():
        equation[0] = ''.join((equation[0],'3')) #Adds 3 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 4
    def on_click_4():
        equation[0] = ''.join((equation[0],'4')) #Adds 4 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 5
    def on_click_5():
        equation[0] = ''.join((equation[0],'5')) #Adds 5 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 6
    def on_click_6():
        equation[0] = ''.join((equation[0],'6')) #Adds 6 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 7
    def on_click_7():
        equation[0] = ''.join((equation[0],'7')) #Adds 7 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 8
    def on_click_8():
        equation[0] = ''.join((equation[0],'8')) #Adds 8 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 9
    def on_click_9():
        equation[0] = ''.join((equation[0],'9')) #Adds 9 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick 0
    def on_click_0():
        equation[0] = ''.join((equation[0],'0')) #Adds 0 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick decimal
    def on_click_decimal():
        equation[0] = ''.join((equation[0],'.')) #Adds . to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this


    #Operators:

    #Onclick division
    def on_click_division():
        equation[0] = ''.join((equation[0],'÷')) #Adds ÷ to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick times
    def on_click_times():
        equation[0] = ''.join((equation[0],'x')) #Adds x to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick subtract
    def on_click_substract():
        equation[0] = ''.join((equation[0],'-')) #Adds - to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick add
    def on_click_add():
        equation[0] = ''.join((equation[0],'+')) #Adds + to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this


    #Delete, brackets and equals:

    #Onclick delete
    def on_click_delete():
        equation[0] = ((equation[0]))[:-1]       #Deletes the last character of the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick oepn bracket
    def on_click_open_bracket():
        equation[0] = ''.join((equation[0],'(')) #Adds ( to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick closed bracket
    def on_click_close_bracket():
        equation[0] = ''.join((equation[0],')')) #Adds ) to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onclick equals
    def on_click_equals():
        x = equation[0]
        x = x.replace('÷','/') #Changes the ÷ sign to /
        x = x.replace('x','*') #Changes the x sign to *
        x = x.replace('X','*') #Changes the x sign to *
        while True:
            try:
                equation[0] = str(eval(x)) #Solves the equation
            except SyntaxError:
                break
            else:
                answer.configure(text = equation[0]) #Configures the answer label to show this
                break


    #Right-most column:

    #Onclick clear
    def on_click_clear():
        equation[0] = '' #Deletes everything in the equation
        answer.configure(text = equation[0]) #Configures the answer label to show this
    

    #Keyboard inputs:

    #Onpress 1
    def on_press_1(event):
        equation[0] = ''.join((equation[0],'1')) #Adds 1 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this
    
    #Onpress 2
    def on_press_2(event):
        equation[0] = ''.join((equation[0],'2')) #Adds 2 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this
    
    #Onpress 3
    def on_press_3(event):
        equation[0] = ''.join((equation[0],'3')) #Adds 3 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress 4
    def on_press_4(event):
        equation[0] = ''.join((equation[0],'4')) #Adds 4 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress 5
    def on_press_5(event):
        equation[0] = ''.join((equation[0],'5')) #Adds 5 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this
    
    #Onpress 6
    def on_press_6(event):
        equation[0] = ''.join((equation[0],'6')) #Adds 6 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this
    
    #Onpress 7
    def on_press_7(event):
        equation[0] = ''.join((equation[0],'7')) #Adds 7 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this 

    #Onpress 8
    def on_press_8(event):
        equation[0] = ''.join((equation[0],'8')) #Adds 8 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress 9
    def on_press_9(event):
        equation[0] = ''.join((equation[0],'9')) #Adds 9 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress 0
    def on_press_0(event):
        equation[0] = ''.join((equation[0],'0')) #Adds 0 to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress decimal
    def on_press_decimal(event):
        equation[0] = ''.join((equation[0],'.')) #Adds . to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this


    #Operators

    #Onpress division
    def on_press_division(event):
        equation[0] = ''.join((equation[0],'÷')) #Adds ÷ to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress times
    def on_press_times(event):
        equation[0] = ''.join((equation[0],'x')) #Adds x to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress subtract
    def on_press_subtract(event):
        equation[0] = ''.join((equation[0],'-')) #Adds - to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress add
    def on_press_add(event):
        equation[0] = ''.join((equation[0],'+')) #Adds + to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this


    #Delete, brackets and equals

    #Onpress delete
    def on_press_delete(event):
        equation[0] = ((equation[0]))[:-1]   #Deletes the last character of the equation
        answer.configure(text = equation[0]) #Configures the answer label to show this

    #Onpress open bracket
    def on_press_open_bracket(event):
        equation[0] = ''.join((equation[0],'(')) #Adds ( to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #Onpress close bracket
    def on_press_close_bracket(event):
        equation[0] = ''.join((equation[0],')')) #Adds ) to the equation
        answer.configure(text = equation[0])     #Configures the answer label to show this

    #On press equals
    def on_press_equals(event):
        x = equation[0]
        x = x.replace('÷','/') #Changes the ÷ sign to /
        x = x.replace('x','*') #Changes the x sign to *
        x = x.replace('X','*') #Changes the x sign to *
        while True:
            try:
                equation[0] = str(eval(x)) #Solves the equation
            except SyntaxError:
                break
            else:
                answer.configure(text = equation[0]) #Configures the answer label to show this
                break

    def on_press_clear(event):
        equation[0] = '' #Deletes everything in the equation
        answer.configure(text = equation[0]) #Configures the answer label to show this

    frame_buttons = tk.Frame(root) #Make frame
    #These buttons are in the frame. stickt = 'ew' makes the buttons the same size, and next to each other. COLUMN 1
    button_1 = Button(frame_buttons,text = '1',font = font_style,command = on_click_1,bg = button_background,fg = button_foreground) #Button 1
    button_1.grid(row = 0,column = 0,sticky = 'ew')
    button_2 = Button(frame_buttons,text = '2',font = font_style,command = on_click_2,bg = button_background,fg = button_foreground) #Button 2
    button_2.grid(row = 0,column = 1,sticky = 'ew')
    button_3 = Button(frame_buttons,text = '3',font = font_style,command = on_click_3,bg = button_background,fg = button_foreground) #Button 3
    button_3.grid(row = 0,column = 2,sticky = 'ew')
    button_4 = Button(frame_buttons,text = '4',font = font_style,command = on_click_4,bg = button_background,fg = button_foreground) #Button 4
    button_4.grid(row = 1,column = 0,sticky = 'ew')
    button_5 = Button(frame_buttons,text = '5',font = font_style,command = on_click_5,bg = button_background,fg = button_foreground) #Button 5
    button_5.grid(row = 1,column = 1,sticky = 'ew')
    button_6 = Button(frame_buttons,text = '6',font = font_style,command = on_click_6,bg = button_background,fg = button_foreground) #Button 6
    button_6.grid(row = 1,column = 2,sticky = 'ew')
    button_7 = Button(frame_buttons,text = '7',font = font_style,command = on_click_7,bg = button_background,fg = button_foreground) #Button 7
    button_7.grid(row = 2,column = 0,sticky = 'ew')
    button_8 = Button(frame_buttons,text = '8',font = font_style,command = on_click_8,bg = button_background,fg = button_foreground) #Button 8
    button_8.grid(row = 2,column = 1,sticky = 'ew')
    button_9 = Button(frame_buttons,text = '9',font = font_style,command = on_click_9,bg = button_background,fg = button_foreground) #Buyyon 9
    button_9.grid(row = 2,column = 2,sticky = 'ew')
    button_0 = Button(frame_buttons,text = '0',font = font_style,command = on_click_0,bg = button_background,fg = button_foreground) #Button 0
    button_0.grid(row = 3,column = 0,sticky = 'ew')
    fill_1 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)                          #Fill 1 (bottom)
    fill_1.grid(row = 3,column = 2,sticky = 'nsew')
    button_decimal = Button(frame_buttons,text = '.',font = font_style,command = on_click_decimal,bg = button_background,fg = button_foreground) #Decimal button
    button_decimal.grid(row = 3,column = 1,sticky = 'ew')

    #Operator buttons (also in frame) COLUMN 2
    division = Button(frame_buttons,text = '÷',font = font_style,command = on_click_division,bg = button_background,fg = button_foreground)   #Division button
    division.grid(row = 0,column = 3,sticky = 'ew')
    times = Button(frame_buttons,text = 'x',font = font_style,command = on_click_times,bg = button_background,fg = button_foreground)         #Times button
    times.grid(row = 1,column = 3,sticky = 'ew')
    substract = Button(frame_buttons,text = '-',font = font_style,command = on_click_substract,bg = button_background,fg = button_foreground) #Subtract button
    substract.grid(row = 2,column = 3,sticky = 'ew')
    add = Button(frame_buttons,text = '+',font = font_style,command = on_click_add,bg = button_background,fg = button_foreground)             #Add button
    add.grid(row = 3,column = 3,sticky = 'ew')

    #Delete, equals and brackets buttons (also in frame) COLUMN 3
    delete = Button(frame_buttons,text = 'DEL',font = font_style,command = on_click_delete,bg = button_background,fg = button_foreground)             #Delete button
    delete.grid(row = 0,column = 4,sticky = 'ew')
    open_bracket = Button(frame_buttons,text = '(',font = font_style,command = on_click_open_bracket,bg = button_background,fg = button_foreground)   #Open bracket button
    open_bracket.grid(row = 1,column = 4,sticky = 'ew') 
    close_bracket = Button(frame_buttons,text = ')',font = font_style,command = on_click_close_bracket,bg = button_background,fg = button_foreground) #Close bracket button
    close_bracket.grid(row = 2,column = 4,sticky = 'ew')
    equals = Button(frame_buttons,text = '=',font = font_style,command = on_click_equals,bg = button_background,fg = button_foreground)               #Equals button
    equals.grid(row = 3,column = 4,sticky = 'ew')

    #Clear button and fill (also in frame) COLUMN 4
    clear = Button(frame_buttons,text = 'CL',font = font_style,command = on_click_clear,bg = button_background,fg = button_foreground) #Clear button
    clear.grid(row = 0,column = 5,sticky = 'ew')

    #Fill:
    fill_2 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_2.grid(row = 1,column = 5,sticky = 'nsew')
    fill_3 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_3.grid(row = 2,column = 5,sticky = 'nsew')
    fill_4 = Label(frame_buttons,text = '',font = font_style,bg = button_background,fg = button_foreground)
    fill_4.grid(row = 3,column = 5,sticky = 'nsew')

    #Sort out answer label:
    answer = Label(text = equation[0],font = font_style,bg = answer_background,fg = answer_foreground)

    answer.grid(row = 0,column = 0,sticky = 'nsew')
    frame_buttons.grid(row = 1,column = 0)
    
    #Bind key presses with fuctions:
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
    root.bind('x', on_press_times)
    root.bind('X', on_press_times)
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

