#python program to count number of lowercase characters in a string eg::ConzuRa Soft SoLuTIONS"
#procedure:
#--->intitialize count value as 0
#--->iterate a loop
#--->check is that char is lower or not if it is lower then increase count by 1
#--->print count
x = "ConzuRa Soft SoluTIONS"
count = 0
for ch in x:
    if(ch.islower() == True):
        count += 1
print(count)
