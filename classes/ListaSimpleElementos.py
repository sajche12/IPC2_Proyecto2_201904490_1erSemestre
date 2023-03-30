class Nodo:     #Creando clase del Nodo
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

class ListaElementos:    #Creando clase de la lista enlazada
    def __init__(self):
        self.lista_elementos = []

    def agregar_elementos(self, nuevo_elemento):    #Metodo para agregar Nodos a la lista simple
        self.lista_elementos.append(nuevo_elemento)
        
    def imprimir_elementos(self):
        for elemento in self.lista_elementos:
            print("Número atómico:", elemento.numero)
            print("Símbolo:", elemento.simbolo)
            print("Nombre:", elemento.nombre)

    