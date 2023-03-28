from .ListaDoble import *

class Maquinas:
    
    def __init__(self, nombre, no_pines, no_elementos) -> None:
        self.nombre = nombre
        self.no_pines = no_pines
        self.no_elementos = no_elementos
        self.listaElementos = ListaDoblementeEnlazada()
        self.listaCompuestos = ListaDoblementeEnlazada()