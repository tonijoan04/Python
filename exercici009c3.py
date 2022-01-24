"""
Observa el siguiente código. Adivina lo que crees que producirá y escríbelo.
Luego, ejecútalo y compara el resultado con tu suposición.
Señala claramente tu suposición y la respuesta correcta.
Aunque no tengas que explicarlo, asegúrate de entender el por qué el ordenador ha imprimido eso.
Que no te vaya a pillar desprevenido esto en el futuro.
"""

x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print ("Fizz")
if z:
    print ("Buzz")