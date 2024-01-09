#factorial from 5 to 10 in 3 lines
from math import factorial
factorials = lambda x: factorial(x)
result = [factorials(x) for x in range(5, 12)]
print(result)