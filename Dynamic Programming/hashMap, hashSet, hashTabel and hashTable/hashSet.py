hash_Set=set()
print(type(hash_Set))
hash_Set.add(10)
hash_Set.add(30)
hash_Set.add(20)
hash_Set.add(50)
hash_Set.add(50)
hash_Set.add(40)
print(hash_Set)
search_ele=20
if search_ele in hash_Set:
    print("Ele found !")
else:
    print("Not found !")