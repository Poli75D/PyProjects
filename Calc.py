from tkinter import *

font = "Helvetica 13"
bg1 = "light blue"  # main color
bg2 = "light coral"  # add color


class cls_Calc(Frame):
    def __init__(self, master):
        super(cls_Calc, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg=bg1, bd=12,
                                insertwidth=4, width=50,
                                font=font, textvariable=self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        self.button7 = Button(self, bg=bg1, bd=12, text="7", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(7))
        self.button7.grid(row=2, column=0, sticky=W)
        self.button8 = Button(self, bg=bg1, bd=12, text="8", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(8))
        self.button8.grid(row=2, column=1, sticky=W)
        self.button9 = Button(self, bg=bg1, bd=12, text="9", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(9))
        self.button9.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg=bg1, bd=12, text="4", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)
        self.button5 = Button(self, bg=bg1, bd=12, text="5", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)
        self.button6 = Button(self, bg=bg1, bd=12, text="6", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button1 = Button(self, bg=bg1, bd=12, text="1", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(1))
        self.button1.grid(row=4, column=0, sticky=W)
        self.button2 = Button(self, bg=bg1, bd=12, text="2", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(2))
        self.button2.grid(row=4, column=1, sticky=W)
        self.button3 = Button(self, bg=bg1, bd=12, text="3", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(3))
        self.button3.grid(row=4, column=2, sticky=W)

        self.button0 = Button(self, bg=bg1, bd=12, text="0", width=10, pady=25, font=font,
                              command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.buttonAdd = Button(self, bg=bg1, bd=12, text="+", width=10, pady=25, font=font,
                                command=lambda: self.buttonClick("+"))
        self.buttonAdd.grid(row=2, column=3, sticky=W)
        self.buttonSub = Button(self, bg=bg1, bd=12, text="-", width=10, pady=25, font=font,
                                command=lambda: self.buttonClick("-"))
        self.buttonSub.grid(row=3, column=3, sticky=W)
        self.buttonMul = Button(self, bg=bg1, bd=12, text="*", width=10, pady=25, font=font,
                                command=lambda: self.buttonClick("*"))
        self.buttonMul.grid(row=4, column=3, sticky=W)
        self.buttonDiv = Button(self, bg=bg1, bd=12, text="/", width=10, pady=25, font=font,
                                command=lambda: self.buttonClick("/"))
        self.buttonDiv.grid(row=5, column=3, sticky=W)

        self.buttonEq = Button(self, bg=bg2, bd=12, text="=", width=23, pady=25, font=font,
                               command=self.CalculateTask)
        self.buttonEq.grid(row=5, column=1, sticky=W, columnspan=2)
        self.buttonAC = Button(self, bg=bg2, bd=12, text="TEEEEEJ Wyzeruj To", width=50, pady=25, font=font,
                               command=self.ClearDisplay)
        self.buttonAC.grid(row=1, sticky=W, columnspan=4)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as Err:
            self.displayText("ERROR!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")


Calc = Tk()
Calc.title("Calculator")
app = cls_Calc(Calc)
Calc.resizable(width=False, height=False)
Calc.mainloop()
