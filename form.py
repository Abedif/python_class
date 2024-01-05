#=================Module============================
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#==================GUI=============================
win = Tk()
win.geometry('400x350+440+250')
win.resizable(0,0)
win.title('form')
win.config(bg ='light green')

#================Functions=======================











#==================Widget=======================

#name
name_label = Label(win , text = 'Name : ' , font= 'arial 15' , bg ='light green' , fg='black' )
name_label.place(x=35 , y=30)

name_ent = Entry(win , width=35)
name_ent.place(x=110 , y=35)

#family
family_label = Label(win , text = 'Family : ' , font= 'arial 15' , bg ='light green' , fg='black' )
family_label.place(x=35 , y=70)

family_ent = Entry(win , width=35)
family_ent.place(x=110 , y=75)

#salary
salary_label = Label(win , text = 'Salary : ' , font= 'arial 15' , bg ='light green' , fg='black' )
salary_label.place(x=35, y=110)

salary_ent = Entry(win , width=35)
salary_ent.place(x=110 , y=115)


#button
tax_btn = ttk.Button(win , width=15 , text='Tax')
tax_btn.place(x=110, y=160) 

bime_btn = ttk.Button(win , width=15 , text='Bime')
bime_btn.place(x=220, y=160) 

status_btn = ttk.Button(win , width=15 , text='Status')
status_btn.place(x=110, y=210) 

exit_btn = ttk.Button(win , width=15 , text='Exit')
exit_btn.place(x=220, y=210) 




win.mainloop()