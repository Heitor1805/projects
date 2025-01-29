import random
random1=random.randint(1,101)
for i in range(1,101):
    n=int(input("Number:"))
    if random1==n:
        print("Correct")
        break
    else:
        print("Try again")   
