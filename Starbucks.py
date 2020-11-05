from tkinter import *

root=Tk()
root.geometry("1350x750+0+0")
root.title("/t Starbucks /t")
root.configure(background='black')

# *************** Variables ***************

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

GSTPaid=IntVar()
SubTotal=IntVar()
TotalCost=IntVar()
CostOfDrinks=IntVar()
CostOfCakes=IntVar()

E_WhiteMocha=IntVar()
E_Cappuccino=IntVar()
E_Frappuccino=IntVar()
E_Espresso=IntVar()
E_Macchiato=IntVar()
E_DevilsOwn=IntVar()
E_JavaChip=IntVar()
E_Latte=IntVar()
E_CoffeeCake=IntVar()
E_RedVelvetCake=IntVar()
E_SwissChocolateCake=IntVar()
E_NewYorkCheesecake=IntVar()
E_LemonCheesecake=IntVar()
E_WhiteForestCake=IntVar()
E_LindtMarshmallowCake=IntVar()
E_MarbleCake=IntVar()

d1=100
d2=200
d3=400
d4=300
d5=150
d6=250
d7=350
d8=450
c1=200
c2=250
c3=150
c4=300
c5=270
c6=350
c7=400
c8=500

# -------------Functions------------

def qExit():
    root.destroy()

def qReset():
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    
    E_WhiteMocha.set(0)
    E_Cappuccino.set(0)
    E_Frappuccino.set(0)
    E_Espresso.set(0)
    E_Macchiato.set(0)
    E_DevilsOwn.set(0)
    E_JavaChip.set(0)
    E_Latte.set(0)
    E_CoffeeCake.set(0)
    E_RedVelvetCake.set(0)
    E_SwissChocolateCake.set(0)
    E_NewYorkCheesecake.set(0)
    E_LemonCheesecake.set(0)
    E_WhiteForestCake.set(0)
    E_LindtMarshmallowCake.set(0)
    E_MarbleCake.set(0)
    
    GSTPaid.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostOfDrinks.set("")
    CostOfCakes.set("")
    txtReceipt = Text(ft2, width=59,height=22,bg="white", bd=8, font=('arial',12, 'bold'))
    txtReceipt.grid(row=1,column=0)

def CostOfItem():
    txtReceipt = Text(ft2, width=59,height=22,bg="white", bd=8, font=('arial',12, 'bold'))
    txtReceipt.grid(row=1,column=0)

    Item1=(E_WhiteMocha.get())
    Item2=(E_Cappuccino.get())
    Item3=(E_Frappuccino.get())
    Item4=(E_Espresso.get())
    Item5=(E_Macchiato.get())
    Item6=(E_DevilsOwn.get())
    Item7=(E_JavaChip.get())
    Item8=(E_Latte.get())
    Item9=(E_CoffeeCake.get())
    Item10=(E_RedVelvetCake.get())
    Item11=(E_SwissChocolateCake.get())
    Item12=(E_NewYorkCheesecake.get())
    Item13=(E_LemonCheesecake.get())
    Item14=(E_WhiteForestCake.get())
    Item15=(E_LindtMarshmallowCake.get())
    Item16=(E_MarbleCake.get())
    
    e1=var1.get()    
    e2=var2.get()
    e3=var3.get()
    e4=var4.get()
    e5=var5.get()
    e6=var6.get()
    e7=var7.get()
    e8=var8.get()  
    e9=var9.get()
    e10=var10.get()
    e11=var11.get()
    e12=var12.get()
    e13=var13.get()
    e14=var14.get()
    e15=var15.get()
    e16=var16.get()
    
    txtReceipt.insert(INSERT,"Your Order Details:-\n")
    
    if(e1==1):
        txtReceipt.insert(INSERT,"\nWhite Mocha "+str(Item1))
    if(e2==1):
        txtReceipt.insert(INSERT,"\nCappuccino "+str(Item2))
    if(e3==1):
        txtReceipt.insert(INSERT,"\nFrappuccino "+str(Item3))
    if(e4==1):
        txtReceipt.insert(INSERT,"\nEspresso "+str(Item4))
    if(e5==1):
        txtReceipt.insert(INSERT,"\nMacchiato "+str(Item5))
    if(e6==1):
        txtReceipt.insert(INSERT,"\nDevils Own "+str(Item6))
    if(e7==1):
        txtReceipt.insert(INSERT,"\nJava Chip "+str(Item7))
    if(e8==1):
        txtReceipt.insert(INSERT,"\nLatte "+str(Item8))
    if(e9==1):
        txtReceipt.insert(INSERT,"\nCoffee Cake "+str(Item9))
    if(e10==1):
        txtReceipt.insert(INSERT,"\nRed Velvet Cake "+str(Item10))
    if(e11==1):
        txtReceipt.insert(INSERT,"\nSwiss Chocolate Cake "+str(Item11))
    if(e12==1):
        txtReceipt.insert(INSERT,"\nNew York Cheesecake "+str(Item12))
    if(e13==1):
        txtReceipt.insert(INSERT,"\nLemon Cheesecake "+str(Item13))
    if(e14==1):
        txtReceipt.insert(INSERT,"\nWhite Forest Cake "+str(Item14))
    if(e15==1):
        txtReceipt.insert(INSERT,"\nLindt Marshmallow Cake "+str(Item15))
    if(e16==1):
        txtReceipt.insert(INSERT,"\nMarble Cake "+str(Item16))
    
    PriceofDrinks=(e1*d1*Item1)+(e2*d2*Item2)+(e3*d3*Item3)+(e4*d4*Item4)+(e5*d5*Item5)+(e6*d6*Item6)+(e7*d7*Item7)+(e8*d8*Item8)
    CostOfDrinks.set(PriceofDrinks)
    PriceofCakes=(e9*c1*Item9)+(e10*c2*Item10)+(e11*c3*Item11)+(e12*c4*Item12)+(e13*c5*Item13)+(e14*c6*Item14)+(e15*c7*Item15)+(e16*c8*Item16)
    CostOfCakes.set(PriceofCakes)
    stot=PriceofDrinks+PriceofCakes
    gst=0.05*stot
    tot=gst+stot
    GSTPaid.set(gst)
    SubTotal.set(stot)
    TotalCost.set(tot)
    txtReceipt.insert(INSERT,"\n\nTotal Cost: "+str(tot))

