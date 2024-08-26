def mi_decorador(func):
    def envoltura():
        print("Algo se hace antes de la funcion 1")
        func()
        print("algo se hace despues de la funcion 2")

    return envoltura

@mi_decorador
def saludar():
    print("¡Hola desde Python")

saludar()