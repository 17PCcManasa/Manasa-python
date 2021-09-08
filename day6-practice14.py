#python program to print sum of digits in given string. eg:input:abdul123 output:6
x = input("enter:")
sum = 0
for ch in x:
    if ch.isdigit():
        sum += int(ch)
print(sum)
