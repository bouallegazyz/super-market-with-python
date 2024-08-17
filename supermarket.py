from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
pro=Tk()
pro.geometry("800x400")
pro.resizable(False,False)
pro.title("supermarchet")
pro.iconbitmap("supermarcher.ico")
title=Label(pro,text="supermarketsystem",fg="gold",bg="black",font=('tajawel',16,'bold'))
title.pack(fill=X)
u1='https://www.facebook.com/profile.php?id=100010354231680'
def open1():
    webbrowser.open_new(u1)
def verif():
    user=Enl.get()
    passw=En2.get()
    if user=='aziz' and passw=="12345678":
        messagebox.showinfo('welcome',"user et mot de passe sont correct")
        import super
        mypage=super.Super
        page=mypage.get()
        print(page)
    else:
        messagebox.showerror('eurror',"mot de passe et user ne sont pas correct")
F1=Frame (pro, width=230, height=420 ,bg='red')
F1.place(x=570,y=30)
Title1 =Label (F1, text ='supermarket system',bg='red',fg='white',font=("tajawal",12,'bold'))
Title1.place (x=42,y=10)
title2 =Label(F1,text='bouallegue mohamed aziz',bg='red',fg='white',font=("tajawal",12,'bold'))
title2.place(x=22,y=50)
title3 =Label(F1,text='contact :',bg='red',fg='white',font=("tajawal",12,'bold'))
title3.place(x=76,y=90)
B1=Button(F1, text='facebook account',width=26,fg='black',bg='yellow',font=('tajawal',11,'bold'),command=open1)
B1.place(x=2,y=130)
title4 =Label(F1,text='telephone:51098640',bg='red',fg='white',font=("tajawal",12,'bold'))
title4.place(x=40,y=170)
B2=Button(F1, text='fermer le systéme',width=26,fg='black',bg='yellow',font=('tajawal',11,'bold'),command=quit)
B2.place(x=2,y=330)
photo=PhotoImage(file="supermarcher.png")
imo=Label(pro,image=photo)
imo.place(x=50,y=31,height=300)
F2=Frame (pro, width=570, height=120,bg='red')
F2.place(x=0,y=330)
l1=Label(F2,text='le nom de utilisateur',fg='gold',bg='red',font=("tajawal",12))
l1.place(x=20,y=10)
l2=Label(F2,text='le mot de passe',fg='gold',bg='red',font=("tajawal",12))
l2.place(x=20,y=40)
Enl =Entry (F2 ,font=('tajawal',12), justify='center')
Enl.place (x=170,y=10)
En2 = Entry (F2 ,font=('tajawal',12), justify='center')
En2.place(x=150,y=40)
b=Button(F2,text='login',fg='black',bg='gold',font=("tajawal",12),command=verif)
b.place(x=400,y=15)

pro.mainloop()