import random
x=input("pedra, papel or tesoura?: ").lower()
options=["pedra","papel","tesoura"]
maquina=random.choice(options)
if x==maquina:
    print("Draw")
elif x=="pedra" and maquina=="tesoura":
    print("Você venceu")
elif x=="pedra" and maquina=="papel":
    print("Você perdeu")
elif x=="papel" and maquina=="pedra":
    print("PLayer won")
elif x=="papel" and maquina=="tesoura":
    print("Você perdeu")
elif x=="tesoura" and maquina=="pedra":
    print("Você perdeu")
elif x=="tesoura" and maquina=="papel":
    print("Você venceu")
    





    

