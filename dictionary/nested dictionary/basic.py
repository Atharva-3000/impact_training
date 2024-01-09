d={"krishna":[23,21,24],"raju":[21,20,18],"saritha":[22,20,16]}
for p,q in d.items():
    print(p)
    s=sum(q)
    avg=s/len(q)
    print("avg: %.2f"%avg)