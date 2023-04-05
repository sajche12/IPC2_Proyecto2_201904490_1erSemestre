class Nodo:     
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaSimple:    
    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def agregar_nodo(self, dato):    
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
        self.tamano += 1
    
    def __iter__(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
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