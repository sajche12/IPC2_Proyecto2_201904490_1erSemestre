class Cola:
    def __init__(self):
        self.datos = []

    def estaVacia(self):
        return self.datos == []

    def agregar(self, dato):
        self.datos.append(dato)

    def tamano(self):
        return len(self.datos)