"""
Escribe un programa que reciba un número del usuario del usuario e imprima su es positivo, nogativo o cero.
Utiliza la cadena if/elif/else apropiado,no vayas a emplear ters if consecutivos
"""


numero = int(input("Escriu un numero: "))
if numero > 0:
    print("Es positiu")
elif numero < 0:
    print ("Es negatiu")
else:
    print ("Es zero")
