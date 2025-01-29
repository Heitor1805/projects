x = int(input("Number: "))
divisores = 0  # Contador para rastrear quantos divisores o número tem

for i in range(1, x + 1):
    if x % i == 0:  # Verifica se é divisível por i
        divisores += 1  # Incrementa o contador de divisores

if divisores == 2:  # Se tiver apenas dois divisores (1 e ele mesmo), é primo
    print("Primo")
else:
    print("Não primo")
