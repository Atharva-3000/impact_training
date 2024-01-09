#wWAP to print cubes of the odd numbers from 30 to 50
d={p:p**3 for p in range(30,51) if (p%2)!=0}
print(d)