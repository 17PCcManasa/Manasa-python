#python program to detects if two strings or anagrams or not
s1 = input("enter string1:")
s2 = input("enter string2:")
if(len(s1) == len(s2)):
   for ch in s1:
       if ch in s2:
           continue
       else:
           print("its not a anagram")
else:
    print("its not a anagram")

#another methods
if sorted(s1) == sorted(s2):
    print("its a anagram")
else:
    print("its not a anagram")
