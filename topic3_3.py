from abc import ABC, abstractmethod
import math
import pickle


# 6) Grading System
class Student(ABC):
    @abstractmethod
    def total(self):
        pass

class Grade(Student):
    def __init__(self, name, subA, subB, subC):
        self.name = name
        self.subA = subA
        self.subB = subB
        self.subC = subC
    def total(self):
        return self.subA + self.subB + self.subC
    def result(self):
        if (self.total() >= 120) and (self.subA > 35) and (self.subB > 35) and (self.subC > 35):
            print ('Pass')
        else:
            print ('Failed')
    def grade(self):
        if (self.total() >= 120) and (self.subA > 35) and (self.subB > 35) and (self.subC > 35):
            if self.total() >= 240:
                print ("Outstanding!")
            elif self.total() >= 180 < 240:
                print ("Excellant !")
            elif self.total() >= 150 < 180:
                print ("Good")
            else:
                print ("Average")
        else:
            print ("No grade to give for Failed")
            
grading = Grade('Steve', 15, 55, 80)
print ('Total: ',grading.total())
grading.result()
grading.grade()

#Store details in Dict
storeDetails = {"name": grading.name, "total": grading.total(), "result":grading.result(), "grade":grading.grade()}
# print (storeDetails)

#Store details in pickles
with open('studentGrades.pickle', 'wb') as handle:
    pickle.dump(storeDetails, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('studentGrades.pickle', 'rb') as handle:
    studentGrades = pickle.load(handle)

print (studentGrades)

def changeMarks(score, required):
    studentGrades["total"] = required
    return studentGrades

# Change the student Grade
changeMarks(studentGrades["total"], 50)
print (studentGrades)