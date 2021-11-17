import random

tajnibroj = random.randint(1, 30)

while True:

    pogodi = int(input("Pogodi broj između 1 i 30:"))

    if pogodi == tajnibroj:
        print("Bravo pogodio si traženi broj.")
        break
    else:
        print("Pogriješio si, pokušaj ponovno.")