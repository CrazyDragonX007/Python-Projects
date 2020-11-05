from tkinter import *

root = Tk()
root.geometry("1200x800+0+0")
root.title("PYTHON PIZZA")

# ----------------Variables --------------

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
svar1=IntVar()
svar2=IntVar()
svar3=IntVar()
svar4=IntVar()
svar5=IntVar()
svar6=IntVar()
svar7=IntVar()
svar8=IntVar()
svar9=IntVar()
v=IntVar()
v.set(0)
v1=300
v2=400
v3=500
nv1=500
nv2=450
nv3=600
s1=100
s2=40
s3=80
fbill=0
stot=0
ptot=0
d1=StringVar()
d1.set("Margherita")
d2=StringVar()
d2.set("Veggie Lovers")
d3=StringVar()
d3.set("Veggie Supreme")
d4=StringVar()
d4.set("Chicken Tandoori")
d5=StringVar()
d5.set("Chicken Supreme")
d6=StringVar()
d6.set("Meatizza")
d7=StringVar()
d7.set("Lava Cake")
d8=StringVar()
d8.set("Mountain Dew")
d9=StringVar()
d9.set("Cheese Garlic Bread")

# ---------------- Functions ----------------

def pizza():
    win = Toplevel()
    win.geometry("500x500+0+0")
    win.title("Choose your pizza!")
    piza=Frame(win,bd=8,relief="raise")
    piza.pack()
    veg=Label(piza,text="Veg").grid(row=0,column=0)
    price=Label(piza,text=" Price\n Standard Size ").grid(row=0,column=1)
    quan=Label(piza,text=" Quantity ").grid(row=0,column=2)
    a=Checkbutton(piza,text=" Margherita ",variable=var1).grid(row=1,column=0,sticky=W)
    ap=Label(piza,text=" Rs-300").grid(row=1,column=1)
    ap1=Entry(piza,textvariable=svar1).grid(row=1,column=2)
    b=Checkbutton(piza,text=" Veggie lovers ",variable=var2).grid(row=2,column=0,sticky=W)
    bp=Label(piza,text=" Rs-400 ").grid(row=2,column=1)
    bp1=Entry(piza,textvariable=svar2).grid(row=2,column=2)
    c=Checkbutton(piza,text=" Veggie Supreme ",variable=var3).grid(row=3,column=0,sticky=W)
    cp=Label(piza,text=" Rs-500 ").grid(row=3,column=1)
    cp1=Entry(piza,textvariable=svar3).grid(row=3,column=2)
    nveg=Label(piza,text="Non - Veg").grid(row=4,column=0)
    d=Checkbutton(piza,text=" Chicken Tandoori ",variable=var4).grid(row=5,column=0,sticky=W)
    dp=Label(piza,text=" Rs-500 ").grid(row=5,column=1)
    dp1=Entry(piza,textvariable=svar4).grid(row=5,column=2)
    e=Checkbutton(piza,text=" Chicken Supreme ",variable=var5).grid(row=6,column=0,sticky=W)
    ep=Label(piza,text=" Rs-450 ").grid(row=6,column=1)
    ep1=Entry(piza,textvariable=svar5).grid(row=6,column=2)
    f=Checkbutton(piza,text=" Meatizza ",variable=var6).grid(row=7,column=0,sticky=W)
    fp=Label(piza,text=" Rs-600 ").grid(row=7,column=1)
    fp1=Entry(piza,textvariable=svar6).grid(row=7,column=2)
    def select():
        win.withdraw()
    
    finish=Button(piza,command=select,width=8,text="Finish",bd=15,relief='raised',bg='blue',fg='white').grid(row=8,column=1,pady=20)

def sides():
    win = Toplevel()
    win.title("Choose sides")
    side=Frame(win,width=400,height=200,bd=8,relief="raise")
    side.pack()
    sides=Label(side,text="Sides",font=('arial',20,'bold')).grid(row=0,column=0)
    price=Label(side,text="Price").grid(row=0,column=1)
    quan=Label(side,text=" Quantity ").grid(row=0,column=2)
    s1=Checkbutton(side,text="Lava Cake",variable=var7).grid(row=1,column=0,sticky=W)
    ps1=Label(side,text="Rs-100").grid(row=1,column=1)
    es1=Entry(side,textvariable=svar7).grid(row=1,column=2)
    s2=Checkbutton(side,text="Mountain Dew",variable=var8).grid(row=2,column=0,sticky=W)
    ps2=Label(side,text="Rs-40").grid(row=2,column=1)
    es2=Entry(side,textvariable=svar8).grid(row=2,column=2)
    s3=Checkbutton(side,text="Cheese Garlic Bread",variable=var9).grid(row=3,column=0,sticky=W)
    ps3=Label(side,text="Rs-80").grid(row=3,column=1)
    es3=Entry(side,textvariable=svar9).grid(row=3,column=2)
    def sb():
        win.withdraw()
    sideb=Button(side,command=sb,width=10,text="Continue").grid(row=4,column=0)
    
