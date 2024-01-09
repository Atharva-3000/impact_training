def cal():
    a = int(input("Enter your Month Number: "))
    if(a>12):
        print("Enter the right number of Month ! Try Again")
        cal()
    dayList=[30,28,31,30,31, 30,31,31,30,31,30,31]
    if(a==2):
        y = int(input("Enter your Year: "))
        if(((y % 400 == 0) or (y % 100 != 0)) and (y % 4 == 0)):
            dayList[1]=29
    print("The number of days for the entered month is:",dayList[a-1])
cal()
