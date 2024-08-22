class ClaseBase:
    def __init__(self):
        print("Constructor de ClaseBase")
    def metodo_clase(self):
        print("Metodo de la clase Base")



class ClaseDerivada(ClaseBase):
        def __init__(self):
            print("Constructor de ClaseDerivada")


obj = ClaseDerivada()
obj.metodo_clase()