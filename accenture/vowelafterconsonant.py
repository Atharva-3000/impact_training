#wap to count how many times a vowel comes after a consonant in a string

def vowel_after_consonant(string):
    count=0
    
    for i in range(len(string)-1):
        if string[i] in 'aeiou' and string[i+1] not in 'bcdfghjklmnpqrstvwxyz':
            count+=1
    return count
print(vowel_after_consonant('aaa@'))