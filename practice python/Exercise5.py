a=[1,1,2,3,4,5,6]
b=[1,2,3,4,5,6,7,8]
c=[]
for i in a:
    for y in b:
        if i==y and i not in c:
            
            c.append(i)
            print("",i)
