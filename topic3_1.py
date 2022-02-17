from abc import ABC, abstractmethod

# 1) Creating class vehicle using constructors and dictionary return values
class Vehicle():
    def __init__(self, eating_capacity, fuel, wheels):
        self.eating_capacity = eating_capacity
        self.fuel = fuel
        self.wheels = wheels

car1 = Vehicle("55","500/L","4")
dictReturn = car1.__dict__

#2) 
class Object3D(ABC):
    @abstractmethod
    def sides(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
 
class Volume(Object3D):
    def noofsides(self):
        print("I have 3 sides")
 
class TSA(Object3D):
    def noofsides(self):
        print("I have 5 sides")
 
# Driver code
R = Volume()
R.noofsides()
# K = TSA()
# K.noofsides()


# if __name__ == "__main__":
#     #1) 
#     # print (dictReturn)
#     #2)
#     pass
