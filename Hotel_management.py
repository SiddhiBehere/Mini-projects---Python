#Hotel management system

from tkinter import *
from tkinter import ttk
from time import strftime
import sqlite3
import re

#GUI
window = Tk()
window.title("Siddhi's Hotel Management")
# window.geometry("800x600")
window.resizable(width=True, height=True)

#creating three Label frames

f2 = LabelFrame(window, text='Billing')
f2.pack(side='right', padx=10, pady=5, fill='both', expand=True)
f3 = LabelFrame(window,text="View")
f3.pack(side='bottom', padx=10, pady=5, fill='both', expand=True)
f1 = LabelFrame(window, text="Menu")
f1.pack(side='left',padx=10, pady=5, fill='both', expand=True)

#created to save selected menu items
def create():
    con = sqlite3.connect('Hotel_management.db') 
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Menu(cust_id INTEGER primary key autoincrement, Dish_veg TEXT,'
    'Dish_nonveg TEXT, Dish_drinks TEXT, Dish_desserts TEXT,Total INTEGER,table_no INTEGER,' 
    'sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)')
    con.commit()
    con.close()
create()

def comboclick1(event):
    label = Label(l3, text=drop1.get())
    label.pack()
def comboclick2(event):
    label = Label(l3, text=drop2.get())
    label.pack() 
def comboclick3(event):
    label = Label(l3,text=drop3.get())
    label.pack()
def comboclick4(event):
    label = Label(l3, text=drop4.get())
    label.pack()
# def comboclick5(event):
#     label = Label(f3, text=drop5.get())

dishes_veg = ['Pav Bhaji 90', 'Roti 30', 'Paneer Tikka 200','Pulav 150','Mushroom masala 190','Rice 70',
'Dosa 80','Idli 75','Manchurian 200','Soup 160','Paneer chilli 195', 'None 0']
drop1 = ttk.Combobox(f1, value=dishes_veg)
drop1.set("Veg(Price)")
a = drop1.bind("<<ComboboxSelected>>",comboclick1)
drop1.pack(side='top')
dishes_nonveg = ['Chicken Tikka 200', 'Egg curry 170', 'Fish Fry 250', 'Chicken Lolipops 200',
'Chicken soup 195','Butter chicken 230','Praws curry 180','Fish masala 230','Seek kabab 220',
'Crab curry 260', 'None 0']
drop2 = ttk.Combobox(f1, value=dishes_nonveg)
drop2.set("Non-Veg(Price)")
b = drop2.bind("<<ComboboxSelected>>",comboclick2)
drop2.pack(side='top')
dishes_drinks = ['Tea 20','Coffee 20','Cold coffee 35','Hot chocolate 50','Juice 40','Berry crush 35',
'Soda 40','Smoothies 50','Milkshake 50','Lemonade 45', 'Mocktails 60', 'None 0']
drop3 = ttk.Combobox(f1, value=dishes_drinks)
drop3.set("Beverages(Price)")
c = drop3.bind("<<ComboboxSelected>>",comboclick3)
drop3.pack(side='top')
dishes_desserts = ['Cake 300', 'Cheesecake 400', 'Brownie 150', 'Icecream 140', 'Pie 150', 'Cookies 150',
'Custard 180', 'Pudding 150','Pasteries 120', 'None 0']
drop4 = ttk.Combobox(f1, value=dishes_desserts)
drop4.set("Desserts(Price)")
d = drop4.bind("<<ComboboxSelected>>", comboclick4)
drop4.pack(side='top')
# payment = ['Cash', 'UPI', 'Debit card', 'Credit card']
# drop5 = ttk.Combobox(f2, value =payment)
# drop5.set("Payment Options")
# drop5.bind("<<ComboboxSelected>>", comboclick5)
# drop5.grid()


# text1 = (drop1.get())
# text2 = (drop2.get())
# text3 = (drop3.get())
# text4 = (drop4.get())
global counter
def cust_id():
    global counter
    counter = 1
    label1.config(text=counter)
    # counter += 1

