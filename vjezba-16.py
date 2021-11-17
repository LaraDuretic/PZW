# Rječnici u Pythonu 

osoba = {
    "ime":"Marko",
    "prezime":"Marković",
    "god":18
}

print(osoba["ime"])     #ako želimo ispisati određeni ključ

print(osoba.get("prezime"))     #2. način ako želimo ispisati određeni ključ

x = osoba.keys()    #ispisuje samo ključeve pošto piše .keys, a da piše .values onda bi ispisalo samo vrijednost

print(x)

osoba["razred"] = "2.C"     #ako želimo dodati novi ključ

print(osoba.get("razred"))

for x in osoba:
    print(x)

for x in osoba:
    print(osoba[x])

for x in osoba.values():
    print(x)

