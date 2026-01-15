from tkinter import *
import mailer

def main_tagasi():
    btn3.pack_forget()
    btn4.pack_forget()
    tagasiBtn.pack_forget()
    oma_epost_info.pack()
    oma_epost.pack()
    btn1.pack()
    btn2.pack()


def leia_saajad():
    saajad = kuhu.get()
    if '@' in saajad:
        saaja_error.pack_forget()
    else:
        kuhu.pack_forget()
        enter.pack_forget()
        kuhu.pack()
        saaja_error.pack()
        enter.pack()

def work_window():
    global btn3, btn4, tagasiBtn
    root.geometry('400x300')
    oma_epost_info.pack_forget()
    oma_epost.pack_forget()
    btn1.pack_forget()
    btn2.pack_forget()
    btn3 = Button(root, command=uks_saaja, text='Õnnitle ühte konkreetset saajat', font=('Comic Sans MS', 15))
    btn3.pack()
    btn4 = Button(root, command=valjamine, text='Õnnitle mitut saajat (komaga eraldatud)', font=('Comic Sans MS', 15))
    btn4.pack()
    tagasiBtn = Button(root, command=main_tagasi, text='Tagasi', font=('Comic Sans MS', 15))
    tagasiBtn.pack()

def uks_saaja():
    global kuhu, enter
    btn3.pack_forget()
    btn4.pack_forget()
    kuhu_info.pack()
    kuhu = Entry(root)
    kuhu.pack()
    enter = Button(root, command=leia_saajad, text='Enter', font=('Comic Sans MS', 15))
    enter.pack()


def valjamine():
    root.destroy()

root = Tk()

root.geometry('500x250')
root.title("Email õnnetluse generator")
root.resizable(width=False, height=False)
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

saaja_error = Label(root, text="Ma ei saa aru, mis e-post see on!")
kuhu_info = Label(root, text="Sisestage e-posti adress!")

title = Label(root, text='Email õnnetluse generator', font=('Comic Sans MS', 20))
title.pack()
oma_epost_info = Label(root, text="Sisestage oma e-posti adress!")
oma_epost_info.pack()
oma_epost = Entry(root)
oma_epost.pack()
btn1 = Button(root,command=work_window, text='Alustada', font=('Comic Sans MS', 15))
btn1.pack()
btn2 = Button(root, command=valjamine, text='Välja', font=('Comic Sans MS', 15))
btn2.pack()

root.mainloop()

