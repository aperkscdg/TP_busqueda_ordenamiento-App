import time 
import os
import random as r

def MainMenu():
    while True:
        os.system("cls")
        print("Elige un algoritmo que quieras usar: ")
        print("Algoritmo de ordenamiento: (0)")
        print("Algoritmo de búsqueda binaria: (1)")
        print("Salir: (2)")
        try:
            entrada = int(input("Elija una opción: "))
            if entrada == 0:
                ordenamiento(entrada)
            if entrada == 1:
                busqueda(entrada)
            if entrada == 2:
                break
            if entrada > 2:
                print("Poner un número válido en el menú.")
                os.system("cls")
                continue
        except ValueError:
            os.system("cls")
            print("Error: Debes ingresar un número entero válido.")
            time.sleep(1)
            continue

def resultado(fin, inicio, arreglo, entrada, posicion, valor):
    os.system("cls")
    if entrada == 0:
        print("El arreglo ordenado es este:", arreglo)
    if entrada == 1:
        if len(arreglo) == 0:
            print("La lista está vacía.")
        elif posicion is None:
            print("El número no está en la lista.")
        else:
            print("El número", valor, "está en la posición:", posicion)

    tiempo_seg = fin - inicio
    tiempo_ms = (fin - inicio) * 1000
    if tiempo_seg >= 1:
        print(f"Tardó {tiempo_seg:.4f} segundos ({tiempo_ms:.2f} ms)")
        input("Presione cualquier tecla para volver al menú: ")
        return
    else:
        print(f"Tardó {tiempo_ms:.4f} ms")
        input("Presione cualquier tecla para volver al menú: ")
        return 

def busqueda(opcion):
    lista = []
    valor = None
    os.system("cls")
    while True:
        print("Ingrese números de forma ordenada para poder buscar el número.")
        print("Agregue un número negativo para salir y ejecutar el algoritmo.")
        print("El número -2 sirve para agregar datos automáticamente.")
        try:
            entrada = int(input("Ingrese un número entero para agregar a su arreglo: "))
            if entrada < 0 and entrada != -2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("¿Cuántos datos quieres agregar?: "))
                    numero_agregar = 1
                    index = 0
                    lista.append(numero_agregar)
                    if cantidad > 500:
                        raise RuntimeError("Muchos datos")
                    while index != cantidad:
                        numero_random = r.randint(0, 10)
                        if numero_random % 2 == 0:
                            numero_agregar = numero_agregar + 5
                            lista.append(numero_agregar)
                        else:
                            numero_agregar += 1
                            lista.append(numero_agregar)
                        index += 1
                    print("La lista ordenada quedó de esta forma:", lista)
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

    def busqueda_binaria(lista, izquierda, derecha, valor):
        global inicio
        inicio = time.perf_counter()
        mitad = (izquierda + derecha) // 2
        if izquierda <= derecha:
            if lista[mitad] == valor:
                return mitad
            if lista[mitad] > valor:
                return busqueda_binaria(lista, izquierda, mitad - 1, valor)
            if lista[mitad] < valor:
                return busqueda_binaria(lista, mitad + 1, derecha, valor)
        else:
            return None
    while valor is None:
        try:
            valor = int(input("Ingrese el número que quiere buscar: "))
            posicion = busqueda_binaria(lista, izquierda, derecha, valor)
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")
            time.sleep(2)
            continue

    fin = time.perf_counter()
    resultado(fin, inicio, lista, opcion, posicion, valor)

def ordenamiento(opcion):
    os.system("cls")
    arreglo = []
    while True:
        try:
            os.system("cls")
            print("Agregue un número negativo para salir y ejecutar el algoritmo.")
            print("Agregue números de forma desordenada para ver el funcionamiento del algoritmo.")
            print("El número -2 sirve para agregar datos automáticamente.")
            entrada = int(input("Ingrese un número entero para agregar al arreglo: "))
            if entrada < 0 and entrada != -2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("¿Cuántos datos quiere agregar a su arreglo?: "))
                    for datos in range(0, cantidad):
                        if cantidad > 500:
                            raise RuntimeError("Muchos datos")
                        arreglo.append(r.randint(0, 500))
                    print("La lista ordenada quedó de esta forma:", arreglo)
                    input("Siguiente: ")
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
        numero = 0
        print("Lista original:", Arreglo)
        for index in range(1, len(Arreglo)):
            numero = Arreglo[index]
            while index > 0 and Arreglo[index - 1] > numero:
                Arreglo[index] = Arreglo[index - 1]
                index -= 1
            Arreglo[index] = numero
        return Arreglo 

    arreglo = insertion_sort(arreglo)
    fin = time.perf_counter()
    resultado(fin, inicio, arreglo, opcion, None, None)

MainMenu()
