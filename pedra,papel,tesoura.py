import random
x=input("rock, paper or scissor?: ").lower()
options=["rock","paper","scissor"]
maquina=random.choice(options)
if x==maquina:
    print("Draw")
elif x=="rock" and maquina=="scissor":
    print("Player won")
elif x=="rock" and maquina=="paper":
    print("Player lose")
elif x=="paper" and maquina=="rock":
    print("Player won")
elif x=="paper" and maquina=="scissor":
    print("Player lose")
elif x=="scissor" and maquina=="rock":
    print("Player lose")
elif x=="scissor" and maquina=="paper":
    print("Player won")
    





    

