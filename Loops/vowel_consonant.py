#Write a program to read a charater from a user and check whether it is vowel or consonant
char=input("Enter the character: ")
#vowel=['a','e','i','o','u']
vowel="aeiouAEIOU"
if(char in vowel):
    print("It's a vowel")
else:
    print("Its a consonant")
