#given a string, and an input n, task is to divide the string into n equal parts
def divide_in_equal_p_parts(s, n):
    l = len(s)
    part_size = l//n
    if l%n != 0:
        print("Invalid String")
        return
    else:
        for i in range(0, l, part_size):
            print(s[i:i+part_size])
s = input("Enter the string: ")
n = int(input("Enter the number of parts: "))
divide_in_equal_p_parts(s, n)