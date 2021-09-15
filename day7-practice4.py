#write a program to find all numbers in a range which are perfect squares and sum of all digits in the number is less than 10
x = int(input("enter the range:"))

for i in range(1,x+1):
    print(i, end=' ')
print()
for i in range(1,x+1):
    z = i + i
    if(z < 10):
        y = i * i
        print("square of",i," is:",y)

        
o/p:
= RESTART: C:\Users\manas\OneDrive\Desktop\python\python training\day7-practice5.py
enter the range:10
1 2 3 4 5 6 7 8 9 10 
square of 1  is: 1
square of 2  is: 4
square of 3  is: 9
square of 4  is: 16





x = int(input("enter the range:"))

for i in range(1,x+1):
    print(i,end=' ')
print()
for i in range(1,x+1):
    y = i * i
    a = y
    sm = 0
    while (y > 0):
        z = y % 10
        sm += z
        y = y // 10
    if(sm < 10):
        print("square of ",i," is:",a)
o/p:
enter the range:10
1 2 3 4 5 6 7 8 9 10 
square of  1  is: 1
square of  2  is: 4
square of  3  is: 9
square of  4  is: 16
square of  5  is: 25
square of  6  is: 36
square of  9  is: 81
square of  10  is: 100    

