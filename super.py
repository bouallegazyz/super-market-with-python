from tkinter import *
import math, random , os
from tkinter import messagebox
class Super:
    def __init__ (self,root):
        self.root=root
        self.root.geometry ('1300x700+30+10')
        self.root.title('Super-Market')
        self.root.resizable (False, False)
        self.root.iconbitmap('supermarcher.ico')
        title = Label (self.root, text='supermarket', fg='yellow',bg="black",font=("tajawal",12))
        title.pack (fill=X)
        def totale():
            q1=bqent1.get()
            q2=bqent2.get()
            q3=bqent3.get()
            q4=bqent4.get()
            q5=bqent5.get()
            q6=bqent6.get()
            q7=bqent7.get()
            q8=bqent8.get()

            l=[q1,q2,q3,q4,q5,q6,q7,q8]
            x=0
            for i in range(8):
                if l[i]=="":
                    x=x
                else:
                    if l[i]==q1:
                        x=x+int(l[i])*1.29
                    elif l[i]==q2:
                        x=x+int(l[i])*1.29
                    elif l[i]==q3:                
                        x=x+int(l[i])*3.30
                    elif l[i]==q4:                
                        x=x+int(l[i])*5.50
                    elif l[i]==q5:                
                        x=x+int(l[i])*8.70
                    elif l[i]==q6:                
                        x=x+int(l[i])*2,19 
                    elif l[i]==q7:                
                        x=x+int(l[i])*2,19 
                    else:                
                        x=x+int(l[i])*2,19
            if x==0:
                messagebox.showerror('eurror',"donner le liste d'achat")
            else:
                messagebox.showinfo('totale',x)
        #========Fatora=====
        def rd():
            x=random.randint(1000,9999)
            messagebox.showinfo("le numéro est de facture est",x)
        #== Customer DATA
        F1 =Frame(root, bd=2 ,width=338, height=170, bg='red')
        F1.place(x=961,y=25)
        tit = Label (F1, text="les donnés de client",font=('tajawal',13, 'bold'))
        tit.place (x=90,y=0)
        his_name = Label(F1 ,text="mon de client", font=('tajawal',10),bg='red')
        his_name.place (x=6, y=40)
        his_phone = Label(F1, text='numero de téléphone', font=('tajawal',10),bg='red')
        his_phone.place (x=6, y=70)
        his_num = Label (F1, text="numero d'achat", font=('tajawal',10), bg='red')
        his_num.place (x=6,y=100)
        En_name =Entry (F1 ,font=('tajawal',12), justify='center')
        En_name.place (x=130,y=40)
        En_phone =Entry (F1 ,font=('tajawal',12), justify='center')
        En_phone.place (x=130,y=70)
        En_num =Button (F1 ,bd=1,bg='yellow',fg='black',font=('tajawal',12),text='voir',command=rd)
        En_num.place (x=130,y=100)
        # Fatora: bill
        titdd=Label (F1, text='[facture]',font=('tajawal', 13, 'bold'), bg='red')
        titdd.place (x=125, y=135)
        F3=Frame (root, bd=2, width=338, height=399, bg='white')
        F3.place (x=961,y=205)
        scrol_y = Scrollbar (F3, orient=VERTICAL)
        self.textarea= Text (F3, yscrollcommand=scrol_y.set)
        scrol_y.pack (side=LEFT, fill=Y)
        scrol_y.config (command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        F4 = Frame (root, bd=2, width=657, height=112, bg='red')
        F4.place (x=641,y=587)
        hesab =Button (F4, text="totale de boissons" ,width=13, height=1,font='tajawal', bg='black',fg='gold',command=totale)
        hesab.place (x=520, y=10)
        fatora =Button (F4, text='facture' ,width=13, height=1, font='tajawal',bg='black',fg='gold')
        fatora.place (x=520, y=55)
        clear = Button (F4, text='totales de allimentaire', width=13,height=1, font='tajawal',bg='black',fg='gold')
        clear.place (x=350, y=10)
        exite =Button (F4, text='fermer' ,width=13, height=1, font='tajawal',bg='black',fg='gold',command=quit)
        exite.place (x=350, y=55)
         #======== items [1] =====
        FF1=Frame (root, bd=2 ,width=318, height=680,bg='yellow')
        FF1.place (x=1,y=25)
        t = Label (FF1, text='les boissons', font=('tajawal',13,'bold'),bg='yellow',fg='black')
        t.place (x=105,y=0)
        bq1=Label(FF1,text='Canette cocacola:1,29 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq1.place(x=1,y=70)
        bq2=Label(FF1,text='Canette Fanta:1,29 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq2.place(x=1,y=90)
        bq3=Label(FF1,text='coca de 1L :2,51 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq3.place(x=1,y=110)
        bq4=Label(FF1,text='cocacola de 1,5 :3,00 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq4.place(x=1,y=130)
        bq5=Label(FF1,text='Canette Fanta:1,29 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq5.place(x=1,y=150)
        bq6=Label(FF1,text='fanta 1L :2,39 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq6.place(x=1,y=170)
        bq7=Label(FF1,text='Boga Lim 1,5L:3,10 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq7.place(x=1,y=190)
        bq8=Label(FF1,text='Punch Cidre:7,47 DT',font=('tajawal',13),bg='yellow',fg='black')
        bq8.place(x=1,y=210)
        bqent1=Entry(FF1,width=12)
        bqent1.place(x=200,y=70)
        bqent2=Entry(FF1,width=12)
        bqent2.place(x=200,y=90)
        bqent3=Entry(FF1,width=12)
        bqent3.place(x=200,y=110)
        bqent4=Entry(FF1,width=12)
        bqent4.place(x=200,y=130)
        bqent5=Entry(FF1,width=12)
        bqent5.place(x=200,y=150)
        bqent6=Entry(FF1,width=12)
        bqent6.place(x=200,y=170)
        bqent7=Entry(FF1,width=12)
        bqent7.place(x=200,y=190)
        bqent8=Entry(FF1,width=12)
        bqent8.place(x=200,y=210)
        #======== items [2] =====
        FF2=Frame (root, bd=2 ,width=318, height=680,bg='yellow')
        FF2.place (x=321,y=25)
        t = Label (FF2, text='les produits alimentaires', font=('tajawal',13,'bold'),bg='yellow',fg='black')
        t.place (x=80,y=0)
        al1=Label(FF2,text='Lait(1 litre):1,45 DT',font=('tajawal',13),bg='yellow',fg='black')
        al1.place(x=1,y=70)
        al2=Label(FF2,text='Pain(1 kg):0,47 DT',font=('tajawal',13),bg='yellow',fg='black')
        al2.place(x=1,y=90)
        al3=Label(FF2,text='Riz(1 kg):3,30 DT',font=('tajawal',13),bg='yellow',fg='black')
        al3.place(x=1,y=110)
        al4=Label(FF2,text='Pommes(1 kg):5,50 DT',font=('tajawal',13),bg='yellow',fg='black')
        al4.place(x=1,y=130)
        al5=Label(FF2,text='Bananes(1 kg):8,70 DT',font=('tajawal',13),bg='yellow',fg='black')
        al5.place(x=1,y=150)
        al6=Label(FF2,text='Tomates(1 kg):2,19 DT',font=('tajawal',13),bg='yellow',fg='black')
        al6.place(x=1,y=170)
        al7=Label(FF2,text='Tomates(1 kg):2,19 DT',font=('tajawal',13),bg='yellow',fg='black')
        al7.place(x=1,y=190)
        al8=Label(FF2,text='poulet(1 kg):17,30 DT',font=('tajawal',13),bg='yellow',fg='black')
        al8.place(x=1,y=210)
        al9=Label(FF2,text='Bœuf(1 kg):35,40 DT',font=('tajawal',13),bg='yellow',fg='black')
        al9.place(x=1,y=230)
        alm1=Entry(FF2,bd=2,width=12,justify='center')
        alm1.place(x=200,y=70)
        alm2=Entry(FF2,bd=2,width=12,justify='center')
        alm2.place(x=200,y=90)
        alm3=Entry(FF2,bd=2,width=12,justify='center')
        alm3.place(x=200,y=110)
        alm4=Entry(FF2,bd=2,width=12,justify='center')
        alm4.place(x=200,y=130)
        alm5=Entry(FF2,bd=2,width=12,justify='center')
        alm5.place(x=200,y=150)
        alm6=Entry(FF2,bd=2,width=12,justify='center')
        alm6.place(x=200,y=170)
        alm7=Entry(FF2,bd=2,width=12,justify='center')
        alm7.place(x=200,y=190)
        alm8=Entry(FF2,bd=2,width=12,justify='center')
        alm8.place(x=200,y=210)
        alm9=Entry(FF2,bd=2,width=12,justify='center')
        alm9.place(x=200,y=230)


        #======== items [3] =====
        FF3=Frame (root, bd=2 ,width=318, height=560,bg='yellow')
        FF3.place (x=641,y=25)
        
        self.qq1=IntVar()
        self.qq2=IntVar()
        self.qq3=IntVar()
        self.qq5=IntVar()
        self.qq6=IntVar()
        self.qq7=IntVar()
        self.qq8=IntVar()
        self.qq9=IntVar()
        self.bacoliat= StringVar()
        self.adoat = StringVar ()
        






root =Tk()
ob = Super(root)
root.mainloop ( ) 
