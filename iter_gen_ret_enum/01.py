#wap to generate factorials of a number form 5 to 10 and return the values to main program
# def factorial_generator(start, end):
#     for num in range(start, end + 1):
#         yield calculate_factorial(num)

# def calculate_factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# start_range = int(input("Enter the start: "))
# end_range =  int(input("Enter the start: "))

# for factorial in factorial_generator(start_range, end_range):
#     print(f"Factorial of {start_range}: {factorial}")
#     start_range += 1

def gen1(s,e):
    for p in range(s,e+1):
        f=1
        for q in range(1,p+1):
            f=f*q
        yield f
g1=gen1(5,10)
for p in g1:
    print(p)