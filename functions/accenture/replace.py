first = input("Enter big string: ")
sub = input("Enter substring: ")
replace = input("Enter replace value: ")
if sub in first:
    first = first.replace(sub, replace)
print(first)