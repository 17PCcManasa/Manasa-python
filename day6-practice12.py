#python program to count the occurences of each word in a given string sentence
x = "hello nice to meet you hello"
z = x.split()
a = []
for i in z:
    if (i not in a):
        a.append(i)
for i in range(0,len(a)):
    print("occurrences of ",a[i],"is:",z.count(a[i]))
