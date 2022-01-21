from tkinter import*
root=Tk()
root.geometry("1800x1000+100+100")
root.resizable(width=False, height=False)
root.title("Raspisanie urokov")


def Eesti():
  label.configure(text="Olesja-Ojamäe B_234(Estonskiy)",font="times_new_roman 15")
def Logistik():
  label.configure(text="Klimanskaja-Inessa B_002(Logistik)",font="times_new_roman 15")
def Matem():
  label.configure(text="Voronova-Nadezda B_133(Matematik)",font="times_new_roman 15")
def Russky():
  label.configure(text="Mihhailova-Ljudmila B_221(Russky)",font="times_new_roman 15")
def Programm():
  label.configure(text="Oleinik-Marina E_korpus07(Programm)",font="times_new_roman 15")
def Fizika():
  label.configure(text="Voronova-Nadezda B_133(Fizika)",font="times_new_roman 15")
def Inglish():
  label.configure(text="Borodina-Olga B_227(Inglish)",font="times_new_roman 15")
def Iskustvo():
  label.configure(text="Norkevitð-Aleksandra B_232 (Iskustvo)",font="times_new_roman 15")
def Fizra():
  label.configure(text="Maksõmiv-Maksim Zal_A (Fizra)",font="times_new_roman 15")
def Rakendus():
  label.configure(text="Merkulova-Irina E_10(Rakendus)",font="times_new_roman 15")
label = Label(root)
label.place(x=800, y=700)




Button(text="Raspisanie urokov",font="times_new_roman 15").grid(row=0,column=0)
Button(text="Понедельник",relief=RIDGE,font="times_new_roman 15").grid(row=1,column=0)
Button(text="Вторник",relief=RIDGE,font="times_new_roman 15").grid(row=2,column=0)
Button(text="Среда",relief=RIDGE,font="times_new_roman 15").grid(row=3,column=0)
Button(text="четверг",relief=RIDGE,font="times_new_roman 15").grid(row=4,column=0)
Button(text="Пятница",relief=RIDGE,font="times_new_roman 15").grid(row=5,column=0)
Button(text="0",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=1)
Button(text="1",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=2)
Button(text="2",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=3)
Button(text="3",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=4)
Button(text="4",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=5)
Button(text="5",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=6)
Button(text="6",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=7)
Button(text="7",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=8)
Button(text="8",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=9)
Button(text="9",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=10)
Button(text="10",relief=RIDGE,font="times_new_roman 15").grid(row=0,column=11)

#дни недели(понедельник-пятница)
Button(text="Logistik",relief=RIDGE,font="times_new_roman 15 ",bg="#61b356",width=30,height=3,command=Logistik).grid(row=1,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="Matem",relief=RIDGE,font="times_new_roman 15",bg="#d446c1",width=30,height=3,command=Matem).grid(row=1,column=5,columnspan=2,sticky=W+E+N+S)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=1,column=7,sticky=W+E+N+S)
Button(text="Russky",relief=RIDGE,font="times_new_roman 15",bg="#a33939",width=30,height=3,command=Russky).grid(row=1,column=8,columnspan=2,sticky=W+E+N+S)

Button(text="Programm",relief=RIDGE,font="times_new_roman 15",bg="#46cfd4",width=45,height=3,command=Programm).grid(row=2,column=3,columnspan=3,sticky=W+E+N+S)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=2,column=6,sticky=W+E+N+S)
Button(text="Fizika",relief=RIDGE,font="times_new_roman 15",bg="#f24444",width=30,height=3,command=Fizika).grid(row=2,column=7,columnspan=2,sticky=W+E+N+S)


Button(text="Iskustvo",relief=RIDGE,font="times_new_roman 15",bg="#8427a1",width=30,height=3,command=Iskustvo).grid(row=3,column=3,columnspan=2,sticky=W+E+N+S)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=3,column=5,sticky=W+E+N+S)
Button(text="Fizra",relief=RIDGE,font="times_new_roman 15",bg="#dfed18",width=30,height=3,command=Fizra).grid(row=3,column=6,columnspan=2,sticky=W+E+N+S)

Button(text="Logistik",relief=RIDGE,font="times_new_roman 15",bg="#61b356",width=30,height=3,command=Logistik).grid(row=4,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="Pereriv4ik",font="times_new_roman 15",bg="thistle",width=15,height=3).grid(row=4,column=4,sticky=W+E+N+S)
Button(text="Programm",relief=RIDGE,font="times_new_roman 15",bg="#46cfd4",width=30,height=3,command=Programm).grid(row=4,column=5,columnspan=2,sticky=W+E+N+S)
Button(text="Rakendus",relief=RIDGE,font="times_new_roman 15",bg="#b50909",width=30,height=3,command=Rakendus).grid(row=4,column=7,columnspan=2,sticky=W+E+N+S)
Button(text="Eesti",relief=RIDGE,font="times_new_roman 15",bg="#a0b0ac",width=30,height=3,command=Eesti).grid(row=4,column=9,columnspan=2,sticky=W+E+N+S)


Button(text="Rakendus",relief=RIDGE,font="times_new_roman 15",bg="#9e0e0e",width=30,height=3,command=Rakendus).grid(row=5,column=2,columnspan=2,sticky=W+E+N+S)
Button(text="Programm",relief=RIDGE,font="times_new_roman 15",bg="#46cfd4",width=80,height=3,command=Programm).grid(row=5,column=4,columnspan=5,sticky=W+E+N+S)
Button(text="Inglish",relief=RIDGE,font="times_new_roman 15",bg="#9df268",width=30,height=3,command=Inglish).grid(row=5,column=9,columnspan=2,sticky=W+E+N+S)





root.mainloop()