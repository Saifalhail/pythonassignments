from abc import ABC, abstractmethod
import math
import re
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext
import csv

# 1) Creating class vehicle using constructors and dictionary return values
class Vehicle():
    def __init__(self, eating_capacity, fuel, wheels):
        self.eating_capacity = eating_capacity
        self.fuel = fuel
        self.wheels = wheels

car1 = Vehicle("55","500/L","4")
dictReturn = car1.__dict__
# print (dictReturn)

# 2) Abstract class method with two abstract methods
# a)
class Object3D(ABC):
    @abstractmethod
    def volume(self):
        pass

class Box(Object3D):
    def __init__(self, l,b,h):
        self.l = l
        self.b = b
        self.h = h
    def volume(self):
        return self.l*self.b*self.h
    def tsa(self):
        return 2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))

# b)
class Cylinder(Object3D):
    def __init__(self, r,h):
        self.r = r 
        self.h = h
    def volume(self):
        return (math.pi * pow(self.r, 2) * self.h)
    def tsa(self):
        return (2 * math.pi * self.r * self.h) + (2 * math.pi * pow(self.r, 2))

# 3)
class Box2(Object3D):
    def __init__(self, l, b, h):
        self.l = l
        self.b = b
        self.h = h
    def volume(self):
        return self.l*self.b*self.h
    def tsa(self):
        return 2 * ((self.l * self.b) + (self.b * self.h) + (self.l * self.h))
    def __repr__(self):
        return f'Box({self.l}, {self.b}, {self.h})'

# 2 a)
Bv = Box(2,3,4)
Btsa = Box(2,3,4)
# print ('Box Volume: ',Bv.volume())
# print ('Box TSA: ', Btsa.tsa())
# 2 b)
Cv = Cylinder(2,3)
Ctsa = Cylinder(3,4)
# print ('Cylinder Volume: ',Cv.volume())
# print ('Cylinder TSA: ', Ctsa.tsa())
# 3)
first = Box2(2,3,4)
second = Box2(2,3,4)
# print (first.volume() + second.volume())
# print (first.tsa() * second.tsa())


# 4) Numbers checker with static methods
class Number:
    def primeNums(m, n):
        prime_list = []
        for i in range(m, n):
            if i == 0 or i == 1:
                continue
            else:
                for j in range(2, int(i/2)+1):
                    if i % j == 0:
                        break
                else:
                    prime_list.append(i)
        print(prime_list)
        return prime_list
    def recur_fibo(n):
        nterms = 10
        for i in range(nterms):
            print(i-1 + i-2)
    def oddEvenNum(m, n):
        for i in range(m, n + 1):
            if i % 2 != 0:
                print("Odd Nums: ", i, end = " ")
        for i in range(m,n+1):
            if(i%2 == 0):
                print("Even Nums: ", i)
    def reverse(m, n):
        lst = list(range(m, n))
        reversedList = [i for i in reversed(lst)]
        print (reversedList)
    def palindrome(n):
        res = str(n) == str(n)[::-1]
        print ("Is the number palindrome ? : " + str(res))
    def checkPrime(n):
        if n > 1:
            for i in range(2, int(n/2)+1):
                if (n % i) == 0:
                    print(n, "is not a prime number")
                    break
            else:
                print(n, "is a prime number")
        else:
            print(n, "is not a prime number")

primeNumbersList = Number.primeNums(m=5, n=20)
fibNums = Number.recur_fibo(n=20)
oddNums = Number.oddEvenNum(m=5, n=20)
reversed = Number.reverse(m=5, n=20)
palindrome = Number.palindrome(n=20)
checkPrime = Number.checkPrime(n=20)

