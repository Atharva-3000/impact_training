d={"Krishna":{"Python":23,"C":18,"C++":20},"Saritha":{"Python":21,"C":17,"C++":22},"Raju":{"Python":20,"C":17,"C++":22}}
for p,q in d.items():
    print(p)
    print("=================")
    for i in q.values():
        print(i)
    print()