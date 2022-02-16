import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext


class Assignment(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.assignmentResults()

    # Assignment Questions and Answers Here
    def assignmentResults(self):
        '''
        Assignment
        Results and Answers 
        '''
        # 1) Button
        button1 = Button(root, text = "Hello" , fg = "blue", height=1, width=10).pack(pady=2)

        # 2) Two Buttons
        button2 = Button(root, text="Exit", command=root.destroy, height=1, width=10).pack(pady=2)

        # 3) Combo Box with 3 Options
        comboBox = ttk.Combobox(root, values=["Option1", "Option2", "Option3"], height=5, width=20).pack(pady=5)

        # 4) Check Button Widget
        CheckVar = IntVar()
        checkButton = Checkbutton(root, text = "checkButton", variable = CheckVar, onvalue = 1, offvalue = 0, height=5, width = 20).pack()

        # 5) Spin Box Widget
        currentValue = StringVar()
        spinBox = ttk.Spinbox(root, from_=0, to=5, textvariable=currentValue, wrap=True).pack()

        # 6) Text Widget With Remove Capabilties
        def removeText():
            textBox.delete("1.0", "end")
        textBox = Text(root, height = 2, width = 52)
        textBox.pack(pady=5)
        removeButton = Button(root, height = 1, width = 10, text ="Remove Text", command = removeText)
        removeButton.pack()

        # 7) Three Single line text, accept and display
        def displayText():
            string= userEntry1.get(), userEntry2.get(), userEntry3.get()
            labelUserEntry.configure(text=string)

        labelUserEntry=Label(root, text="", font=("Courier 22 bold"))
        labelUserEntry.pack(pady=2)

        userEntry1 = Entry(root, width=10)
        userEntry1.pack(pady=2)
        userEntry2 = Entry(root, width=10)
        userEntry2.pack(pady=2)
        userEntry3 = Entry(root, width=10)
        userEntry3.pack(pady=2)
        
        ttk.Button(root, text= "Show Input",width= 20, command= displayText).pack(pady=20)

        # 8) Three Radio Button Widgets
        radioButtonWidget1 = Radiobutton(root, text="Radio Button Widget", value=0).pack(pady=2)
        radioButtonWidget2 = Radiobutton(root, text="Second Radio Button", value=1).pack(pady=2)
        radioButtonWidget3 = Radiobutton(root, text="Third Radio Button", value=2).pack(pady=2)

        # 9) Scrolled Text Widget
        textArea = scrolledtext.ScrolledText(root, width = 10, height = 2, font = ("Times New Roman", 20)).pack(pady=5)

        # 10) Progress Bar Widget
        progressBar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
        progressBar.pack(pady=5)
        startButton = ttk.Button(root, text='Start', command=progressBar.start)
        startButton.pack(pady=5)
        stopButton = ttk.Button(root, text='Stop', command=progressBar.stop)
        stopButton.pack(pady=2)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    example = Assignment(root)
    example.pack(side="top", fill="both", expand=False)
    root.mainloop()