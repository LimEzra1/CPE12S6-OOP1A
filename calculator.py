from tkinter import *

class MyWindow:
    def __init__(self, window):
        self.lbl = Label(window, text="Simple Calculator")
        self.lbl.place(x=75, y=75)

        self.lbl1 = Label(window, text="Number 1:", fg="blue")
        self.lbl1.place(x=80, y=100)
        self.txt1 = Entry(window, bd=2)
        self.txt1.place(x=150, y=100)

        self.lbl2 = Label(window, text="Number 2:", fg="orange")
        self.lbl2.place(x=80, y=150)
        self.txt2 = Entry(window, bd=5)
        self.txt2.place(x=150, y=150)

        self.btn1 = Button(window, text="Add", command=self.add)
        self.btn1.place(x=80, y=200)

        self.btn2 = Button(window, text="Subtract", command=self.sub)
        self.btn2.place(x=115, y=200)

        self.btn3 = Button(window, text="Multiply", command=self.mul)
        self.btn3.place(x=172, y=200)

        self.btn4 = Button(window, text="Divide", command=self.div)
        self.btn4.place(x=230, y=200)

        self.txt3 = Entry(window)
        self.txt3.place(x=100, y=250)

    def add(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        round(result, 2)
        self.txt3.insert(END, str(result))

window = Tk()
mywin = MyWindow(window)
window.geometry("500x400+10+20")
window.title("Python Project")
window.mainloop()