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
        # 11) Find Volume and Total Surface Area of Rectangular Prism
        def displayTextVolume():
            Volume = (int(volumeInput1.get()) * int(volumeInput2.get()) * int(volumeInput3.get()))
            SurfaceArea = 2 * ( int(volumeInput1.get())   *int(volumeInput2.get()) + int(volumeInput2.get())
                * int(volumeInput3.get()) + int(volumeInput3.get()) * int(volumeInput1.get()))
            labelVolumeEntry.configure(text=Volume)
            labelSurfaceAreaEntry.configure(text=SurfaceArea)

        labelVolumeEntry=Label(root, text="Volume: ", font=("Courier 22 bold"))
        labelVolumeEntry.pack(pady=2)
        labelSurfaceAreaEntry = Label(root, text="TSA: ", font=("Courier 22 bold"))
        labelSurfaceAreaEntry.pack(pady=2)

        volumeInput1 = Entry(root, width=20)
        volumeInput1.insert(END, 'Enter Length')
        volumeInput1.pack(pady=5)
        volumeInput2 = Entry(root, width=20)
        volumeInput2.insert(END, 'Enter Width')
        volumeInput2.pack(pady=5)
        volumeInput3 = Entry(root, width=20)
        volumeInput3.insert(END, 'Enter Height')
        volumeInput3.pack(pady=5)
        volumeButton = Button(root, height = 1, width = 25, text ="Calculate Volume and TSA", command = displayTextVolume).pack(pady=15)

        # 12) Accept Student Details and export as CSV with delimeter comma
        def export():
            entryList = []
            entryList.append(studentUserEntry1.get())
            entryList.append(studentUserEntry2.get())
            entryList.append(studentUserEntry3.get())
            entryList.append(studentUserEntry4.get())

            with open('exportedStudentInfo.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerows(entryList)

        studentUserEntry1 = Entry(root, width=10)
        studentUserEntry1.insert(END, 'Name')
        studentUserEntry1.pack(pady=2)
        studentUserEntry2 = Entry(root, width=10)
        studentUserEntry2.insert(END, 'Course')
        studentUserEntry2.pack(pady=2)
        studentUserEntry3 = Entry(root, width=10)
        studentUserEntry3.insert(END, 'Institute')
        studentUserEntry3.pack(pady=2)
        studentUserEntry4 = Entry(root, width=10)
        studentUserEntry4.insert(END, 'Fees')
        studentUserEntry4.pack(pady=2)
        ttk.Button(root, text= "Export to CSV",width= 20, command=export).pack(pady=15)
        
        # 13)  Accept Multiple Records and Save them
        def exportMultiple():
            with open('exportedMultiple.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerows(saveResults)

        def clear_text():
            entryMultiple.delete(0, 'end')

        saveResults = []

        def saveInput():
            userInput = entryMultiple.get()
            saveResults.append(userInput)
            clear_text()

        entryMultiple = Entry(root, width=30)
        entryMultiple.insert(END, 'Accepting Multiple Entries Here')
        entryMultiple.pack(pady=2)
        ttk.Button(root, text= "Save Input",width= 20, command=saveInput).pack(pady=2)
        ttk.Button(root, text= "Export Inputs",width= 20, command=exportMultiple).pack(pady=5)

        # 14) Access CSV Data and Show results
        def displayCSV():
            csvFile = csvFileName.get()
            with open('{}'.format(csvFile), newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            pulledData.configure(text=data)

        pulledData=Label(root, text="")
        pulledData.pack(pady=2)

        csvFileName = Entry(root, width=30)
        csvFileName.insert(END, 'exportedStudentInfo.csv')
        csvFileName.pack(pady=2)
        ttk.Button(root, text= "Pull CSV & Display",width= 25, command= displayCSV).pack(pady=20)    



    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    example = Assignment(root)
    example.pack(side="top", fill="both", expand=False)
    root.mainloop()