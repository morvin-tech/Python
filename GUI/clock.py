import time
import tkinter as tk
import tkinter as ttk


    

def click():
    But.configure(text=time.strftime("%H:%M:%S"))
    But.configure(background=("White"),foreground=("Black"))
    But.configure(font=("arial",25,"italic","bold"))


clock=tk.Tk()
clock.title("Current time")
But=ttk.Button(clock,text="Time",command=click)
But.grid(column=2,row=1)
clock.mainloop()
   