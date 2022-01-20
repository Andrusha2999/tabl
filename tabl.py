from tkinter import *
def uus_aken(ind:int):
    if askyesno("Küsimus","kas teen lahti?"):
        showinfo("vastus","Teen lahti aken")
    else:
        showinfo("Vastus","Panen kinnu aken")
        aken.destroy()
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=[]
    textn=[]
    tab=[]

root=Tk()
Button(text="uroki LogITpv21").grid(row=0,column=1)
Button(text="Понедельник").grid(row=1,column=1)
Button(text="Вторник").grid(row=2,column=1)
Button(text="Среда").grid(row=3,column=1)
Button(text="Четверг").grid(row=4,column=1)
Button(text="Пятница").grid(row=5,column=1)
Button(text="Суббота").grid(row=6,column=1)
Button(text="Воскресенье").grid(row=7,column=1)
Button(text="1").grid(row=0,column=2)
Button(text="2").grid(row=0,column=3)
Button(text="3").grid(row=0,column=4)
Button(text="4").grid(row=0,column=5)
Button(text="5").grid(row=0,column=6)
Button(text="6").grid(row=0,column=7)
Button(text="7").grid(row=0,column=8)
Button(text="8").grid(row=0,column=9)
Button(text="9").grid(row=0,column=10)
Button(text="10").grid(row=0,column=11)

#дни недели (понедельник-пятница)
Button(text="Logistika",relief=RIDGE,font="times_new_roman 21",bg="#61b356",width=20,height=4).grid(row=1,column=3,columnspan=2) 
Button(text="Matem",relief=RIDGE,font="times_new_roman 21",bg="#d446c1",width=20,height=4).grid(row=1,column=5,columnspan=2)
Button(text="Pereriv4ik",font="times_new_roman 21",bg="thistle",width=20,height=4).grid(row=1,column=7)
Button(text="Russky",relief=RIDGE,font="times_new_roman 21",bg="#a33939",width=20,height=4).grid(row=1,column=8,columnspan=2)



Button(text="Program",relief=RIDGE,font="times_new_roman 21",bg="#46cfd4",width=32,height=4).grid(row=2,column=3,columnspan=3)
Button(text="Pereriv4ik",font="times_new_roman 21",bg="thistle",width=12,height=4).grid(row=2,column=6)
Button(text="Fizika",relief=RIDGE,font="times_new_roman 21",bg="#f24444",width=18,height=4).grid(row=2,column=7,columnspan=2)


Button(text="Iskustvo",relief=RIDGE,font="times_new_roman 21",bg="#8427a1",width=18,height=4).grid(row=3,column=3,columnspan=2)
Button(text="Pereriv4ik",font="times_new_roman 21",bg="thistle",width=8,height=4).grid(row=3,column=5)
Button(text="Fizra",relief=RIDGE,font="times_new_roman 21",bg="#dfed18",width=18,height=4).grid(row=3,column=6,columnspan=2)


Button(text="Logistika",relief=RIDGE,font="times_new_roman 21",bg="#61b356",width=18,height=4).grid(row=4,column=2,columnspan=2)
Button(text="Pereriv4ik",font="times_new_roman 21",bg="thistle",width=8,height=4).grid(row=4,column=4)
Button(text="Program",relief=RIDGE,font="times_new_roman 21",bg="#46cfd4",width=18,height=4).grid(row=4,column=5,columnspan=2)
Button(text="Rakendus",relief=RIDGE,font="times_new_roman 21",bg="#b50909",width=18,height=4).grid(row=4,column=7,columnspan=2)
Button(text="Eesti",relief=RIDGE,font="times_new_roman 21",bg="#a0b0ac",width=16,height=4).grid(row=4,column=9,columnspan=2)



Button(text="Rakendus",relief=RIDGE,font="times_new_roman 21",bg="#b50909",width=18,height=4).grid(row=5,column=2,columnspan=2)
Button(text="Program",relief=RIDGE,font="times_new_roman 21",bg="#46cfd4",width=70,height=4).grid(row=5,column=4,columnspan=5)
Button(text="Inglisse",relief=RIDGE,font="times_new_roman 21",bg="#9df268",width=16,height=4).grid(row=5,column=9,columnspan=2)














root.mainloop()