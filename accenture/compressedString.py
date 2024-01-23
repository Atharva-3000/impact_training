#wap to read a string from the user, check whether it is a compressed string or not. If it is a compressed string, then print the compressed string else print "Not a compressed string"
#EXAMPLE:aaabbbbccdefff ,a3b4c2d1e1f3
#OUTPUT: compressed string
s=input("Enter a string:")
count=1
compressedString=""
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        compressedString=compressedString+s[i]+str(count)
        count=1
compressedString=compressedString+s[i]+str(count)
print(compressedString)
if(len(compressedString)<len(s)):
    print("Compressed string")
else:
    print("Not a compressed string")