class Alumno:
    def __init__(self,  nombre ):
        self.nombre = nombre
        self.notas = []


#notas-----------------------------------------------
    def pedir_notas(self):
        for i in range(4):
            notas = float(input(f"Ingrese la nota {i + 1} para {self.nombre}: "))


            self.notas.append(notas)

#mostrar notas--------------------------
    def mostrar_notas(self):
        print(f"notas de {self.nombre}: {self.notas}")

#Promedio------------------------------------------
    def promedio(self):
        return sum(self.notas) / len(self.notas)

#sitauacion---------------------------------------
    def situacion(self):
        promedio =self.promedio()
        if promedio >= 4:
            print ("Estas aprobado")
        else:
            print("te falto , estas reprobado")


"""para que no de error de division 
por zero primero pedir notas"""

Alumno1  = Alumno("Rodrigo")
Alumno1.pedir_notas()
Alumno1.mostrar_notas()

print(f"Promedio :{Alumno1.promedio()}")
Alumno1.situacion()






