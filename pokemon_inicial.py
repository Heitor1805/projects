import random
b=input("Qual seu pokemon?: ").lower()
a=["charmander","squirtle","bulbassauro"]
choice=random.choice(a)
if b=="charmander" and choice=="squirtle":
 print("Player lose")
elif b=="charmander" and choice=="bulbassauro":
 print("Player won")
elif b=="squirtle" and choice=="charmander":
 print("Player won")
elif b=="squirtle" and choice=="bulbassauro":
 print("Player lose")
elif b=="bulbassauro" and choice=="charmander":
 print("Player lose")
elif b=="bulbassauro" and choice=="squirtle":
 print("Player won")
else:
 print("Draw")

