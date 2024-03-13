#write a program to remove all consecutive duplicates from a given string. For example, if the input string is “aaaaabbbbbb”, the output should be “ab”.

def removeDuplicatesFromString(s):
    result = ''
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1]:
            result += s[i]
    return result
s = "abbcsb"
print(removeDuplicatesFromString(s))