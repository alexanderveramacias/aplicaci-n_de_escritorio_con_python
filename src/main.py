from tkinter import *

root=Tk()
root.title("calculator")

display=Entry(root)
display.grid(row=0,columnspan=5,sticky=W+E)
Button(root,text="1").grid(row=1,column=0,sticky=W+E)
Button(root,text="2").grid(row=1,column=1,sticky=W+E)
Button(root,text="3").grid(row=1,column=2,sticky=W+E)
root.mainloop()
