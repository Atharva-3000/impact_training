#wap to read string for the user and print vowel count
x=input("Enter your staring: ")
x=x.lower()
d={p:x.count(p) for p in ['a','e','i','o','u']}
# or
# d={p:x.count(p) for p in x if x in "aeiou"}
print(d)