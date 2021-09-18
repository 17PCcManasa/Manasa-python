#generate a dict dynamically
#{1:1,2:4,3:9,4:16}
sqrs={}
cubes={}
n = int(input("enter a value1:"))
for i in range(1,n+1):
    sqrs[i]=pow(i,2)
    cubes.update({i:i**3})
print(sqrs)
print(cubes)
o/p:
enter a value1:4
{1: 1, 2: 4, 3: 9, 4: 16}
{1: 1, 2: 8, 3: 27, 4: 64}
