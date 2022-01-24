"""
¿Qué está mal en este código?
"""

print("Bienvenidos a la Ultra Trail!")
 
print("A. Banquero")
print("B. Carpintero")
print("C. Granjero")
 
res = input("¿Cuál es tu profesión?")
 
if res == "A":
    dinero = 100
elif res == "B":
    dinero = 70
else:
    dinero = 50
     
print("Genial! empezarás el juego con", dinero, "dólares.")