n = int(input("Enter the size of your input list: "))
print("Start Entering the Values :")
li = list(map(int,input().split(" ")))[:n]
li.sort(reverse=True)
print(*li,sep="")
