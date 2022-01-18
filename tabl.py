from tkinter import *
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
Button(text="Tugiõpe eesti").grid(row=1,column=2)
Button(text="Logistika").grid(row=1,column=3,columnspan=2)
Button(text="Matematika").grid(row=1,column=5,columnspan=2)
Button(text="Pereriv4ik").grid(row=1,column=7)
Button(text="Russki").grid(row=1,column=8,columnspan=2)


Button(text="Tugiõpe ximija").grid(row=2,column=2)
Button(text="Programa").grid(row=2,column=3,columnspan=3)
Button(text="Pereriv4ik").grid(row=2,column=6)
Button(text="Fisika").grid(row=2,column=7,columnspan=2)


Button(text="Tugiõpe inglisse").grid(row=3,column=2)
Button(text="Iskustsvo").grid(row=3,column=3,columnspan=2)
Button(text="Pereriv4ik:").grid(row=3,column=5)
Button(text="Fizra").grid(row=3,column=6,columnspan=2)


Button(text="logistika").grid(row=4,column=2,columnspan=2)
Button(text="Pereriv4ik").grid(row=4,column=4)
Button(text="Programa").grid(row=4,column=5,columnspan=2)
Button(text="Rakendus").grid(row=4,column=7,columnspan=2)
Button(text="Eesti").grid(row=4,column=9,columnspan=2)
Button(text="Ruhma tund").grid(row=4,column=11)


Button(text="Rakendus").grid(row=5,column=2,columnspan=2)
Button(text="Programeriumine").grid(row=5,column=4,columnspan=5)
Button(text="Inglisse").grid(row=5,column=9,columnspan=2)

root.mainloop()