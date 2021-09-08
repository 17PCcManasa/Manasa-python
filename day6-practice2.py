#python program to count the numbers of vowels in a string
x = input("enter a string:")
count = 0
y = x.lower()
for ch in y:
    if(ch =='a' or ch =='e' or ch =='i' or ch =='o' or ch =='u'):
        count+=1
print(count)
