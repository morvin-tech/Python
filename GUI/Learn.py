import tkinter as tk
import tkinter as ttk
App=tk.Tk()
App.title(' Morvin Terminal')


#Label
#ttk.Label(App,text='Python').grid(column=20,row=0)

#Button
#def Onclick():
    #But1.configure(text='AI and ML')
    #But1.configure(background='Blue')
    

#But1=ttk.Button(App,text='Future',command=Onclick)
#But1.grid(column=1,row=0)

#Textbox
ttk.Label(App,text='Enter Your name:').grid(column=0,row=0)

name=tk.StringVar()
name1=ttk.Entry(App,width=15,textvariable=name)
name1.grid(column=0,row=1)
    

def Onclick():
   But1.configure(text='Python->'+ name.get())
   But1.configure(background='Blue')

But1=ttk.Button(App,text='Confirm',command=Onclick)
But1.grid(column=2,row=1) 
#But1.configure(state='disabled')#Disabling a button 
name1.focus()

App.mainloop()
