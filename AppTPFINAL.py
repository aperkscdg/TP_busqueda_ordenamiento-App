
import time 
import os
import random as r

def MainMenu():
    while True:
        os.system("cls")
        print("Elije un algotirmo que quieras usar: ")
        print("Algotirmo de ordenamiento: (0) ")
        print("Algoritmo de bosqueda binaria: (1) ")
        print("Salir: (3) " )
        try:
            entrada = int(input("elija una opcion: "))
            if entrada == 0:
                ordenamiento(entrada)
            if entrada == 1:
                busqueda(entrada)
            if entrada == 2:
                break
            if entrada >2:
                print("Poner un numero valido en el menu: ")
                os.system("cls")
                continue
        except ValueError:
            os.system("cls")
            print("Error: Debes ingresar un número entero válido: ")
            time.sleep(1)
            continue

def resultado(fin,inicio,arreglo,entrada,posicion,valor):
    os.system("cls")
    if entrada == 0:
        print("El Arreglo ordenado es este: ", arreglo)
    if entrada == 1:
            if len(arreglo) == 0:
                print("la lista esta vacia")
            elif posicion == None:
                print("El numero no esta en lista")
            else:
                print("El numero", valor , "Esta en la posicion: ", posicion)
    tiempo_seg = fin - inicio
    tiempo_ms = (fin - inicio) * 1000
    if tiempo_seg >= 1:
        print(f"Tardó {tiempo_seg:.4f} segundos ({tiempo_ms:.2f} ms)")
        input("precione cualquier cosa para volver al menu: ")
        return
    else:
        print(f"Tardó {tiempo_ms:.4f} ms")
        input("precione cualquier cosa para volver al menu: ")
        return 

def busqueda(opcion):
    lista=[]
    valor = None
    os.system("cls")
    while True:
        print("Ingrese Numero de forma Ordenada para poder buscar el numero")
        try:
            entrada = int(input("ingrese un numero entero para agregar en su arreglo: "))
            if entrada <0 and entrada !=-2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("Cuantos Datos Quieres Agregar: "))
                    numero_agregar = int(1)
                    index = 0
                    lista.append(numero_agregar)
                    if cantidad >500:
                            raise RuntimeError("Muchos Datos")
                    while index != cantidad:
                        numero_random = r.randint(0,10)
                        if numero_random %2==0:
                            numero_agregar=numero_agregar+5
                            lista.append(numero_agregar)
                        else:
                            numero_agregar+=1
                            lista.append(numero_agregar)
                        index+=1
                    print("La lista ordenada quedo de esta forma: ", lista)
                    input("Siguiente: ")
                    break
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")
                    time.sleep(2)
                    os.system("cls")
                    continue
            lista.append(entrada)
            print(lista)
            time.sleep(1)
            os.system("cls")
            continue
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            time.sleep(2)
            os.system("cls")
            continue
    izquierda = 0
    derecha = len(lista) - 1
    def busqueda_binaria(lista,izquierda,derecha,valor):
        global inicio
        inicio = time.perf_counter()
        mitad = (izquierda + derecha) // 2
        if izquierda <= derecha:
            if lista[mitad] == valor:
                return mitad
            if lista[mitad] > valor:
                return busqueda_binaria(lista,izquierda,mitad-1,valor)
            if lista[mitad] < valor:
                return busqueda_binaria(lista,mitad+1,derecha,valor)
        else:
            return posicion == None
    while valor == None:
        try:
            valor = int(input("ingrese el numero que quiera buscar: "))
            posicion = busqueda_binaria(lista,izquierda,derecha,valor)
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            time.sleep(2)
            continue
    fin = time.perf_counter()
    resultado(fin,inicio,lista,opcion,posicion,valor)

def ordenamiento(opcion):
    os.system("cls")
    arreglo=[]
    while True:
        try:
            os.system("cls")
            print("Agregue un numero negativo para salir y ajecutar el algotirmo ")
            print("Agregue numeros de forma desordenada, para ver el funcionamiento del algoritmo ")
            entrada = int(input("ingrese un numero entero para agregar al arreglo: "))
            if entrada <0 and entrada !=-2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("Cuantos datos quiere agregar a su arreglo: "))
                    for datos in range(0,cantidad):
                        if cantidad > 500:
                            raise RuntimeError("Muchos Datos")
                        arreglo.append(r.randint(0,500))
                    break
                except ValueError:
                    print("Error: Debes ingresar un número entero válido.")
                    time.sleep(2)
                    os.system("cls")
                    continue
            arreglo.append(entrada)
            print(arreglo)
            time.sleep(1)
            continue
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            time.sleep(2)
            continue
    def insertion_sort(Arreglo):
        global inicio
        inicio = time.perf_counter()
        numero=int(0)
        print("lista original: ", Arreglo)
        for index in range(1, len(Arreglo)):
            numero = Arreglo[index]
            while index > 0 and Arreglo[index-1] > numero:
                Arreglo[index] = Arreglo[index-1]
                index-=1
            Arreglo[index]=numero
        return Arreglo 
    arreglo = insertion_sort(arreglo)
    fin = time.perf_counter()
    resultado(fin,inicio,arreglo,opcion,None,None)

MainMenu()