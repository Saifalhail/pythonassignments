from abc import ABC, abstractmethod
import math
import re
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext
import csv

# 5)
class Employee():
    def __init__(self, name, job, basic_pay, age):
        self.name = name
        self.job = job
        self.basic_pay = basic_pay
        self.age = age
    def pay(basic):
        hra = basic * 0.10
        da = basic * 0.25
        gross = hra + da + basic
        return gross

emp1 = Employee('Steve', 'Eng', 50, 30)
empGross = Employee.pay(emp1.basic_pay)
empDetails = [emp1.name, emp1.job, empGross, emp1.age]
print (empDetails)

class Employee(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.employeeDetails()

    # Assignment Questions and Answers Here
    def employeeDetails(self):    
        def displayCSV():
            csvFile = csvFileName.get()
            with open('{}'.format(csvFile), newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
                text_box.insert('end', data)

        csvFileName = Entry(root, width=30)
        csvFileName.insert(END, 'employeedetails.csv')
        csvFileName.pack(pady=2)
        ttk.Button(root, text= "Pull CSV & Display",width= 25, command= displayCSV).pack(pady=20)  

        saveResults = []

        def saveInput():
            userInput = entryMultiple.get()
            userInput2 = entryMultiple2.get()
            userInput3 = entryMultiple3.get()
            userInput4 = entryMultiple4.get()
            saveResults.append(userInput)
            saveResults.append(userInput2)
            saveResults.append(userInput3)
            saveResults.append(userInput4)

        def editInput():
            empDetails.append(saveResults)
            text_box.delete("1.0", "end")
            text_box.insert('end', empDetails)

        entryMultiple = Entry(root, width=30)
        entryMultiple.insert(END, 'Name')
        entryMultiple.pack(pady=2)
        entryMultiple2 = Entry(root, width=30)
        entryMultiple2.insert(END, 'Job')
        entryMultiple2.pack(pady=2)
        entryMultiple3 = Entry(root, width=30)
        entryMultiple3.insert(END, 'Basic Pay')
        entryMultiple3.pack(pady=2)
        entryMultiple4 = Entry(root, width=30)
        entryMultiple4.insert(END, 'Age')
        entryMultiple4.pack(pady=2)

        ttk.Button(root, text= "Save Input",width= 20, command=saveInput).pack(pady=2)

        def exportMultiple():
            with open('employeedetails.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerows(saveResults)

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
    example = Employee(root)
    example.pack(side="top", fill="both", expand=False)
    root.mainloop()