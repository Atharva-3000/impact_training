#write a program to print square of even numbers from 1 to 20
#key is the number and value is square of the number
d={p:p*p for p in range(1,21) if(p%2)==0}
print(d)