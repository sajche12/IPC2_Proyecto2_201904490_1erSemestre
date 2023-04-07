import tkinter as tk
import xml.etree.ElementTree as ET
from tkinter import filedialog
from .Elemento import Elemento
from .Maquinas import Maquinas
from .Compuesto import Compuesto
from .ListaSimple import ListaSimple
from .Pin import Pin
from .ListaDoble import ListaDobleEnlazada
import random

class Menu:
    maquina:Maquinas
    elementos:Compuesto
    accion = Pin()
    
    def cargarXml(self, archivo):
        
        root = archivo.getroot()
        
        self.lista_maquinas = ListaSimple()
        for maquina in root.findall('./listaMaquinas/Maquina'):
            nombre_maquina = maquina.find('nombre').text
            numero_pines = maquina.find('numeroPines').text
            int(numero_pines)
            numero_elementos = maquina.find('numeroElementos').text
            int(numero_elementos)
            nueva_maquina = Maquinas(nombre_maquina, numero_pines, numero_elementos)
            self.lista_maquinas.agregar_nodo(nueva_maquina)
        
        for i in root.findall('./listaElementos/elemento'):
            numero = i.find('numeroAtomico').text
            int(numero)
            simbolo = i.find('simbolo').text
            nombre = i.find('nombreElemento').text
            nuevo_elemento = Elemento(numero, simbolo, nombre)
            nueva_maquina.lista_elementos.agregar_nodo(nuevo_elemento)
        
        for compuesto in root.findall('./listaCompuestos/compuesto'):
            nombre_compuesto = compuesto.find('nombre').text
            lista = []
            for elemento in compuesto.findall('elementos/elemento'):
                lista.append(elemento.text)
                tiempo = len(lista)
            nuevo_compuesto = Compuesto(nombre_compuesto, lista, tiempo)
            nueva_maquina.lista_compuestos.insertar(nuevo_compuesto)
            
        self.maquina = nueva_maquina   
    
    def archivo_salida(self):
        
        tree = ET.parse("C:\\Users\\ACER\\Desktop\\Proyecto2\\salida.xml")
        root = tree.getroot()
       
        for compuesto in root.findall('./listaCompuestos/compuesto'):
            maquina = self.lista_maquinas.buscar_por_indice(self.numero_maquina)
            nombre_maquina = maquina.nombre
            compuesto.find('nombre').text = f'{self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto).nombre_compuesto}'
            compuesto.find('maquina').text = f'{nombre_maquina}'
            compuesto.find('tiempoOptimo').text = f'{self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto).tiempo+1}'
        
        for tiempo in root.findall('./listaCompuestos/compuesto/instrucciones/tiempo'):
            tiempo.find('numeroSegundo').text = f'{self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto).tiempo+1}'
        
        for self.accion in root.findall('./listaCompuestos/compuesto/instrucciones/tiempo/self.acciones/self.accionPin'):
            for i in self.accion.lista_instrucciones:
                for j in self.conteo_pines:
                    numero_pin = ET.SubElement(self.accion, 'numeroPin')
                    numero_pin.text = f'{j}'
            
                    self.accion = ET.SubElement(self.accion, 'self.accion')
                    self.accion.text = "Mover adelante"
                
            
            # self.accion.find('numeroPin').text = ""
            # self.accion.find('self.accion').text = ""
        
        tree.write("C:\\Users\\ACER\\Desktop\\Proyecto2\\salida.xml")
        print("\n¡EL ARCHIVO SE CREO CORRECTAMENTE!")   
                
    def imprimir_elementos(self):
        lista_ordenada = sorted(self.maquina.lista_elementos, key=lambda x: int(x.numero))
        for elemento in lista_ordenada:
            print("-------------------------")
            print(f"Numero: {getattr(elemento, 'numero', 'NA')}")
            print(f"Simbolo: {getattr(elemento, 'simbolo', 'NA')}")
            print(f"Nombre: {getattr(elemento, 'nombre', 'NA')}")
            print("-------------------------")
    
    def imprimir_compuesto(self):
        for compuesto in self.maquina.lista_compuestos:
            print("---------------------")
            print(f"Nombre: {getattr(compuesto, 'nombre_compuesto', 'NA')}")
            print(f"Elementos: {getattr(compuesto, 'elemento', 'NA')}")
            print("---------------------")
                
    def imprimir_maquinas(self):
        for maquina in self.lista_maquinas:
            print("-------------------------")
            print(f"Nombre: {getattr(maquina, 'nombre', 'NA')}")
            print(f"Pines: {getattr(maquina, 'no_pines', 'NA')}")
            print(f"Elementos: {getattr(maquina, 'no_elementos', 'NA')}")
            print("-------------------------")
    
    def agregar_elemento(self):
        numero = int(input("\nIngresa el numero atomico del elemento: "))
        simbolo = input("Ingresa el simbolo del elemento: ")
        nombre = input("Ingresa el nombre del elemento: ")
        encontrado = False
        for elemento in self.maquina.lista_elementos:
            if (int(elemento.numero) == numero) or (elemento.simbolo == simbolo) or (elemento.nombre == nombre):
                print("\nEl elemento ya se encuentra en la lista")
                encontrado = True
                break
            
        if not encontrado:
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
            print("\n1. Ver lista de elementos quimicos")
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
        
        print("\nLISTA DE COMPUESTOS")
        i = 1
        for compuesto in self.maquina.lista_compuestos:
            print("---------------------")
            print(f"{i}. Nombre: {getattr(compuesto, 'nombre_compuesto', 'NA')}")
            print(f"Elementos: {getattr(compuesto, 'elemento', 'NA')}")
            print("---------------------")
            i += 1
        self.numero_compuesto = int(input("\nEscriba el numero del compuesto: "))
        compuesto_analizar = self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto)
        #print(f"Numero de instrucciones: {len(compuesto_analizar.elemento)+1}")
        # for i in range(1, len(compuesto_analizar.elemento+1)):
        #     self.accion.lista_instrucciones.agregar_nodo(i)
        
        
        input("\nPresione enter para continuar...")
        
        print("\nLISTADO DE MAQUINAS")
        j = 1
        for maquina in self.lista_maquinas:
            print("-------------------------")
            print(f"{j}. Nombre: {getattr(maquina, 'nombre', 'NA')}")
            tiempo = self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto).tiempo
            print(f"Tiempo: {tiempo + 1} segundos")
            print(f"Numero de Pines: {getattr(maquina, 'no_pines', 'NA')}")
            print("-------------------------")
            j += 1
        self.numero_maquina = int(input("\nEscriba el numero de la maquina con la cual trabajara: "))
        #maquina_analizar = self.lista_maquinas.buscar_por_indice(self.numero_maquina)
        # for j in range(1, tiempo + 1):
        #     self.accion.lista_pines.agregar_nodo(j)
            
        input("\nPresione enter para continuar...")
        
        print(f'\nTiempo optimo para construir "{compuesto_analizar.nombre_compuesto}" es de: {tiempo + 1} segundos\n')
        print(f'Instrucciones para construir el compuesto "{compuesto_analizar.nombre_compuesto}":\n')
        
        n = int(self.lista_maquinas.buscar_por_indice(self.numero_maquina).no_pines)+1
        self.conteo_pines = n
        m = int(tiempo)+2
        self.conteo_instrucciones = m
        funciones = ['Mover adelante', 'Mover atras', 'Esperar']
        elementos_fusionar = self.maquina.lista_compuestos.buscar_por_indice(self.numero_compuesto).elemento
        list(elementos_fusionar)
        
        for i in range(1, m):
            print("---------------------")
            print(f"Segundo {i}")
            for j in range(1, n):
                if i == 1:
                    print(f"Pin {j}", end="|")
                    print(self.accion.mover_adelante)
                    instruccion = self.accion.mover_adelante
                    self.accion.lista_instrucciones.agregar_nodo(instruccion)
                elif i % 2 == 0:
                    print(f"Pin {j}", end="|")
                    instruccion = f"Fusionar {list(elementos_fusionar)[i-2]}"
                    self.accion.lista_instrucciones.agregar_nodo(instruccion)
                    print(instruccion)
                    for k in range(j+1, n):
                        print(f"Pin {k}", end="|")
                        instruccion = random.choice(funciones)
                        self.accion.lista_instrucciones.agregar_nodo(instruccion)
                        print(instruccion)
                    break
                else:
                    for k in range(j, n-1):
                        instruccion = random.choice(funciones)
                        self.accion.lista_instrucciones.agregar_nodo(instruccion)
                        print(f"Pin {k}", end="|")
                        print(instruccion)
                    print(f"Pin {k+1}", end="|")
                    instruccion = f"Fusionar {list(elementos_fusionar)[i-2]}"
                    self.accion.lista_instrucciones.agregar_nodo(instruccion)
                    print(instruccion)
                    break
            print("---------------------\n")
                
        input("\nPresione enter para continuar...")
        
    def gestion_compuestos(self):
        regresar = False
        while not regresar:
            print("1. Ver lista de compuestos y formulas")
            print("2. Analizar compuesto")
            print("3. Regresar al Menu Principal")
            print ("\nElige una opcion")
 
            opcion = self.pedirNumeroEntero()
            
            if opcion == 1:
                print("\nLISTA DE COMPUESTOS")
                self.imprimir_compuesto()
            elif opcion == 2:
                self.analizar_compuesto()
            elif opcion == 3:
                regresar = True
                continue
        
    def abrir_archivo(self):
        #filename = "C:\\Users\\ACER\\Desktop\\Proyecto2\\entrada.xml"
        filename = filedialog.askopenfilename()
        xml = ET.parse(filename)
        self.cargarXml(xml)
    
    def archivo_graphviz(self):
        pass
    
    def eliminar_contenido(self):
        # Eliminar todas las máquinas
        self.lista_maquinas = ListaSimple()

        # Eliminar todos los elementos
        for maquina in self.lista_maquinas:
            maquina.lista_elementos = ListaSimple()

        # Eliminar todos los compuestos
        for maquina in self.lista_maquinas:
            for elemento in maquina.lista_elementos:
                elemento.lista_compuestos = ListaDobleEnlazada()

        # Establecer la máquina activa en nula
        self.maquina = None
    
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
                self.eliminar_contenido()
                print("\nLOS DATOS CARGADOS SE ELIMINARON CORRECTAMENTE")
            elif opcion == 2:
                #Generar archivo de entrada
                print("Seleccione el archivo a cargar...")
                root = tk.Tk()
                root.withdraw()
                self.abrir_archivo()
                print("\n¡ARCHIVO CARGADO CORRECTAMENTE!")
            elif opcion == 3:
                #Generar archivo de salida
                self.archivo_salida()
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