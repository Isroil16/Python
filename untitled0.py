from tkinter import * 
from tkinter import ttk

root=Tk()
root.title("Akaunt yaratish")
root.resizable(False,False)
root.background='#333'
frame1=ttk.Frame(root,padding=(32))
frame1.grid()

label1=ttk.Label(frame1,text='Username',padding=(5,5))
label1.grid(row=0,column=0)

label2=ttk.Label(frame1,text="Password",padding=(5,5))
label2.grid(row=1,column=0,sticky=E)


username=StringVar
username_entry=ttk.Entry(frame1,textvariable=username,width=20,show='')
username_entry.grid(row=0, column=1)
password=StringVar()
password_entry=ttk.Entry(frame1,textvariable=password,width=20,show='*')
password_entry.grid(row=1, column=1)
frame2=ttk.Frame(frame1,padding=(0,5))
frame2.grid(row=2,column=1,sticky=W)


button1=ttk.Button(frame2,text='OK',command=lambda:print("%s,%s"%(username.get().password.get())))
button1.pack(side=LEFT)
button2=ttk.Button(frame2,text='Cancel')
button2.pack(side=LEFT)
root.mainloop()