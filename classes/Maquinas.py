from .ListaDoble import ListaDobleEnlazada
from .ListaSimple import ListaSimple

class Maquinas:
    
    no_elementos:int
    no_pines:int
    
    def __init__(self, nombre, no_pines, no_elementos) -> None:
        self.nombre = nombre
        self.no_elementos = no_elementos
        self.no_pines = no_pines
        self.lista_compuestos = ListaDobleEnlazada()
        self.lista_maquinas = ListaSimple()
        self.lista_elementos = ListaSimple()
        