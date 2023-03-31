import xml.etree.ElementTree as ET
from tkinter.filedialog import *
from .Elemento import Elemento
from .Maquinas import Maquinas
from .Compuesto import Compuesto

class Menu:
    maquina:Maquinas
    
    def cargarXml(self, archivo):
        
        root = archivo.getroot()
        
        for maquina in root.findall('./listaMaquinas/Maquina'):
            nombre_maquina = maquina.find('nombre').text
            numero_pines = maquina.find('numeroPines').text
            int(numero_pines)
            numero_elementos = maquina.find('numeroElementos').text
            int(numero_elementos)
            nueva_maquina = Maquinas(nombre_maquina, numero_pines, numero_elementos)
            nueva_maquina.lista_maquinas.agregar_nodo(nueva_maquina)
        
        for i in root.findall('./listaElementos/elemento'):
            numero = i.find('numeroAtomico').text
            int(numero)
            simbolo = i.find('simbolo').text
            nombre = i.find('nombreElemento').text
            nuevo_elemento = Elemento(numero, simbolo, nombre)
            nueva_maquina.lista_elementos.agregar_nodo(nuevo_elemento)
            
        for compuesto in root.findall('./listaCompuestos/compuesto'):
            nombre_compuesto = compuesto.find('nombre').text
            for i in root.findall('./listaCompuestos/compuesto/elementos'):
                elemento = i.find('elemento').text
                nuevo_compuesto = Compuesto(nombre_compuesto, elemento)
            nueva_maquina.lista_compuestos.agregar_nodo(nuevo_compuesto)
            
        self.maquina = nueva_maquina   
        
    def imprimir_elementos(self):
        lista_ordenada = sorted(self.maquina.lista_elementos, key=lambda x: int(x.numero))
        for elemento in lista_ordenada:
            print("-------------------------")
            print(f"Numero: {getattr(elemento, 'numero', 'NA')}")
            print(f"Simbolo: {getattr(elemento, 'simbolo', 'NA')}")
            print(f"Nombre: {getattr(elemento, 'nombre', 'NA')}")
            print("-------------------------")
    
    def imprimir_maquinas(self):
        for maquina in self.maquina.lista_maquinas:
            print("-------------------------")
            print(f"Nombre: {getattr(maquina, 'nombre_maquina', 'NA')}")
            print(f"Pines: {getattr(maquina, 'numero_pines', 'NA')}")
            print(f"Elementos: {getattr(maquina, 'numero_elementos', 'NA')}")
            print("-------------------------")
    
    def agregar_elemento(self):
        numero = int(input("Ingresa el numero atomico del elemento: "))
        simbolo = input("Ingresa el simbolo del elemento: ")
        nombre = input("Ingresa el nombre del elemento: ")
        nuevo_elemento = Elemento(numero, simbolo, nombre)
        self.maquina.lista_elementos.agregar_nodo(nuevo_elemento)
    
    def pedirNumeroEntero(self):    #Metodo para seleccionar una opcion en el menu
        correcto=False
        num=0
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True
            except ValueError:
                print('Error, introduce un numero entero')
        return num
    
    def gestion_elementos(self):
        regresar = False
        while not regresar:
            print("1. Ver lista de elementos quimicos")
            print("2. Agregar nuevo elemento quimico")
            print("3. Regresar al Menu Principal")
            print ("\nElige una opcion")
 
            opcion = self.pedirNumeroEntero()
            
            if opcion == 1:
                print("\nLISTA DE ELEMENTOS")
                self.imprimir_elementos()
            elif opcion == 2:
                self.agregar_elemento()
            elif opcion == 3:
                regresar = True
                continue
    
    def analizar_compuesto(self):
        regresar = False
        while not regresar:
            print("1. Seleccionar un compuesto")
            print("2. Ver listado de máquinas y tiempos necesarios para producir el compuesto")
            print("3. Ver gráficamente el listado de instrucciones con que una máquina puede producir el compuesto")
            print("4. Regresar")
            print ("\nElige una opcion")
 
            opcion = self.pedirNumeroEntero()
            
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                regresar = True
                continue
    
    
    def gestion_compuestos(self):
        regresar = False
        while not regresar:
            print("1. Ver lista de compuestos y formulas")
            print("2. Analizar compuesto")
            print("3. Regresar al Menu Principal")
            print ("\nElige una opcion")
 
            opcion = self.pedirNumeroEntero()
            
            if opcion == 1:
                pass
            elif opcion == 2:
                self.analizar_compuesto()
            elif opcion == 3:
                regresar = True
                continue
        
    
    def menu(self): #Menu con las opciones a elejir
        salir = False
        opcion = 0
        while not salir:
            print("\n-----MENU PRINCIPAL-----")
            print("1. Inicializacion")
            print("2. Cargar archivo xml de entrada")
            print("3. Generar archivo xml de salida")
            print("4. Gestion de elementos quimicos")
            print("5. Gestion de compuestos")
            print("6. Gestion de maquinas")
            print("7. Ayuda")
            print("8. Salir")
            print("------------------------\n")
            
            print ("Elige una opcion")
 
            opcion = self.pedirNumeroEntero()
 
            if opcion == 1:
                #Inicializacion
                pass
            elif opcion == 2:
                #Generar archivo de entrada
                print("Seleccione el archivo a cargar...")
                filename = "C:\\Users\\ACER\\Desktop\\entrada.xml"
                xml = ET.parse(filename)
                self.cargarXml(xml)
                print("\n¡ARCHIVO CARGADO CORRECTAMENTE!")
            elif opcion == 3:
                #Generar archivo de salida
                pass
            elif opcion == 4:
                #Gestion de elementos
                 self.gestion_elementos()
            elif opcion == 5:
                #Gestion de compuestos
                self.gestion_compuestos()
            elif opcion == 6:
                #Gestion de maquinas
                print("\nLISTADO DE MAQUINAS")
                self.imprimir_maquinas()
            elif opcion == 7:
                #Ayuda
                print("\nNombre: Diego Aldair Sajche Avila")
                print("Codigo estudiantil: 201904490")
                print("CUI: 3011869790101")
                print("Repositorio: https://github.com/sajche12/IPC2_Proyecto2_201904490")
            elif opcion == 8:
                #Salir
                salir = True
            else:
                print ("\nIntroduce un numero entre 1 y 8")
        print ("\nFIN DEL PROGRAMA")