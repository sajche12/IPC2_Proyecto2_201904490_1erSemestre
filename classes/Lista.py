class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        
class ListaDoblementeEnlazada:
    def __init__(self):
        self.nodo_inicial = None
        
    def insertar_en_listaVacia(self, dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Nodo(dato)
            self.nodo_inicial = nuevo_nodo
        else:
            print("La lista esta vacia")
            
    def insertar_nodo(self, dato):
        if self.nodo_inicial is None:
            nuevo_nodo = Nodo(dato)
            self.nodo_inicial = nuevo_nodo
            return
        
        auxiliar = self.nodo_inicial
        
        while auxiliar.siguiente is not None:
            auxiliar = auxiliar.siguiente
            
        nuevo_nodo = Nodo(dato)
        auxiliar.siguiente = nuevo_nodo
        nuevo_nodo.anterior = auxiliar
        
    def ver_lista(self):
        if self.nodo_inicial is None:
            print("La lista no tiene elementos")
            return
        else:
            auxiliar = self.nodo_inicial
            while auxiliar is not None:
                print(auxiliar.dato , " ")
                auxiliar = auxiliar.siguiente