label1 = Label(f2, text='Customer ID:')
label1.grid(row=1,column=1, sticky=W)
label1 = Label(f2)
label1.grid(row=1, column=2)

cust_id()
label2 = Label(f2, text='Table No:')
label2.grid(row=2,column=1,sticky=W)
entry2 = StringVar()
entry2 = Entry(f2, textvariable=entry2)
entry2.grid(row = 2, column=2)
frame = Frame(f2)
frame.grid()

def disp_time():
    time = strftime('%H:%M:%S %p \n %x \n %A')
    label4.config(text=time)

# label3 = StringVar()    
label3 = Label(f2, text='Time:\nDate:\nDay:')
label3.grid(row=3, column=1, sticky=W)
label4 = Label(f2)
label4.grid(row=3, column=2)
disp_time()
l3 = StringVar()
label5 = Label(f2, text="Menu selected:")
label5.grid(row=4, column=1, padx=6, pady=5)
l3 = Entry(f2,width=20,textvariable=l3)
l3.grid(row=6, column=1)
l4 = Label(f2)
l4.grid(row=10, column=1)
l5 = Label(f2)
l5.grid(row=11, column=1)
l6 = Label(f2)
l6.grid(row=12, column=1)

def done():
    para = '\d+'
    a = re.findall(para, drop1.get())
    b = re.findall(para, drop2.get())
    c = re.findall(para, drop3.get())
    d = re.findall(para, drop4.get())
    con = sqlite3.connect('Hotel_management.db') 
    cur = con.cursor()
    if drop1.get() == 'Veg(Price)' and drop2.get() == 'Non-Veg(Price)' and drop3.get() == 'Beverages(Price)' and drop4.get() == 'Desserts(Price)':
        l5.config(text="Please select something from Menu", fg='red')
        return
    a1 = [eval(i) for i in a]
    b1 = [eval(i) for i in b]
    c1 = [eval(i) for i in c]
    d1 = [eval(i) for i in d]
    # print(a1, b1, c1, d1)
    res = a1[0] + b1[0] + c1[0] + d1[0]
    cur.execute('INSERT INTO Menu(Dish_veg, Dish_nonveg, Dish_drinks, Dish_desserts, Total, table_no)' 
    'VALUES (?, ?, ?, ?, ?, ?)', (drop1.get(), drop2.get(), drop3.get(), drop4.get(),res, entry2.get()))
    if entry2.get() == '':
        l5.config(text="Please enter table number", fg='red')
        return
    con.commit()
    cur.execute('SELECT * FROM Menu')
    print(cur.fetchall())
    l5.config(text="Order placed successfully :)", fg='green')
    l8.config(text=res, fg='purple')
    l2.config(text=entry2.get())
    label4.config(text=disp_time())

# def next():
#     global counter
#     counter += 1
#     label1.config(text=counter)
#     entry2.delete(0, 'end')
#     l3.delete(0, 'end')

b1 = Button(l4, text="Close", width=6, height=1, borderwidth=3, command=window.destroy)
b1.pack(side='right', expand=True, pady=10, padx=10)
b = Button(l4, text="Done", width=6, height=1, borderwidth=3, command=done)
b.pack(side='left', expand=True, padx=10)
# b = Button(l4, text="Next", width=6, height=1, borderwidth=3, command=next)
# b.pack(side='right', expand=True, padx=10)
l7 = Label(f2, text="Total price:  Rs.", fg="purple")
l7.grid(row=14, column=1, sticky=W)
l8 = Label(f2)
l8.grid(row=14, column=2, sticky=W)
l9 = Label(f2)
l9.grid(row=15, column=1, sticky=W)

l1 = Label(f3, text="Table No.:",fg='dark blue')
l1.grid(row=1, column=1)
l2 = Label(f3,fg='dark blue')
l2.grid(row=1, column=2)
label3 = Label(f3, text='Time:\nDate:\nDay:', fg='dark blue')
label3.grid(row=3, column=1, sticky=W)
label4 = Label(f3, fg='dark blue')
label4.grid(row=3, column=2)
# disp_time()



window.mainloop()




