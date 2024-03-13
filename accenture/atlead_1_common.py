# given two lists, check whether they have atleast one common element

def atleast_1_common(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(atleast_1_common(l1, l2))