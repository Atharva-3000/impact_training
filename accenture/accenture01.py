s = input()
inputString = ""
for i in s.split(" "):
    inputString = inputString+i[::-1]+" "
print(inputString)
