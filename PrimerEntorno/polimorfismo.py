#permite que objetos de diferentes clases respondan a la misma interfaz o metodos
#de diferentes

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre


    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return (f"{self.nombre} dice Guau¡")


class Gato(Animal):
    def hablar(self):
        return(f"{self.nombre} dice Miau¡")

def hacer_sonido_Animal(animal):
    print(animal.hablar())


perro = Perro("Mica")
gato = Gato("Chuco")

hacer_sonido_Animal(perro)
hacer_sonido_Animal(gato)