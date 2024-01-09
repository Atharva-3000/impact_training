#vowel and consonant count
n=input("Enter your string: ")
vowel=0
consonant=0
for i in n:
    if(i in ['a','e','i','o','u']):
        vowel=vowel+1
    elif (i==' '):
        continue
    else:
        consonant=consonant+1
print("Vowel count is: ",vowel,"Consonant count is", consonant)