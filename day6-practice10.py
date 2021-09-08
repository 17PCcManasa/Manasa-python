#python program to calculate the number of digits and letters in a string
s = input("enter a string:")
dcount = 0
lcount = 0
for ch in s:
    if ch.isdigit():
        dcount += 1
    elif(ch.isalpha()):
        lcount += 1
    else:
        pass
print("digits count is:",dcount)
print("letters count is:",lcount)
