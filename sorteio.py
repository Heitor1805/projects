import random
aleatorio=random.randint(1,11)
for i in range(1,11):
    n=int(input("Número:"))
    if aleatorio==n:
        print("Correto")
        break
    else:
        print("Tente denovo")   