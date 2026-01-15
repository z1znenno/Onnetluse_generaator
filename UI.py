from tkinter import *
import onnitleja

def work_window():
    root.geometry('400x300')
    btn1.destroy()
    btn2.destroy()
    btn3 = Button(root, command=work_window, text='Õnnitle ühte konkreetset saajat', font=('Comic Sans MS', 15))
    btn3.pack()
    btn4 = Button(root, command=valjamine, text='Õnnitle mitut saajat (komaga eraldatud)', font=('Comic Sans MS', 15))
    btn4.pack()

def valjamine():
    root.destroy()

root = Tk()

root.geometry('500x250')
root.title("Email õnnetluse generator")
root.resizable(width=False, height=False)
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

title = Label(root, text='Email õnnetluse generator', font=('Comic Sans MS', 20))
title.pack()
btn1 = Button(root,command=work_window, text='Alustada', font=('Comic Sans MS', 15))
btn1.pack()
btn2 = Button(root, command=valjamine, text='Välja', font=('Comic Sans MS', 15))
btn2.pack()

root.mainloop()

