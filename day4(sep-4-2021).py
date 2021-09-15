#write function to find given number is even or not?
n = int(input("enter a number:"))
def isEven(x):
    if(x % 2 == 0):
        print(x," is even number")
    else:
        print(x," is odd number")
isEven(n)

#another method

n = int(input("enter a number:"))
def isEven(x):
    if(x % 2 == 0):
        return True
    else:
        return False
print(isEven(n))

#resuability:
n = int(input("enter a number:"))
def isEven(x):
    if(x % 2 == 0):
        return True
    return False
count = 0
for i in range(2,n+1):
    if isEven(i):
        print(i,end=' ')
        count += 1
print("events in between ",n," is:",count)

#task-1 find even numbers in between range along with count and sum
x = int(input("enter a number:"))
y = int(input("enter a number:"))
def isEven(n):
    if(n % 2 == 0):
        return True
    return False
count = 0
sum = 0;
for i in range(x,y+1):
    if isEven(i):
        print(i,end=' ')
        count += 1
        sum = sum + i
print("events in between is:",count)
print("sum of is:",sum)

#task2-find a given number is prime or not?
n = int(input("enter a nunmber:"))
x = 0
if(n > 1):
    for i in range(2,n):
        if(n % i == 0):
            x += 1
    if(x == 0):
        print(n," is a prime number")
    else:
        print(n," is not a prime number")
else:
    print(n," is not a prime number")

    #task3-print primes in a given range ,then print count?
a = int(input("enter a number:"))
def isPrime(x):
    count = 0
    for i in range(2,x):
        for j in range(2,i):
            if(i % j == 0):
                break
            else:
                print(i, end =' ')
                count += 1
    print(end = '\n')
    print("count of numbers:",count)
print("prime numbers are:")
isPrime(a)

#task4-print primes in between range then print count
a = int(input("enter a number:"))
b = int(input("enter a number:"))
def isPrime(x,y):
    count = 0
    for i in range(x+1,y):
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print(i, end = ' ')
            count += 1
        print(end = '\n')
        print("count of numbers:",count)
print("prime numbers are from ",a," to ",b" are:")
isPrime(a,b)

#task5-write a function to print 5 and 10 multiples in a given range
a = int(input("enter a number:"))
b = int(input("enter a number:"))
def multiples(x,y):
    for i in range(x,y):
        if(i % 5 == 0) & (i % 10 == 0):
            print(i,end=' ')
multiples(a,b)
    
    
        

     
    
