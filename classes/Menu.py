import xml.etree.ElementTree as ET
from tkinter.filedialog import *
from .Elemento import Elemento
from .Maquinas import Maquinas
from .Compuesto import Compuesto
from .ListaSimpleElementos import ListaElementos

class Menu:
    muestra:Maquinas
    lista_elementos:ListaElementos
    
    
    def cargarXml(self, archivo):
        
        root = archivo.getroot()
        
        nombre_maquina = root[1][0][0].text
        no_pines = root[1][0][1].text
        no_elementos = root[1][0][2].text
            
        nueva_maquina = Maquinas(nombre_maquina, no_pines, no_elementos)
        
        for elemento in root.findall('./listaElementos/elemento'):
            numero = elemento.find('numeroAtomico').text
            simbolo = elemento.find('simbolo').text
            nombre = elemento.find('nombreElemento').text
            nuevo_elemento = Elemento(numero, simbolo, nombre)
            self.lista_elementos.agregar_elemento(nuevo_elemento)
            
        self.lista_elementos.imprimir_elementos()
        
        for compuesto in root.findall('./listaCompuestos/compuesto'):
            nombre_compuesto = compuesto.find('nombre').text
            simbolo = compuesto.findall('elementos/elemento')
            nuevo_compuesto = Compuesto(nombre_compuesto, simbolo)
            nueva_maquina.listaCompuestos.insertar_nodo(nuevo_compuesto)
        
        self.muestra = nueva_maquina
    
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
                print("LISTA DE ELEMENTOS")
                
            elif opcion == 2:
                pass
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
                pass
            elif opcion == 2:
                print("Seleccione el archivo a cargar...")
                filename = "C:\\Users\\ACER\\Desktop\\entrada.xml"
                xml = ET.parse(filename)
                self.cargarXml(xml)
                print("\n¡ARCHIVO CARGADO CORRECTAMENTE!")
            
            elif opcion == 3:
                pass
            elif opcion == 4:
                 self.gestion_elementos()
            elif opcion == 5:
                self.gestion_compuestos()
            elif opcion == 6:
                pass
            elif opcion == 7:
                print("\nNombre: Diego Aldair Sajche Avila")
                print("Codigo estudiantil: 201904490")
                print("CUI: 3011869790101")
                print("Repositorio: https://github.com/sajche12/IPC2_Proyecto2_201904490")
            elif opcion == 8:
                salir = True
            else:
                print ("\nIntroduce un numero entre 1 y 8")
        print ("\nFIN DEL PROGRAMA")