#python program to form a new string where the first character and the last character have been exchanged
x = input("enter a string:")
a = x[0]
b = x[1:-1]
c = x[-1]
print(c+b+a)
