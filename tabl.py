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
label.place(x=1000, y=700)
def ponedel():
     label.configure(text="* Tugiõpe \n * Logistika \n * Keel ja kirjandus",font="Arial 20")
def vtornik():
     label.configure(text="* Tugiõpe\n * Programmeerimine\n * füüsika",font="Arial 20")
def sreda():
     label.configure(text="* Tugiõpe \nKunst \n * Kehaline kasvatus",font="Arial 20")
def tetverg():
     label.configure(text="* Logistika\n * rakendus \n* Eesti keel",font="Arial 20")
def patnisa():
    label.configure(text="* rakendus\n * Programmeerimine\n * Inglise keel",font="Arial 20")
def vremja1():
    label.configure(text="8-15")
def 
Label(text="raspisanie Urokov").grid(row=0,column=1,sticky=W+E+N+S)
Button(text="Понедельник:",command=ponedel).grid(row=1,column=1,sticky=W+E+N+S)
Button(text="Вторник:",command=vtornik).grid(row=2,column=1,sticky=W+E+N+S)
Button(text="Среда:",command=sreda).grid(row=3,column=1,sticky=W+E+N+S)
Button(text="Четверг:",command=tetverg).grid(row=4,column=1,sticky=W+E+N+S)
Button(text="Пятница:",command=patnisa).grid(row=5,column=1,sticky=W+E+N+S)
Button(text="0",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=1)
Button(text="1",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=2)
Button(text="2",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=3)
Button(text="3",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=4)
Button(text="4",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=5)
Button(text="5",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=6)
Button(text="6",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=7)
Button(text="7",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=8)
Button(text="8",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=9)
Button(text="9",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=10)
Button(text="10",relief=RIDGE,font="Times_New_Roman 15").grid(row=0,column=11)

#дни недели(понедельник-пятница)
Button(text="Logistik",relief=RIDGE,font="Times_New_Roman 15 ",bg="#61b356",width=30,height=3,command=Logistik).grid(sticky=W+E+N+S,row=1,column=3,columnspan=2)
Button(text="Matem",relief=RIDGE,font="Times_New_Roman 15",bg="#d446c1",width=30,height=3,command=Matem).grid(sticky=W+E+N+S,row=1,column=5,columnspan=2)
Button(text="Pereriv4ik",font="Times_New_Roman 15",bg="thistle",width=15,height=3).grid(sticky=W+E+N+S,row=1,column=7,)
Button(text="Russky",relief=RIDGE,font="Times_New_Roman 15",bg="#a33939",width=30,height=3,command=Russky).grid(sticky=W+E+N+S,row=1,column=8,columnspan=2)

Button(text="Programm",relief=RIDGE,font="Times_New_Roman 15",bg="#46cfd4",width=45,height=3,command=Programm).grid(sticky=W+E+N+S,row=2,column=3,columnspan=3)
Button(text="Pereriv4ik",font="Times_New_Roman 15",bg="thistle",width=15,height=3).grid(sticky=W+E+N+S,row=2,column=6)
Button(text="Fizika",relief=RIDGE,font="Times_New_Roman 15",bg="#f24444",width=30,height=3,command=Fizika).grid(sticky=W+E+N+S,row=2,column=7,columnspan=2)


Button(text="Iskustvo",relief=RIDGE,font="Times_New_Roman 15",bg="#8427a1",width=30,height=3,command=Iskustvo).grid(sticky=W+E+N+S,row=3,column=3,columnspan=2)
Button(text="Pereriv4ik",font="Times_New_Roman 15",bg="thistle",width=15,height=3).grid(sticky=W+E+N+S,row=3,column=5)
Button(text="Fizra",relief=RIDGE,font="Times_New_Roman 15",bg="#dfed18",width=30,height=3,command=Fizra).grid(sticky=W+E+N+S,row=3,column=6,columnspan=2)

Button(text="Logistik",relief=RIDGE,font="Times_New_Roman 15",bg="#61b356",width=30,height=3,command=Logistik).grid(sticky=W+E+N+S,row=4,column=2,columnspan=2)
Button(text="Pereriv4ik",font="Times_New_Roman 15",bg="thistle",width=15,height=3).grid(sticky=W+E+N+S,row=4,column=4)
Button(text="Programm",relief=RIDGE,font="Times_New_Roman 15",bg="#46cfd4",width=30,height=3,command=Programm).grid(sticky=W+E+N+S,row=4,column=5,columnspan=2)
Button(text="Rakendus",relief=RIDGE,font="Times_New_Roman 15",bg="#b50909",width=30,height=3,command=Rakendus).grid(sticky=W+E+N+S,row=4,column=7,columnspan=2)
Button(text="Eesti",relief=RIDGE,font="Times_New_Roman 15",bg="#a0b0ac",width=30,height=3,command=Eesti).grid(sticky=W+E+N+S,row=4,column=9,columnspan=2)


Button(text="Rakendus",relief=RIDGE,font="Times_New_Roman 15",bg="#9e0e0e",width=30,height=3,command=Rakendus).grid(sticky=W+E+N+S,row=5,column=2,columnspan=2)
Button(text="Programm",relief=RIDGE,font="Times_New_Roman 15",bg="#46cfd4",width=80,height=3,command=Programm).grid(sticky=W+E+N+S,row=5,column=4,columnspan=5)
Button(text="Inglish",relief=RIDGE,font="Times_New_Roman 15",bg="#9df268",width=30,height=3,command=Inglish).grid(sticky=W+E+N+S,row=5,column=9,columnspan=2)





root.mainloop()