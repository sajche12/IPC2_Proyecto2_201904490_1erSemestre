class Nodo: #CLASE NODO 
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
        
class ListaDoblementeEnlazada:  #CLASE LISTA DOBLEMENTE ENLAZADA
    def __init__(self): 
        self.nodo_inicial = None
            
    def insertar_nodo(self, dato):  #FUNCION PARA INGRESAR EL NODO A LA LISTA
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
        