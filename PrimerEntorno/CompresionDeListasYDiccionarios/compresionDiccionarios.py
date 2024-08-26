"""
nuevo_diccionario = {clave : valor  for elemento in iterrable if condicon}
"""

personas={"rodrigo" : 48, "Mica" : 7 , "Amigo Imaginario": 48  }

""" Elementos  key:value para cada nombre, edad en iterrable persona 
 .items entrega la informacion como un diccionario
 if edad  >= condicion"""
mayores_de_edad = {nombre: edad for nombre, edad in personas.items() if edad >= 18}
print(mayores_de_edad)

