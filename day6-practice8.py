#program to check a string palindrom or not
x = input("enter a string:")
y = x[::-1]
if (x == y):
    print(x,"is a palindrome")
else:
    print(x,"is not a palindrome")
