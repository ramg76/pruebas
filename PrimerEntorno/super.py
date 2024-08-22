class ClaseBase:
    def __init__(self):
        print("Constructor de ClaseBase")

    def metodo_clase(self):
        print("Metodo de la clase base")


#Clase Derivada

class ClaseDerivada(ClaseBase):
    def __init__(self):
        super().__init__()#llama al constructor de ClaseBase
        print("Constructor ClaseDerivaba")


obj = ClaseDerivada()
obj.metodo_clase()