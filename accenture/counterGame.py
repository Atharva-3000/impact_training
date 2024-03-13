# we have 2 users, i.e. the user and the computer, whoever reaches 17 first wins, at a time the user can add either 1 or 2 to the current count
# computer is smart enought to calculate automatically
# user will start
w=[2,5,8,11,14,17]
i=0
co=0
while i<17:
    if co==0:
        u=int(input("Enter the value:"))
        if u>i+2 or u<i+1:
            print(f"you can only enter {i+1} or {i+2}")
            continue
        i=u
        co=1
    else:
        if i in w:
            i=i+1
        else:
            for j in w:
                if i<j:
                    i=j
                    break
        print(f"I choose {i}")
        co=0
if co==0:
    print("computer win")
else:
    print("user win")
