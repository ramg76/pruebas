"""
nueva_lista = [expresion for elemento if n % 2 == 0]
"""

numeros = [1,2,3,4,5]
cuadrados_pares = [n ** 2 for n in  numeros if n % 2 == 0]
print(cuadrados_pares)