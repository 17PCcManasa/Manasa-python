#write a program to put even and odd elements in a list into two different lists
n = int(input("enter the number of elements:"))
x = []
y = []
z = []

for i in range(0,n):
    a = int(input())
    x.append(a)
for i in x:
    if(i % 2 == 0):
        y.append(i)
    else:
        z.append(i)
print(x)
print("even elements:" ,y)
print("odd elements:" ,z)

o/p:
 RESTART: C:\Users\manas\OneDrive\Desktop\python\python training\day7-practice1.py
enter the number of elements:4
9
8
4
1
[9, 8, 4, 1]
even elements: [8, 4]
odd elements: [9, 1]

