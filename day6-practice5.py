#python program to calculate the number of words and the number of characters present in a string
x = "python programming language"
y = x.split()
count = 0
for i in y:
    count += 1
print("number of words:",count)
count=0
for ch in x:
    count += 1
print("numbers of characters:",count)

#another method:
x = "python@programming@language"
print(x.split('@'))
