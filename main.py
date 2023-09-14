import tkinter
from tkinter import*
import messagebox
from tkinter import ttk





A=Tk()
A.geometry("%dx%d+%d+%d"%(1000,560,1,1))
A.configure(bg="#AEE2FF")
A.title("register")
A.iconbitmap("icon/abol.ico")

lbl=tkinter.PhotoImage(file="abb.png")
label = ttk.Label(A, image=lbl).pack()
users=[]
#def

def onclickregister(e):
    if btn_register.cget("state")==NORMAL:
        dic={"name":txt_name.get(),"family":txt_family.get(),"age":str(combo.get()),"phone_number":str(txt_phone_number.get())}
        if exist(dic)==False:
            register(dic)
            insert(dic)
            clear_text()
            messagebox.showinfo("register","عملیات با موفقیت انجام شد")
        else:
            messagebox.askyesno("rep","یا میخواهید فرد تکراری ثبت نام کنید")

def register(value):
    users.append(value)

def insert(value):
    tbl.insert('',"end",values=[value["name"],value["family"],value["age"],value["phone_number"]])


def clear_text():
    txtnamevar.set("")
    txtfamilyvar.set("")
    txtphonevar.set("")
    txtcombovar.set("")
    txt_name.focus_set()

def getselection(e):
    selct=tbl.selection()
    if selct!=():
        s=tbl.item(selct)["values"]
        txtnamevar.set(s[0])
        txtfamilyvar.set(s[1])
        txtphonevar.set(s[3])
        txtcombovar.set(s[2])

def onclickdelete(e):
    dialog = messagebox.askyesno("delete","ایا از حذف کاربر اطمینان دارید؟")
    if dialog==True:
        dic={"name":txt_name.get(),"family":txt_family.get(),"age":str(combo.get()),"phone_number":str(txt_phone_number.get())}
        delete(dic)
        remove_tbl()
        clear_text()




def delete(value):
    for item in users:
        if item["name"]==value["name"] and item["family"]==value["family"] and item["age"]==value["age"] and item["phone_number"]==value["phone_number"]:
            users.remove(value)


def remove_tbl():
    select=tbl.selection()
    if select!=():
        s=tbl.item(select)["values"]
        tbl.delete(select)

def onclicksreach(e):
    a=txt_sreach.get()
    resuilt=sreach(a)
    clear()
    for item in resuilt:
        insert(item)



def sreach(value):
    resuiltlist=[]
    for item in users:
        if item["name"] == txt_sreach.get() or item["family"] == txt_sreach.get() or item["age"] == txt_sreach.get() or item["phone_number"] == txt_sreach.get():
            resuiltlist.append(item)
    return resuiltlist




def clear():
    for item in tbl.get_children():
        sel=str(item)
        tbl.delete(sel)




def exist(value):
    for item in users:
        if item["name"]==value["name"] and item["family"]==value["family"] and item["age"]==value["age"] and item["phone_number"]==value["phone_number"]:
            return True
    return False

def onclickupdate(e):
    selct=tbl.selection()
    if selct!=():
        selct_item=tbl.item(selct)["values"]
        dic = {"name":selct_item[0],"family":selct_item[1],"age":str(selct_item[2]),"phone_number":str(selct_item[3])}
        index1=update(dic)
        p=users[index1]
        tbl.item(selct, values=[p["name"],p["family"],p["age"],p["phone_number"]])
        messagebox.showinfo("انجام شد","ویرایش با موفقیت انجام شد")


def update(value):
    index=users.index(value)
    users[index]={"name":txt_name.get(),"family":txt_family.get(),"age":str(combo.get()),"phone_number":str(txt_phone_number.get())}
    return index

def cloes():
    A.withdraw()




txtnamevar=StringVar()
txtfamilyvar=StringVar()
txtphonevar=StringVar()
txtcombovar=StringVar()
txtsreachvar=StringVar()


#txt
txt_name=Entry(A,width=40,justify="center",bd=5,textvariable=txtnamevar)
txt_name.place(x=150,y=50)

txt_family=Entry(A,width=40,justify="center",bd=5,textvariable=txtfamilyvar)
txt_family.place(x=150,y=110)

txt_phone_number=Entry(A,width=40,justify="center",bd=5,textvariable=txtphonevar)
txt_phone_number.place(x=150,y=170)

combo=ttk.Combobox(A,width=40,textvariable=txtcombovar)
a=[]
for i in range(1,121):
    a.append(i)
combo["value"]=a
combo.place(x=150,y=230)

txt_sreach=Entry(A,width=40,justify="center",bd=5,textvariable=txtsreachvar)
txt_sreach.place(x=700,y=30)

#lbl
lbl_name=Label(A,text="name:",font=20,foreground="black",bg="blue")
lbl_name.place(x=1,y=45)

lbl_family=Label(A,text="family:",font=20,foreground="black",bg="blue")
lbl_family.place(x=1,y=110)

lbl_phone_number=Label(A,text="phone number:",font=20,foreground="black",bg="blue")
lbl_phone_number.place(x=1,y=170)

lbl_age=Label(A,text="age:",font=20,foreground="black",bg="blue")
lbl_age.place(x=1,y=230)

lbl_sreach=Label(A,text="sreach:",foreground="black",bg="blue")
lbl_sreach.place(x=700,y=9)


#btn
btn_register=Button(A,text="register",bg="#8BE8E5",width=9,height=4)
btn_register.bind("<Button-1>",onclickregister)
btn_register.place(x=430,y=50)

btn_delete=Button(A,text="delete",bg="#8BE8E5",width=10,height=4)
btn_delete.bind("<Button-1>",onclickdelete)
btn_delete.place(x=10,y=300)

btn_sreach=Button(A,text="sreach",bg="#8BE8E5",width=15)
btn_sreach.bind("<Button-1>",onclicksreach)
btn_sreach.place(x=837,y=60)

btn_update=Button(A,text="edit",bg="#8BE8E5",width=10,height=8)
btn_update.bind("<Button-1>",onclickupdate)
btn_update.place(x=10,y=380)


#tabel
column=("c1","c2","c3","c4")
tbl=ttk.Treeview(columns=column,show="headings")

tbl.heading(column[0],text="name")
tbl.column(column[0],width=200)
tbl.heading(column[1],text="family")
tbl.column(column[1],width=200)
tbl.heading(column[2],text="age")
tbl.column(column[2],width=200)
tbl.heading(column[3],text="phone number")
tbl.column(column[3],width=200)

tbl.bind("<Button-1>",getselection)

tbl.place(x=100,y=300)



Meno123=Menu(A)
menobar=Menu(Meno123,tearoff=0)
menobar.add_command(label="تنظیمات")
menobar.add_command(label="کاربری")
menobar.add_separator()
menobar.add_command(label="خروج",foreground="red",command=cloes)
Meno123.add_cascade(label="file",menu=menobar)

A.config(menu=Meno123)



































A.mainloop()
