# To do aplikacija

lista_zadataka = []

print("Dobrodošli u To do aplikaciju. Za izlaz odaberite x")

while True:

    zadatak = input ("Unesi novi zadatak: ")

    if zadatak.lower() != "x":
        lista_zadataka.append(zadatak)
    else:
        break

print("Lista zadataka")
for x in lista_zadataka:
    print(x)

