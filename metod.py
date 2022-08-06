from  tkinter import *

window = Tk()

window.title("Isroil yaratgan")

window.geometry('600x600')
window.configure(background='#333')

my_label=Label(window,width=100,height=10,bg='#b1b1b1',
               text="Turli masalalarni yechish, \n  sun'iy intellekt tizimlari uchun mo'ljallangan dasturlash tili")
my_label.grid(row=10,column=0)

var1=IntVar()
checkbox1=Checkbutton(window, text="python",variable=var1)
checkbox1.grid(row=20,column=0)
var2=IntVar()
checkbox1=Checkbutton(window, text="Java",variable=var2)
checkbox1.grid(row=30,column=0)

var3=IntVar()
checkbox1=Checkbutton(window, text="php",variable=var3)
checkbox1.grid(row=40,column=0)



my_button=Button(window,text='Button',bg='yellow')
my_button.grid(row=50,column=0)
window.mainloop()
