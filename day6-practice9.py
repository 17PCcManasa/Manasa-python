#python program to calculate the number of upper case letters and lower case letters in a string?
x = "ConzuRa Soft SoluTIONS"
count1 = 0
count2 = 0
for i in x:
    if(i.isupper() == True):
        count1 += 1
    if(i.islower() == True):
        count2 += 1
print("uppercase letters are:",count1)
print("lowercase letters are:",count2)
