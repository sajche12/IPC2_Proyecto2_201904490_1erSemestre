from classes.ListaSimpleElementos import ListaEnlazada

class Maquinas:
    
    def __init__(self, nombre, no_pines, no_elementos) -> None:
        self.nombre = nombre
        self.no_elementos = no_elementos
        self.no_pines = no_pines
        self.listaElementos = ListaEnlazada()
        self.listaCompuestos = ListaEnlazada()