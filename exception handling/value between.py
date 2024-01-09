def between(n):
    assert ((n>=3) and (n<=15))  #(a==b)?:b  something like this
    print(n," is in between.")
try:
    between(10)
    between(2)
except(AssertionError):
    print("Number should be between 3 and 15")