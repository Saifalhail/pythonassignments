from multiprocessing.connection import wait
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext
import csv 

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
        # 16) 
        
        displayUnit = []

        def displayCSV():
            csvFile = csvFileName.get()
            with open('{}'.format(csvFile), newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
                displayUnit.append(data)
                text_box.insert('end', displayUnit)
   
        csvFileName = Entry(root, width=30)
        csvFileName.insert(END, 'exportedStudentInfo.csv')
        csvFileName.pack(pady=2)
        ttk.Button(root, text= "Pull CSV & Display",width= 25, command= displayCSV).pack(pady=20)  


        def clear_text():
            entryMultiple.delete(0, 'end')

        saveResults = []

        def saveInput():
            userInput = entryMultiple.get()
            saveResults.append(userInput)
            clear_text()

        def editInput():
            displayUnit.append(saveResults)
            text_box.delete("1.0", "end")
            text_box.insert('end', displayUnit)

        entryMultiple = Entry(root, width=30)
        entryMultiple.insert(END, '')
        entryMultiple.pack(pady=2)
        ttk.Button(root, text= "Save Input",width= 20, command=saveInput).pack(pady=2)

        def exportMultiple():
            with open('exportedEnd.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerows(displayUnit)

        def displayText():
            string = saveResults
            labelUserEntry.configure(text=string)

        labelUserEntry=Label(root, text="", font=("Courier 22 bold"))
        labelUserEntry.pack(pady=2)

        ttk.Button(root, text= "Show Input",width= 20, command= displayText).pack(pady=5)
        ttk.Button(root, text= "Add Inputs",width= 20, command=editInput).pack(pady=5)

        text_box = Text(root, height=12, width=40)
        text_box.pack(expand=True)
        ttk.Button(root, text= "Export Inputs",width= 20, command=exportMultiple).pack(pady=5)


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    example = Assignment(root)
    example.pack(side="top", fill="both", expand=False)
    root.mainloop()