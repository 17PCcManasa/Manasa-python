#python program to take in two strings and display the larger string without using built-in functions
x = input("enter string1:")
y = input("enter string2:")
count1 = 0
count2 = 0
for i in x:
    count1 += 1
for j in y:
    count2 += 1
if(count1 > count2):
    print(x," is a larger string")
else:
    print(y," is a larger string")
    
