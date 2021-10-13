import random

n = random.randint(1,10)

print(n)

a = int(input("unesi broj a:"))

if a == n: 
    print("Bravo")
else:
    print("Netočno, traženi broj je bio {0}".format(n))
