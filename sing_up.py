from tkinter import*
import messagebox



users=[]



def showmsg():

    A=Tk()
    A.geometry("%dx%d+%d+%d"%(500,400,500,50))
    A.configure(bg="#AEE2FF")
    A.title("register")
    A.iconbitmap("icon/abol.ico")

    #def

    def sing_up(e):
        b=False
        for item in users:
            if item["user"]==txt_users.get():
                messagebox.showinfo("warning","کاربر تکراری میباشد")
                b=True
                break
        if b==False:
            if txt_password.get()==txt_repassword.get():
                dic={"user":txt_users.get(),"password":txt_password.get()}
                users.append(dic)
                print(dic)
                messagebox.showinfo("","ثبت نام با موفقیت انجام شد")

            else:
                messagebox.showwarning("warning","پسورد را چک کنید")




    txtuservar=StringVar()
    txtpasswordvar=StringVar()
    txtrepasswordvar=StringVar()
    #txt

    txt_users=Entry(A,width=40,justify="center",bd=5,textvariable=txtuservar)
    txt_users.place(x=130,y=75)

    txt_password=Entry(A,width=40,justify="center",bd=5,textvariable=txtpasswordvar)
    txt_password.place(x=130,y=140)

    txt_repassword=Entry(A,width=40,justify="center",bd=5,textvariable=txtrepasswordvar)
    txt_repassword.place(x=130,y=215)

    #lbl

    lbl_users=Label(A,text="users:",font=20,foreground="black",bg="#AEE2FF")
    lbl_users.place(x=1,y=75)

    lbl_password=Label(A,text="password:",font=20,foreground="black",bg="#AEE2FF")
    lbl_password.place(x=1,y=140)

    lbl_repassword=Label(A,text="repassword:",font=20,foreground="black",bg="#AEE2FF")
    lbl_repassword.place(x=1,y=215)

    lbl=Label(A,text="به صفحه ی ثبت نام خوش امدید")
    lbl.pack(side="top",fill=BOTH)


    #btn

    btn_register=Button(A,text="sing up",bg="#8BE8E5",width=16)
    btn_register.bind("<Button-1>",sing_up)
    btn_register.place(x=200,y=290)







    A.mainloop()