import random

l = []
while len(l) < 10:
    numero = random.randint(1,100)
    if numero not in l:
        l.append(numero)
    	print(numero)
