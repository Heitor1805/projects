a=[1,1,2,3,4,5,6,7,9]
b=[]
c=int(input("Number:"))
def fun(a):
    for i in a:
        if i<c:
            b.append(i)
    print(b)           
fun(set(a))