import os
from tkinter import*
import messagebox
import sing_up
from tkinter import ttk
A=Tk()
A.geometry("%dx%d+%d+%d"%(500,400,500,50))
A.configure(bg="#AEE2FF")
A.title("register")
A.iconbitmap("icon/abol.ico")

#def
def sing_up1(e):
    sing_up.showmsg()


def login(e):
    for item in sing_up.users:
        if item["user"]==txt_users.get() and item["password"]==txt_password.get():
            os.system(f"python main.py")







txtuservar=StringVar()
txtpasswordvar=StringVar()
#txt

txt_users=Entry(A,width=40,justify="center",bd=5,textvariable=txtuservar)
txt_users.place(x=130,y=75)

txt_password=Entry(A,width=40,justify="center",bd=5,textvariable=txtpasswordvar)
txt_password.place(x=130,y=140)

#lbl

lbl_users=Label(A,text="users:",font=20,foreground="black",bg="#AEE2FF")
lbl_users.place(x=1,y=75)

lbl_password=Label(A,text="password:",font=20,foreground="black",bg="#AEE2FF")
lbl_password.place(x=1,y=140)

lbl=Label(A,text="به صفحه ی ورود خوش امدید")
lbl.pack(side="top",fill=BOTH)

lbl_link=ttk.Label(A,text="برای ثبت نام کلیک کنید",foreground="blue")
lbl_link.bind("<Button-1>",sing_up1)
lbl_link.place(x=1,y=370)
#btn

btn_login=Button(A,text="log in",bg="#8BE8E5",width=16)
btn_login.bind("<Button-1>",login)
btn_login.place(x=200,y=230)





A.mainloop()