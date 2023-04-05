from .ListaSimple import ListaSimple

class Pin:
    
    def __init__(self,) -> None:
        self.mover_adelante = "Mover hacia adelante"
        self.mover_atras = "Moverse hacia atras"
        self.esperar = "Esperar"
        self.lista_pines = ListaSimple()
        self.lista_instrucciones = ListaSimple()
        