import re
import random
 
WoordenLijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]

HetWoord = random.choice(WoordenLijst)
LengteWoord = len(HetWoord)
LetterAantal = "-" * LengteWoord

print("Het woord heeft " + str(LengteWoord) + " letters.")
print(LetterAantal)  
print("Je hebt 5 kansen.")

counter = 0
while True:
  LetterInvoer = (input(": "))
  match = re.search(LetterInvoer, HetWoord)
  if LetterInvoer == HetWoord:
   print('Het woord is ' + '"' + HetWoord + '"' + ", WINST!")
   break
     
  elif match: 
    print("Juist!")
    for i in range(0, LengteWoord):
     if LetterInvoer == HetWoord[i]:
      LetterAantal = LetterAantal[:i] + LetterInvoer +LetterAantal[i+1:]    
    print(LetterAantal)

  else:
   print("Nope.")
   counter = counter + 1
   if counter == 1:
     print("Je hebt nog 4 kansen.")

   elif counter == 2:
    print("Je hebt nog 3 kansen.")

   elif counter == 3:
     print("Je hebt nog 2 kansen.")
        
   elif counter == 4:
      print("Je hebt nog 1 kansen.")
    
   elif counter == 5:
      print("Noob, u is dead.")
      print('Le word wuz ' + HetWoord)
      break
