#task:1.write a program to add a key value pair to the dictionary?
details = {}

n = int(input())
for i in range(n):
    key = input("enter key:")
    value = input("enter value:")
    details[key] = value
print(details)
o/p:
= RESTART: C:/Users/manas/OneDrive/Desktop/python/python training/day-10(sep-17-21).py
3
enter key:name
enter value:manasa
enter key:age
enter value:21
enter key:branch
enter value:cse
{'name': 'manasa', 'age': '21', 'branch': 'cse'}

#task:2.write a program to concatenate two dictionaries into one?
d1 = {"name":"manasa","age":21}
d2 = {"branch":"cse"}
d3 = d1.copy()
d3.update(d2)
print(d3)
o/p:
{'name': 'manasa', 'age': 21, 'branch': 'cse'}

#task:3.write a program to check if a given key exists in a dictionary or not?
d1 = {"name":"manasa","age":21,"branch":"cse"}
n = input("enter a key:")
if n in d1.keys():
    print("key exists")
else:
    print("key not exists")
o/p:
enter a key:phno
key not exists

#task:4.write a program to generate a dictionary that contains numbers (between 1 and n)in the form(x,x*x)?
sqrs={}
n = int(input("enter a value:"))
for i in range(1,n+1):
    sqrs[i] = pow(i,2)
print(sqrs)
o/p:
enter a value:5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#task:5.write a program to sum all the items in a dictionary?
d1 = {"x": 25,"y": 50 ,"z" :100}
sm = 0
for i in d1:
    sm += d1[i]
print(sm)
o/p:
175
#task:6.write a program to multiply all the items in a dictionary?
d1 = {"x": 25,"y": 50 ,"z" :100}
sm = 1
for i in d1:
    sm *= d1[i]
print(sm)
o/p:
125000
#task:7.write a program to remove the given key from a dictionary?
d1 ={"X": 25,"y": 50,"z" :100}
n= input("enter a key to delete:")
d1.pop(n)
print(d1)
o/p:
enter a key to delete:y
{'X': 25, 'z': 100}

#task:8.python program to map tow lists into a dictionary?
d1 =["name","age","hobbies"]
d2 =["luky",21,"playing"]
print(dict(zip(d1,d2)))
o/p:
{'name': 'luky', 'age': 21, 'hobbies': 'playing'}

#task:9.python program to count the frequency of words appearing in astring using a dictionary?
words = input().split()
wordscount1 ={}
for word in words:
    wordscount1[word] = words.count(word)
print(wordscount1)

wordscount2 = {}
uniqwords = list(set(words))
print(len(uniqwords))
for word in uniqwords:
    wordscount2[word] = words.count(word)
print(wordscount2)
o/p:
i am abdul and i am from kadapa and i am working in css
{'i': 3, 'am': 3, 'abdul': 1, 'and': 2, 'from': 1, 'kadapa': 1, 'working': 1, 'in': 1, 'css': 1}
9
{'and': 2, 'in': 1, 'i': 3, 'am': 3, 'working': 1, 'kadapa': 1, 'css': 1, 'from': 1, 'abdul': 1}

#task:10.python program to create a dictionary with key as first character and value as words starting with that character?
x = "i am abdul and i am from kadapa and i am working in css"
y = x.split()
d1 = {}
for a in y:
    if(a[0] not in d1.keys()):
        d1[a[0]] = []
        d1[a[0]].append(a)
    else:
        if(a not in d1[a[0]]):
            d1[a[0]].append(a)
print(d1)
o/p:
{'i': ['i', 'in'], 'a': ['am', 'and'], 'm': ['manasa'], 'f': ['from'], 'k': ['kadapa'], 'w': ['working'], 'c': ['css']}

