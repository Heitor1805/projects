x=int(input("Number: "))
divisores=0
for i in range(1,x+1):
    if x%i==0:
        print("Não primo")
        divisores+=1
        break
        
    else:
        print(" primo")
        break