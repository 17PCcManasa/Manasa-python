#find out nums which are divisible with 3 and 9 in a given range
n = int(input("enter number:"))
for i in range(0,n):
    if((i%3 ==0) and (i%9 == 0)):
        print(i)



#implementing a logic to find a given year is leap
n = int(input("enter a number:"))
if(n % 4 ==0):
    if(n % 100 != 0) or (n % 400 == 0):
        print(n," is a leap year")
    else:
        print(n," is not a leap year")
else:
    print(n," is not a leap year")



#print nums in reverse order like....10 9 8 7 6 5 4 3 2 1 by using for loop.
for i in reversed(range(1,10)):
    print(i,end=' ')

    for i in range(10, -1, -1):
        print(i,end=' ')

#while
#--->1 = 0
#while(cond)
#stmts
#inc/dec

#eg:
    i = 0
    while(i<=10):
        print(i)
        i += 1


#jump statements:
    break
    #it will terminate loop perminantly
    #eg:
for i in range(1,100):
            if i == 51:
                break
            print(i,end=' ')
#continue
  #it will terminate loop for instance time only
   #eg:
for i in range(1,101):
        
        if i % 5 == 0:
            continue
        print(i,end=' ')
pass
        
