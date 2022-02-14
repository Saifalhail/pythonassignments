from tkinter import *
from tkinter import ttk, scrolledtext


root = Tk()
root.title("Topic 1")
root.geometry('650x850')

# 1)
button1 = Button(root, text = "Hello" , fg = "blue", height=1, width=10).pack(pady=2)

# 2)
button2 = Button(root, text="Exit", command=root.destroy, height=1, width=10).pack(pady=2)

# 3)
comboBox = ttk.Combobox(root, values=["Option1", "Option2", "Option3"], height=5, width=20).pack(pady=5)

# 4)
CheckVar = IntVar()
checkButton = Checkbutton(root, text = "checkButton", variable = CheckVar, onvalue = 1, offvalue = 0, height=5, width = 20).pack()

# 5)
currentValue = StringVar()
spinBox = ttk.Spinbox(root, from_=0, to=5, textvariable=currentValue, wrap=True).pack()

# 6)
textBox = Text(root, height = 2, width = 52)
textBox.pack(pady=5)

def removeText():
    textBox.delete("1.0", "end")

removeButton = Button(root, height = 1, width = 10, text ="Remove Text", command = removeText).pack()


# 7)
def displayText():
   global userEntry1, userEntry2, userEntry3
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

# 8)
radioButtonWidget1 = Radiobutton(root, text="Radio Button Widget", value=0).pack(pady=2)
radioButtonWidget2 = Radiobutton(root, text="Another One", value=1).pack(pady=2)


# 9)
textArea = scrolledtext.ScrolledText(root, width = 10, height = 2, font = ("Times New Roman", 20)).pack(pady=5)

# 10)
progressBar = ttk.Progressbar(root, orient='horizontal', mode='indeterminate', length=280)
progressBar.pack(pady=5)
startButton = ttk.Button(root, text='Start', command=progressBar.start)
startButton.pack(pady=5)
stopButton = ttk.Button(root, text='Stop', command=progressBar.stop)
stopButton.pack(pady=2)

# 11)



root.mainloop()
