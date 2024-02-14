import re
import re
# c=0
# FINDITER EXAMPLE
# p=re.finditer("ab","ababababab")
# for s in p:
#     c+=1
#     print(s.start(),"...",s.end(),"...",s.group())
# print("The number of occurences:",c)

# MATCH EXAMPLE
# p=re.match("in","india")
# if(p!=None):
#     print("Match is available at the beginning of the string")
#     print(p.start(),"...",p.end(),"...",p.group())
# else:
#     print("Match is not available at the beginning of the string")


#MATCHALL EXAMPLE
# p=re.fullmatch("india","india-rohit")
# if(p!=None):
#     print("The whole string is matched")
# else:
#     print("The whole string is NOT matched")

# SEARCH EXAMPLE
# p=re.search("india","rohit india is a great country")
# if(p!=None):
#     print("Match is available, with first occurence of the pattern in the string at: ")
#     print(p.start(),"...",p.end(),"...",p.group())
# else:
#     print("Match is not available at the beginning of the string")

# #FINDALL EXAMPLE
# p=re.findall("[1-9]","abab2E243")
# print(p)

#SUB EXAMPLE
# p=re.sub("a","#","abab2E243")
# print(p)

#SUBM EXAMPLE
# p=re.subn("a","#","abab2E243")
# print(p)

#^ EXAMPLE
# p=re.search("^LEARN","LEARN TO WRITE abab2E243")
# if(p!=None):
#     print("The given string starts with LEARN")
#     print(p.start(),"...",p.end(),"...",p.group())
# else:
#     print("Match is not available at the beginning of the string")

# $ EXAMPLE
# p=re.search("243$","TO WRITE LEARN abab2E243")
# if(p!=None):
#     print("The given string ends with LEARN")
# else:
#     print("Match is not available at the end of the string")

# l=re.finditer("[\D]","absdf123bsd")
# for p in l:
#     print(p.start(),"...",p.end(),"...",p.group())

#wap to check given mobile number is valid or not
# p = input("Enter mobile number: ")
# if re.fullmatch("[6-9]\d{9}", p):
#     print("Valid")
# else:
#     print("Invalid")
p = input("Enter Vehicle number: ")
if re.fullmatch("[A-Z]{2}\d{2}[A-Z]{2}\d{4}", p):
    print("Valid")
else:
    print("Invalid")