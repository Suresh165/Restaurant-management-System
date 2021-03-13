from tkinter import*
import random
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management Systems")

text_Input = StringVar()
operator =""

Tops = Frame(root, width = 1600,height = 50,bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800,height = 700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300,height = 700, relief=SUNKEN)
f2.pack(side=RIGHT)
#======================================Time==================================
localtime=time.asctime(time.localtime(time.time()))
#================================================Info=============================
lblInfo = Label(Tops, font=('arial',40,'bold'),text=" SUMIT Restaurant Managment System",fg="steel Blue", bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
lblInfo = Label(Tops, font=('arial',20,'bold'),text=localtime,fg="steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1,column=0)
#======================================Calculator====================================
def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualaInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

def Ref():
    x = random.randint(10908,500876)
    randomRef = str(x)
    rand.set(randomRef)

    CoF =float(Fries.get())
    CoD =float(Drinks.get())
    CoPanir_Pizza =float(Panir_Pizza.get())
    CoBurger =float(Burger.get())
    CoChicken_Burger =float(Chicken_Burger.get())
    CoCheese_Burger =float(Cheese_Burger.get())

    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofPanir_Pizza = CoPanir_Pizza * 2.99
    CostofBurger = CoBurger * 2.99
    CostofChicken_Burger = CoChicken_Burger * 2.89
    CostofCheese_Burger = CoCheese_Burger * 2.69

    CostofMeal = "£", str('%.2f' % (CostofFries + CostofDrinks + CostofPanir_Pizza + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger))

    PayTax = ((CostofFries + CostofDrinks + CostofPanir_Pizza + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofPanir_Pizza + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofPanir_Pizza + CostofBurger
                                    + CostofChicken_Burger + CostofCheese_Burger)/99)

    Service = "£", str('%.2f' % Ser_Charge)
    OverAllCost ="£", str('%.2f' %  (PayTax + TotalCost + Ser_Charge))
    PaidTax = "£", str('%.2f' % PayTax)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    StateTax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def qExit():
    root.destroy()

def Reset():
    rand.set("")
    Fries.set("")
    Burger.set("")
    Panir_Pizza.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Chicken_Burger.set("")
    Cheese_Burger.set("")
    StateTax.set("")
    TotalCost.set("")

    
    
textDisplay = Entry(f2,font=('arial',20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                  bg="powder blue", justify='right')

textDisplay.grid(columnspan=4)

btn7=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="7", bg="powder blue",command=lambda:btnclick(7)).grid(row=1,column=0)

btn8=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="8", bg="powder blue",command=lambda:btnclick(8)).grid(row=1,column=1)

btn9=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="9", bg="powder blue",command=lambda:btnclick(9)).grid(row=1,column=2)

Addition=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="+", bg="powder blue",command=lambda:btnclick("+")).grid(row=1,column=3)
#==================================================================================
btn4=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="4", bg="powder blue",command=lambda:btnclick(4)).grid(row=2,column=0)

btn5=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="5", bg="powder blue",command=lambda:btnclick(5)).grid(row=2,column=1)

btn6=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="6", bg="powder blue",command=lambda:btnclick(6)).grid(row=2,column=2)

Subtraction=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="-", bg="powder blue",command=lambda:btnclick("-")).grid(row=2,column=3)

#================================================================================
btn1=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="1", bg="powder blue",command=lambda:btnclick(1)).grid(row=3,column=0)

btn2=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="2", bg="powder blue",command=lambda:btnclick(2)).grid(row=3,column=1)
                      
btn3=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="3", bg="powder blue",command=lambda:btnclick(3)).grid(row=3,column=2)

Multiply=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="*", bg="powder blue",command=lambda:btnclick("*")).grid(row=3,column=3)

#==============================================================================
btn0=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="0", bg="powder blue",command=lambda:btnclick(0)).grid(row=4,column=0)

btnClear=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="c", bg="powder blue",command=btnClearDisplay).grid(row=4,column=1)

btnequals=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="=", bg="red",command= btnEqualaInput).grid(row=4,column=2)

Division=Button(f2,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),
            text="/", bg="powder blue",command=lambda:btnclick("/")).grid(row=4,column=3)

