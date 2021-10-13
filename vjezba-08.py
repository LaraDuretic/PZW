a = int(input("Unesi broj a:"))

b = int(input("Unesi broj b:"))

operacija =  input("Odaberi matematičku operaciju:")

if operacija == "+":
    print(a+b)
elif operacija == "-":
    print(a-b)
elif operacija == "*":
    print(a*b)
elif operacija == "/":
    print(a/b)
else:
    print("Nisi odabrao valjanu operaciju")