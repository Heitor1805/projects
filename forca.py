import random
tentativas=0
cho=random.randint(0,100)
for i in range(0,100):
    num=int(input("Em qual número eu estou pensando?: "))
    if num==cho:
        print("Acertou")
        break
    elif num!=cho:
      print("Tente novamente")
      tentativas+=1
    if tentativas>=3:
       print(f"Você falhou, o número era {cho}")
       break
