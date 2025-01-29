num=int(input("Number: "))
count=0
i=0
for i in range(1,num):
    if num%i==0:
        count+=1
        print(f"The divisors of {num} are {i}")
print(f"This number has {count} divisors ")