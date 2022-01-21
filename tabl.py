from tkinter import*
root=Tk()
def uus_aken(ind:int):
    if askyesno("Küsimus","kas teen lahti?"):
        showinfo("vastus","Teen lahti aken")
    else:
        showinfo("Vastus","Panen kinnu aken")
        aken.destroy()
    uusaken=Toplevel() #
    tabs=ttk.Notebook(uusaken)
    texts=[]
    textn=[]
    tab=[]
Button(text="Raspisanie urokov",font="Arial 15").grid(row=0,column=0)
Button(text="Esmaspäev",relief="flat",font="times_new_roman 15").grid(row=1,column=0)
Button(text="Teisipäev",relief="flat",font="times_new_roman 15").grid(row=2,column=0)
Button(text="Kolmapäev",relief="flat",font="times_new_roman 15").grid(row=3,column=0)
Button(text="Neljapäev",relief="flat",font="times_new_roman 15").grid(row=4,column=0)
Button(text="Reede",relief="flat",font="times_new_roman 15").grid(row=5,column=0)
Button(text="0",relief="flat",font="times_new_roman 15").grid(row=0,column=1)
Button(text="1",relief="flat",font="times_new_roman 15").grid(row=0,column=2)
Button(text="2",relief="flat",font="times_new_roman 15").grid(row=0,column=3)
Button(text="3",relief="flat",font="times_new_roman 15").grid(row=0,column=4)
Button(text="4",relief="flat",font="times_new_roman 15").grid(row=0,column=5)
Button(text="5",relief="flat",font="times_new_roman 15").grid(row=0,column=6)
Button(text="6",relief="flat",font="times_new_roman 15").grid(row=0,column=7)
Button(text="7",relief="flat",font="times_new_roman 15").grid(row=0,column=8)
Button(text="8",relief="flat",font="times_new_roman 15").grid(row=0,column=9)
Button(text="9",relief="flat",font="times_new_roman 15").grid(row=0,column=10)
Button(text="10",relief="flat",font="times_new_roman 15").grid(row=0,column=11)

#дни недели(понедельник-пятница)
Button(text="Logistik",relief="flat",font="times_new_roman 15 ",bg="#61b356",width=30,height=3).grid(row=1,column=3,columnspan=2)
Button(text="Matem",relief="flat",font="times_new_roman 15",bg="#d446c1",width=30,height=3).grid(row=1,column=5,columnspan=2)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=1,column=7)
Button(text="Russky",relief=RIDGE,font="times_new_roman 15",bg="#a33939",width=30,height=3).grid(row=1,column=8,columnspan=2)

Button(text="Programm",relief="flat",font="times_new_roman 15",bg="#46cfd4",width=45,height=3).grid(row=2,column=3,columnspan=3)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=2,column=6)
Button(text="Fizika",relief="flat",font="times_new_roman 15",bg="#f24444",width=30,height=3).grid(row=2,column=7,columnspan=2)


Button(text="Iskustvo",relief="flat",font="times_new_roman 15",bg="#8427a1",width=30,height=3).grid(row=3,column=3,columnspan=2)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=3,column=5)
Button(text="Fizra",relief="flat",font="times_new_roman 15",bg="#dfed18",width=30,height=3).grid(row=3,column=6,columnspan=2)

Button(text="Logistik",relief="flat",font="times_new_roman 15",bg="#61b356",width=30,height=3).grid(row=4,column=2,columnspan=2)
Button(text="Pereriv4ik",font="Arial 15",bg="thistle",width=15,height=3).grid(row=4,column=4)
Button(text="Programm",relief="flat",font="times_new_roman 15",bg="#46cfd4",width=30,height=3).grid(row=4,column=5,columnspan=2)
Button(text="Rakend",relief="flat",font="times_new_roman 15",bg="#b50909",width=30,height=3).grid(row=4,column=7,columnspan=2)
Button(text="Eesti",relief="flat",font="times_new_roman 15",bg="#a0b0ac",width=30,height=3).grid(row=4,column=9,columnspan=2)


Button(text="Rakendus",relief="flat",font="times_new_roman 15",bg="#9e0e0e",width=30,height=3).grid(row=5,column=2,columnspan=2)
Button(text="Programm",relief="flat",font="times_new_roman 15",bg="#46cfd4",width=80,height=3).grid(row=5,column=4,columnspan=5)
Button(text="Inglish",relief="flat",font="times_new_roman 15",bg="#9df268",width=30,height=3).grid(row=5,column=9,columnspan=2)





root.mainloop()