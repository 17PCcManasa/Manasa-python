#write a program to find the second largest number in a list
x = [2,6,35,44,59,25]
x.sort()
print("enter the 2nd largest value: ",x[-2])

o/p:
Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 = RESTART: C:\Users\manas\OneDrive\Desktop\python\python training\day7-practice.py
>>>enter the 2nd largest value:  44   


#another method:
n = int(input("enter the number of elements:"))
x = []


for i in range(0,n):
    y = int(input())
    x.append(y)
x.sort()
print("enter the 2nd largest value: ",x[-2])

o/p:
enter the number of elements: 3
6
9
4
enter the 2nd largest value:  6
