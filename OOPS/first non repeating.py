s=input()
for i in s:
    if (s.count(i)==1):
        print(i)
        break
    else:
        print("Everything is repeating, or the string is empty.")