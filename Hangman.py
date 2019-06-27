import random

WoordenLijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

HetWoord = random.choice(WoordenLijst)
LengteWoord = len(HetWoord)
LetterAantal = "." * LengteWoord


print("Het woord heeft " + str(LengteWoord) + " letters.")
print(LetterAantal)
