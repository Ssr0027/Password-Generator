from tkinter import *
import tkinter as tk
from tkinter.font import Font
import string
import random
import pyperclip

def gen():
    small_al=string.ascii_lowercase
    cap_al=string.ascii_uppercase
    num=string.digits
    spe=string.punctuation
    all=small_al+cap_al+num+spe
    pass_lenth=int (lenght_box.get())
    if choice.get()==1:
        passField.insert(0,random.sample(small_al+cap_al,pass_lenth))
    if choice.get()==2:
        passField.insert(0,random.sample(small_al+cap_al+num,pass_lenth))
    if choice.get()==3:
        passField.insert(0,random.sample(all,pass_lenth))
def copy():
    password=passField.get()
    pyperclip.copy(password)


 

root=Tk()
root.title("SHEIELD")
root.geometry("700x700")
root.resizable(False, False)
root.configure(bg="gray40")

header = tk.Frame(root, bg="wheat1")
header.place(x=0, y=10, height=70, width=700)


heading = Label(root, text="Generate a Password", font=("Times New Roman", 40, "bold"),bg="wheat1")
heading.place(x=150, y=19)


choice = IntVar()


button1=Radiobutton(root,text="Weak",value=1,variable=choice,font=("arial",20,"bold"), height=2, width=20)
button1.place(x=225,y=120)

button2=Radiobutton(root,text="Medium",value=2,variable=choice,font=("arial",20,"bold"), height=2, width=20)
button2.place(x=225,y=200)

button3=Radiobutton(root,text="Strong",value=3,variable=choice,font=("arial",20,"bold"), height=2, width=20)
button3.place(x=225,y=280)

label1=Label(root,text="Lenght of Password: ",font=("Times 20 italic bold",40,"bold"),bg='gray40')
label1.place(x=160,y=335)

lenght_box=Spinbox(root,from_=5,to_=20,width=18,font="Ariel")
lenght_box.place(x=255,y=400)

button3=Button(root,text="Start Generating",font=("arial",22,"bold"), height=2, width=18,command=gen)
button3.place(x=210,y=440)

passField=Entry(root,width=33,bd=2)
passField.place(x=188,y=520)

button4=Button(root,text="Copy Password",font=("arial",22,"bold"), height=2, width=18,command=copy)
button4.place(x=210,y=563)


root.mainloop()