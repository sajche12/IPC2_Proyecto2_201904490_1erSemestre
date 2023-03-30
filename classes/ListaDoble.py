class Nodo: #CLASE NODO
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:   #CLASE LISTA DOBLE ENLAZADA
    def __init__(self): #METODO DE LA CABEZA DE LA LISTA
        self.cabeza = None

    def agregar_nodo(self, dato):   #METODO PARA AGREGAR NODOS A LA LISTA
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
