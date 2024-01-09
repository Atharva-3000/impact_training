def even(n):
    assert n%2==0, "The number should be even"   #(a==b)?:b  something like this
    print(n," is even.")
try:
    even(10)
    even(5)
except(AssertionError):
    print("Number should be even")