#----------------------------Restaurant Info 1------------------------------------------------
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Panir_Pizza = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken_Burger = StringVar()
Cheese_Burger = StringVar()
StateTax = StringVar()
TotalCast = StringVar()

lblReference = Label(f1,font=('arial',16,'bold'),text="Reference", bd=16,anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'), textvariable=rand,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtReference.grid(row=0,column=1)

lblFries = Label(f1,font=('arial',16,'bold'),text="Large_Fries", bd=16,anchor='w')
lblFries.grid(row=1,column=0)
txtFries=Entry(f1,font=('arial',16,'bold'), textvariable=Fries,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtFries.grid(row=1,column=1)

lblBurger = Label(f1,font=('arial',16,'bold'),text="Burger", bd=16,anchor='w')
lblBurger.grid(row=2,column=0)
txtBurger=Entry(f1,font=('arial',16,'bold'), textvariable=Burger,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtBurger.grid(row=2,column=1)

lblPanir_Pizza = Label(f1,font=('arial',16,'bold'),text="Panir_Pizza", bd=16,anchor='w')
lblPanir_Pizza.grid(row=3,column=0)
txtPanir_Pizza=Entry(f1,font=('arial',16,'bold'), textvariable=Panir_Pizza,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtPanir_Pizza.grid(row=3,column=1)

lblChicken_Burger = Label(f1,font=('arial',16,'bold'),text="Chicken_Burger", bd=16,anchor='w')
lblChicken_Burger.grid(row=4,column=0)
txtChicken_Burger=Entry(f1,font=('arial',16,'bold'), textvariable=Chicken_Burger,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtChicken_Burger.grid(row=4,column=1)

lblCheese_Burger = Label(f1,font=('arial',16,'bold'),text="Cheese_Burger", bd=16,anchor='w')
lblCheese_Burger.grid(row=5,column=0)
txtCheese_Burger=Entry(f1,font=('arial',16,'bold'), textvariable=Cheese_Burger,bd=10,insertwidth=4,
                   bg="powder blue", justify = 'right')
txtCheese_Burger.grid(row=5,column=1)
#----------------------------Restaurant Info 2------------------------------------------------
lblDrinks = Label(f1,font=('arial',16,'bold'),text="Drinks", bd=16,anchor='w')
lblDrinks.grid(row=0,column=2)
txtDrinks=Entry(f1,font=('arial',16,'bold'), textvariable=Drinks,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtDrinks.grid(row=0,column=3)

lblCost = Label(f1,font=('arial',16,'bold'),text="Cost", bd=16,anchor='w')
lblCost.grid(row=1,column=2)
txtCost=Entry(f1,font=('arial',16,'bold'), textvariable=Cost,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtCost.grid(row=1,column=3)

lblService_Charge = Label(f1,font=('arial',16,'bold'),text="Service_Charge", bd=16,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge=Entry(f1,font=('arial',16,'bold'), textvariable=Service_Charge,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtService_Charge.grid(row=2,column=3)

lblStateTax = Label(f1,font=('arial',16,'bold'),text="StateTax", bd=16,anchor='w')
lblStateTax.grid(row=3,column=2)
txtStateTax=Entry(f1,font=('arial',16,'bold'), textvariable=StateTax,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtStateTax.grid(row=3,column=3)

lblSubTotal = Label(f1,font=('arial',16,'bold'),text="SubTotal", bd=16,anchor='w')
lblSubTotal.grid(row=4,column=2)
txtSubTotal=Entry(f1,font=('arial',16,'bold'), textvariable=SubTotal,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtSubTotal.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('arial',16,'bold'),text="TotalCost", bd=16,anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost=Entry(f1,font=('arial',16,'bold'), textvariable=Total,bd=10,insertwidth=4,
                   bg="#ffffff", justify = 'right')
txtTotalCost.grid(row=5,column=3)
#=======================================Buttons===============================================
btnTotal=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="total", bg="powder blue",command = Ref).grid(row=7,column=1)

btnReset=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Reset", bg="powder blue",command = Reset).grid(row=7,column=2)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Exit", bg="powder blue",command = qExit).grid(row=7,column=3)


root.mainloop() 
