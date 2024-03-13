#given 2 lists, one is of strings, other of integers, sort list1 according to the order of list2 and return the sorted list1
#example
#l1=['x','xy','xz','1','4', '2', 'v']
#l2=[0,0,1,1,2,3,2]
#output=['x', 'xy', '1', 'xz', '4', 'v', '2']

list1=list(map(str, input().split()))
list2=list(map(str, input().split()))

pair_list=zip(list2, list1)
sorted_list=sorted(pair_list)
sorted_list1=[i[1] for i in sorted_list]
sorted_list2=[i[0] for i in sorted_list]

print(sorted_list1)
print(sorted_list2)