def cost():
    ve1=(svar1.get())
    ve2=(svar2.get())
    ve3=(svar3.get())
    nve1=(svar4.get())
    nve2=(svar5.get())
    nve3=(svar6.get())
    se1=(svar7.get())
    se2=(svar8.get())
    se3=(svar9.get())  
    e1=int((var1.get()))
    e2=int((var2.get()))
    e3=int((var3.get()))
    e4=int((var4.get()))
    e5=int((var5.get()))
    e6=int((var6.get()))
    e7=int((var7.get()))
    e8=int((var8.get()))
    e9=int((var9.get()))
    ptot=(ve1*v1*e1)+(ve2*v2*e2)+(ve3*v3*e3)+(nve1*nv1*e4)+(nve2*nv2*e5)+(nve3*nv3*e6)
    stot=(se1*s1*e7)+(se2*s2*e8)+(se3*s3*e9)
    gtot=(ptot+stot)
    gst=(0.05*gtot)
    new=str(d1.get())
    fbill=int(gtot+gst)
    show=Text(total,bg='dark blue',fg='white')
    show.insert(INSERT,"Your Order Details:-\n\n")
    if(e1==1):
        str1=d1.get()+" "+str(ve1)
        show.insert(INSERT,str1+"\n")
    if(e2==1):
        str1=d2.get()+" "+str(ve2)
        show.insert(INSERT,str1+"\n")
    if(e3==1):
        str1=d3.get()+" "+str(ve3)
        show.insert(INSERT,str1+"\n")
    if(e4==1):
        str1=d4.get()+" "+str(nve1)
        show.insert(INSERT,str1+"\n")
    if(e5==1):
        str1=d5.get()+" "+str(nve2)
        show.insert(INSERT,str1+"\n")
    if(e6==1):
        str1=d6.get()+" "+str(nve3)
        show.insert(INSERT,str1+"\n")
    if(e7==1):
        str1=d7.get()+" "+str(se1)
        show.insert(INSERT,str1+"\n")
    if(e8==1):
        str1=d8.get()+" "+str(se2)
        show.insert(INSERT,str1+"\n")
    if(e9==1):
        str1=d9.get()+" "+str(se3)
        show.insert(INSERT,str1+"\n")
        
    show.insert(INSERT,"\nYour total pizza cost: ")
    show.insert(INSERT,ptot)
    show.insert(INSERT,"\nYour side order cost: ")
    show.insert(INSERT,stot)
    show.insert(INSERT,"\nTotal cost: ")
    show.insert(INSERT,gtot)
    show.insert(INSERT,"\nGST: ")
    show.insert(INSERT,gst)
    show.insert(INSERT,"\nFinal Amount: ")
    show.insert(INSERT,fbill)
    show.grid(row=2,column=0)
    
# ----------------- Frames ------------------

mainF=Frame(root,bd=14,width=1200,height=800, relief="raise")
mainF.pack()

order=Frame(root,bd=18,width=500,height=300,relief="raise" )
#order.geometry("500x500+0+0")
order.pack(expand=1,side=LEFT)

total=Frame(root,bd=18,width=400,height=200, relief="raise")
total.pack(side=RIGHT,expand=1)

# ---------------- Buttons ------------------

b=Button(order,text="Choose Pizza",font=('arial',12, 'bold'), padx=16,bd=8,fg="white",bg="red",command=pizza)
b.grid(row=1,column=0,padx=20,pady=30)

b0=Button(order,text="Choose Sides",font=('arial',12, 'bold'), padx=16,bd=8,fg="white",bg="red",command=sides)
b0.grid(row=2,column=0,padx=20,pady=30)

final=Button(total,text="Show Bill",command=cost,bg='blue',fg='white',font=(14),bd=15).grid(row=1,column=0,pady=20)

Quit=Button(root,text="Exit",command=root.destroy,font=('arial',20,'bold')).pack(side=BOTTOM,pady=20)

# ------------------- Other --------------------

Heading=Label(mainF,text="Welcome to Python Pizza",font=('arial',40,'bold'))
Heading.pack(side=TOP,pady=10)

inv=Label(total,text="Invoice",font=('arial',25,'bold')).grid(row=0,column=0,padx=30,pady=40)
menu=Label(order,text="Place your order",font=('times',25,'bold')).grid(row=0,column=0,pady=10,padx=10)

root.mainloop()