# ***************** Frames *****************

topFrame=Frame(root, width=1350, height=100, bd=14, relief="raise")
topFrame.pack(side=TOP)

f1=Frame(root, width=440, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)

f2=Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)

f2a=Frame(f1, width=900, height=320, bd=6, relief="raise")
f2a.pack(side=BOTTOM)

ft2=Frame(f2, width=440, height=650, bd=12, relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2, width=440, height=50, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa=Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)
f1ab=Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)
f2ab=Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

topFrame.configure(background='black')
f1.configure(background='black')
f2.configure(background='black')

lblinfo= Label(topFrame ,font=('arial',70, 'bold'), text="Starbucks")
lblinfo.grid(row=0,column=0)
 
# *************** CheckButtons ***************

WhiteMocha= Checkbutton(f1aa, text="White Mocha", variable=var1, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=0,sticky=W)
Cappuccino= Checkbutton(f1aa, text="Cappuccino", variable=var2, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=1,sticky=W)
Frappuccino= Checkbutton(f1aa, text="Frappuccino", variable=var3, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=2,sticky=W)
Espresso= Checkbutton(f1aa, text="Espresso", variable=var4, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=3,sticky=W)
Macchiato= Checkbutton(f1aa, text="Macchiato", variable=var5, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=4,sticky=W)
DevilsOwn= Checkbutton(f1aa, text="Devils Own", variable=var6, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=5,sticky=W)
JavaChip= Checkbutton(f1aa, text="Java Chip", variable=var7, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=6,sticky=W)
Latte= Checkbutton(f1aa, text="Latte", variable=var8, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=7,sticky=W)
CoffeeCake= Checkbutton(f1ab, text="Coffee Cake", variable=var9, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=0,sticky=W)
RedVelvetCake= Checkbutton(f1ab, text="Red Velvet Cake", variable=var10, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=1,sticky=W)
SwissChocolateCake= Checkbutton(f1ab, text="Swiss Chocolate Cake", variable=var11, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=2,sticky=W)
NewYorkCheesecake= Checkbutton(f1ab, text="New York Cheesecake", variable=var12, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=3,sticky=W)
LemonCheesecake= Checkbutton(f1ab, text="Lemon Cheesecake", variable=var13, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=4,sticky=W)
WhiteForestCake= Checkbutton(f1ab, text="White Forest Cake", variable=var14, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=5,sticky=W)
LindtMarshmallowCake= Checkbutton(f1ab, text="Lindt Marshmallow Cake", variable=var15, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=6,sticky=W)
MarbleCake= Checkbutton(f1ab, text="Marble Cake", variable=var16, onvalue=1, offvalue=0, font=('arial',18, 'bold')).grid(row=7,sticky=W)

# *************** Entry Fields ***************

