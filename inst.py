from tkinter import *

root = Tk()
root.title("Замовлення фотографій")
root.geometry("380x250")
root.resizable(width=False, height=False)

btn1 = Button(text="10х15", background="#00FF00", foreground="#000000", padx="15",
              pady="2", font="16", width=6, height=1)
btn1.place(x=20, y=20)

btn2=Button(text="13х20", background="#FFFF00", foreground="#000000", padx="15", pady="2", font="16", width=6, height=1)
btn2.place(x=20, y=70)

btn3=Button(text="20х30", background="#FF0000", foreground="#000000", padx="15", pady="2", font="16", width=6, height=1)
btn3.place(x=20, y=120)

btn4=Button(text="ЦИФРОВІ", background="#00FFFF", foreground="#000000", padx="15", pady="2", font="16",width=6,height=1)
btn4.place(x=20, y=170)

txt1 = Entry(root,width=30)
txt1.grid(column=1, row=0)
txt1.place(x=160, y=20)

txt2 = Entry(root,width=30)
txt2.grid(column=1, row=0)
txt2.place(x=160, y=70)

txt3 = Entry(root,width=30)
txt3.grid(column=1, row=0)
txt3.place(x=160, y=120)

txt4 = Entry(root,width=30)
txt4.grid(column=1, row=0)
txt4.place(x=160, y=170)

#label = Label(text="додаткові питання по т.067-950-11-90", font="12", pady="10")
#label.pack()


root.mainloop()

