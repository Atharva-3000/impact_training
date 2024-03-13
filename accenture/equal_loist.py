#given 2 lists check whether they are equal or not, if they are equal return True otherwise False, lists can have repeated elements, and in any order, dont use sort or sorted fucntion, it should even check for repeated elements in the list and return False if they are not equal

def equal_list(l1,l2):
    if len(l1)!=len(l2):
        return False
    d1={}
    d2={}
    for i in l1:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in l2:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    return d1==d2
    
l1=[1,2,3,3,5]
l2=[5,2,3,2,1]
print(equal_list(l1,l2))