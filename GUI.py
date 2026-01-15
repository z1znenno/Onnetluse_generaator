import email
from tkinter import *
import mailer

def work_window():
    global btn3, btn4, tagasiBtn
    oma_epost_info.pack_forget()
    oma_epost.pack_forget()
    btn1.pack_forget()
    btn2.pack_forget()
    posti_error.pack_forget()
    oma_mail = oma_epost.get()
    if '@' in oma_mail:
        root.geometry('400x300')
        btn3 = Button(root, command=saaja, text='Õnnitle ühte konkreetset saajat', font=('Comic Sans MS', 15))
        btn3.pack()
        btn4 = Button(root, command=valjamine, text='Õnnitle mitut saajat (ruumiga eraldatud)', font=('Comic Sans MS', 15))
        btn4.pack()
        tagasiBtn = Button(root, command=main_tagasi, text='Tagasi', font=('Comic Sans MS', 15))
        tagasiBtn.pack()
    else:
        oma_epost_info.pack()
        oma_epost.pack()
        posti_error.pack()
        btn1.pack()
        btn2.pack()

def saaja():
    global kuhu, enter
    btn3.pack_forget()
    btn4.pack_forget()
    tagasiBtn.pack_forget()
    kuhu_info.pack()
    kuhu = Entry(root)
    kuhu.pack()
    enter = Button(root, command=saatma, text='Saatma', font=('Comic Sans MS', 15))
    enter.pack()

def main_tagasi():
    btn3.pack_forget()
    btn4.pack_forget()
    tagasiBtn.pack_forget()
    oma_epost_info.pack()
    oma_epost.pack()
    btn1.pack()
    btn2.pack()


def saatma():
    saajad = kuhu.get()
    saajad.split()
    if '@' in saajad:
        posti_error.pack_forget()
        kuhu_info.pack_forget()
        kuhu.pack_forget()
        enter.pack_forget()
        saatmine_Label = Label(root, text='Saadame...', font=('Comic Sans MS', 15))
        saatmine_Label.pack()
        mailer.soovi_saatmine(saajad)
    else:
        kuhu.pack_forget()
        enter.pack_forget()
        kuhu.pack()
        posti_error.pack()
        enter.pack()

def valjamine():
    root.destroy()

root = Tk()
root.geometry('500x250')
root.title("Email õnnetluse generator")
root.resizable(width=False, height=False)
icon = PhotoImage(file='icon.png')
root.iconphoto(False, icon)

posti_error = Label(root, text="Ma ei saa aru, mis e-post see on!", font=('Comic Sans MS', 10), fg='red')
kuhu_info = Label(root, text="Sisestage e-posti adress!", font=('Comic Sans MS', 15))

title = Label(root, text='Email õnnetluse generator', font=('Comic Sans MS', 20))
title.pack()
oma_epost_info = Label(root, text="Sisestage oma e-posti adress!", font=('Comic Sans MS', 15))
oma_epost_info.pack()
oma_epost = Entry(root)
oma_epost.pack()
btn1 = Button(root,command=work_window, text='Alustada', font=('Comic Sans MS', 15))
btn1.pack()
btn2 = Button(root, command=valjamine, text='Välja', font=('Comic Sans MS', 15))
btn2.pack()

root.mainloop()

