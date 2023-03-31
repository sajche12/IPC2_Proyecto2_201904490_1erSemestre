class Nodo: 
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:   
    def __init__(self): 
        self.cabeza = None

    def agregar_nodo(self, dato):   
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
