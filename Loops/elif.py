#read a character form the user and check whether it is uppercase, lowercase or digit or special character

#take ordinance value
ch=input("Enter your character : ")
if((ch>='A') and (ch<='Z')):
    print("Uppercase")
elif((ch>='a') and (ch<='z')):
    print("Lowercase")
elif((ch>='0') and (ch<='9')):
    print("Digit")
else:
    print("Special Symbol")
