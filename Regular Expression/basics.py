import re
c=0
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
p=re.fullmatch("india","india")
if(p!=None):
    print("The whole string is matched")
else:
    print("The whole string is not matched")