txtWhiteMocha = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_WhiteMocha ,justify='left',state=NORMAL)
txtWhiteMocha.grid(row=0,column=1)
txtCappuccino = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_Cappuccino ,justify='left',state=NORMAL)
txtCappuccino.grid(row=1,column=1)
txtFrappuccino = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_Frappuccino, justify='left',state=NORMAL)
txtFrappuccino.grid(row=2,column=1)
txtEspresso = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_Espresso, justify='left',state=NORMAL)
txtEspresso.grid(row=3,column=1)
txtMacchiato = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_Macchiato, justify='left',state=NORMAL)
txtMacchiato.grid(row=4,column=1)
txtDevilsOwn = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_DevilsOwn, justify='left',state=NORMAL)
txtDevilsOwn.grid(row=5,column=1)
txtJavaChip = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_JavaChip, justify='left',state=NORMAL)
txtJavaChip.grid(row=6,column=1)
txtLatte = Entry(f1aa,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_Latte, justify='left',state=NORMAL)
txtLatte.grid(row=7,column=1)
txtCoffeeCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_CoffeeCake ,justify='left',state=NORMAL)
txtCoffeeCake.grid(row=0,column=1)
txtRedVelvetCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_RedVelvetCake ,justify='left',state=NORMAL)
txtRedVelvetCake.grid(row=1,column=1)
txtSwissChocolateCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_SwissChocolateCake ,justify='left',state=NORMAL)
txtSwissChocolateCake.grid(row=2,column=1)
txtNewYorkCheesecake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_NewYorkCheesecake ,justify='left',state=NORMAL)
txtNewYorkCheesecake.grid(row=3,column=1)
txtLemonCheesecake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_LemonCheesecake ,justify='left',state=NORMAL)
txtLemonCheesecake.grid(row=4,column=1)
txtWhiteForestCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_WhiteForestCake ,justify='left',state=NORMAL)
txtWhiteForestCake.grid(row=5,column=1)
txtLindtMarshmallowCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_LindtMarshmallowCake ,justify='left',state=NORMAL)
txtLindtMarshmallowCake.grid(row=6,column=1)
txtMarbleCake = Entry(f1ab,font=('arial',16, 'bold'), bd=8, width=6,textvariable=E_MarbleCake ,justify='left',state=NORMAL)
txtMarbleCake.grid(row=7,column=1)

# *************** Receipts ***************

lblReceipt = Label(ft2, font=('arial',12, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0,column=0,sticky=W) 
txtReceipt0 = Text(ft2, width=59,height=22,bg="white", bd=8, font=('arial',12, 'bold'))
txtReceipt0.grid(row=1,column=0)

# *************** Buttons ***************

btnTotal = Button(fb2, text="Receipt", font=('arial',12, 'bold'),width=5, padx=16,pady=1,bd=4,fg="white",bg="black",command=CostOfItem)
btnTotal.grid(row=0,column=0)
btnReset = Button(fb2, text="Reset", font=('arial',12, 'bold'),width=5, padx=16,pady=1,bd=4,fg="white",bg="black",command=qReset)
btnReset.grid(row=0,column=1)
btnExit = Button(fb2, text="Exit", font=('arial',12, 'bold'),width=5, padx=16,pady=1,bd=4,fg="white",bg="black",command=qExit)
btnExit.grid(row=0,column=2)

# *************** Cost Information ***************

lblCostOfDrinks= Label(f2aa,text="Cost Of Drinks",font=('arial',16, 'bold'),bd=8, justify='left')
lblCostOfDrinks.grid(row=0,column=0,sticky=W)
txtCostOfDrinks= Entry(f2aa,font=('arial',16, 'bold'),bd=8,insertwidth=2, justify='left',textvariable=CostOfDrinks)
txtCostOfDrinks.grid(row=0,column=1,sticky=W)
lblCostOfCakes= Label(f2aa,text="Cost Of Cakes",font=('arial',16, 'bold'),bd=8, justify='left')
lblCostOfCakes.grid(row=1,column=0,sticky=W)
txtCostOfCakes= Entry(f2aa,font=('arial',16, 'bold'),bd=8,insertwidth=2, justify='left',textvariable=CostOfCakes)
txtCostOfCakes.grid(row=1,column=1,sticky=W)

# *************** Payment Information ***************

lblGSTPaid= Label(f2ab,text="GST",font=('arial',16, 'bold'),bd=8, justify='left')
lblGSTPaid.grid(row=0,column=0,sticky=W)
txtGSTPaid= Entry(f2ab,font=('arial',16, 'bold'),bd=8,insertwidth=2, justify='left',textvariable=GSTPaid)
txtGSTPaid.grid(row=0,column=1,sticky=W)
lblSubTotal= Label(f2ab,text="Sub Total",font=('arial',16, 'bold'),bd=8, justify='left')
lblSubTotal.grid(row=1,column=0,sticky=W)
txtSubTotal= Entry(f2ab,font=('arial',16, 'bold'),bd=8,insertwidth=2, justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=1,column=1,sticky=W)

root.mainloop()