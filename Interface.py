from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Frame, Label, Button

okno = Tk()
okno.geometry('430x400')
okno.resizable(width=False, height=False)

tytul = Label(okno, text='PARKOMAT')
tytul.pack()

def funkcjaPrzycisku():
    print('dodano monete')

button001 = Button(okno, height=2, width=15, bg='light grey', text='1gr', command=funkcjaPrzycisku)
button001.place(x=15, y=50)
button002 = Button(okno, height=2, width=15, bg='light grey', text='2gr')
button002.place(x=160, y=50)
button005 = Button(okno, height=2, width=15, bg='light grey', text='5gr')
button005.place(x=300, y=50)

button01 = Button(okno, height=2, width=15, bg='#77caa3', text='10gr')
button01.place(x=15, y=100)
button02 = Button(okno, height=2, width=15, bg='#77caa3', text='20gr')
button02.place(x=160, y=100)
button05 = Button(okno, height=2, width=15, bg='#77caa3', text='50gr')
button05.place(x=300, y=100)

button1 = Button(okno, height=2, width=15, bg='light green', text='1pln')
button1.place(x=15, y=150)
button2 = Button(okno, height=2, width=15, bg='light green', text='2pln')
button2.place(x=160, y=150)
button5 = Button(okno, height=2, width=15, bg='light green', text='5pln')
button5.place(x=300, y=150)

button10 = Button(okno, height=2, width=15, bg='light blue', text='10pln')
button10.place(x=15, y=200)
button20 = Button(okno, height=2, width=15, bg='light blue', text='20pln')
button20.place(x=160, y=200)
button50 = Button(okno, height=2, width=15, bg='light blue', text='50pln')
button50.place(x=300, y=200)

button100 = Button(okno, height=2, width=15, bg='light pink', text='100pln')
button100.place(x=15, y=250)
button200 = Button(okno, height=2, width=15, bg='light pink', text='200pln')
button200.place(x=160, y=250)
button500 = Button(okno, height=2, width=15, bg='light pink', text='500pln')
button500.place(x=300, y=250)

zaplacbutton = Button(okno, height=3, width=40, bg='goldenrod', text='Zatwierdź')
zaplacbutton.place(x=70, y=320)
okno.mainloop()


