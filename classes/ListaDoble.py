class Nodo: 
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDobleEnlazada:   
    def __init__(self): 
        self.cabeza = None
        self.tamano = 0

     # Insertar al final de la lista
    def insertar(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
        self.tamano += 1

    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            yield nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
    
    def buscar_por_indice(self, indice):
        actual = self.cabeza
        i = 1
        while actual is not None:
            if i == indice:
                return actual.dato
            actual = actual.siguiente
            i += 1
            