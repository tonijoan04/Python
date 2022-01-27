"""
Volem saber si una paraula és capicua:
entrada: “capicua”, sortida: no és capicua
entrada: “anna”, sortida: és capicua.
"""

igual, aux = 0, 0
print("Introdueix una paraula qualsevol: ")
paraula = input()
for ind in reversed(range(0, len(paraula))):
  if paraula[ind].lower() == paraula[aux].lower():
    igual += 1
  aux += 1
if len(paraula) == igual:
	print("Capicua")
else:
	print("No Capicua")
