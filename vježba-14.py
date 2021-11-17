#liste
brojevi=[15,58,63,20,16]
print(brojevi)
print(brojevi[1])
print(brojevi[2:4])
print(brojevi[:3])
print(brojevi[-1])

voce=["jabuka", "banana", "lubenica", "mango", "jagode"]
if "mango" in voce:
    print("mango je na listi!")
voce.append("kruška")
print(voce)
for x in voce:
   print(x)   
   
brojevi.sort()
print(brojevi)
brojevi.sort(reverse=True)
print(brojevi)