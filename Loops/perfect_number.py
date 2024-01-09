for p in range(1,101):
    s=0
    for q in range(1,p//2+1):
        if(p%q==0):
            s=s+q
    if(s==p):
        print(p,end=" ")
    
