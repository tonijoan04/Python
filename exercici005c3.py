"""
Este código que comprueba si x es un valor positivo.
Hay dos cosas mal en él. Una impide que se ejecute, la otra es más sutil.
Asegúrate de que la sentencia if funciona independientemente del valor que tome x.
Identifícalas.
"""

x = int(input("Digues un numero: "))
if x >= 0:
    print("x es positivo.")
else:
    print("x no es positivo.")