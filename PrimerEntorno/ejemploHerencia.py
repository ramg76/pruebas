#----------ClaseBase-----------
class Animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass #su funcion se define en la clase derivadas , en estos se sobreesribe el
    #el metodo de la clase Base



#-----------clase Derivada--------

class Perro(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: Guau"

#------------clase Derivada---------------
class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice Guau"


#-------------Crear instancias de las clases dirivadas-------------

perro = Perro("Mica")
gato = Gato("Simon")

print(perro.hacer_sonido())
print(gato.hacer_sonido())