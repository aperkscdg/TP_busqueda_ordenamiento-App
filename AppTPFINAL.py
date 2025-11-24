import time 
import os
import random as r

# Colores ANSI
RESET = "\033[0m"
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
WHITE = "\033[97m"
BOLD = "\033[1m"

def linea():
    print(CYAN + "──────────────────────────────────────────" + RESET)

def MainMenu():
    while True:
        os.system("cls")
        linea()
        print(BOLD + WHITE + "MENÚ PRINCIPAL" + RESET)
        linea()
        print(GREEN + "(0)" + RESET + " Algoritmo de ordenamiento")
        print(GREEN + "(1)" + RESET + " Algoritmo de búsqueda binaria")
        print(RED   + "(2)" + RESET + " Salir")
        linea()
        try:
            entrada = int(input(YELLOW + "Elija una opción: " + RESET))
            if entrada == 0:
                ordenamiento(entrada)
            if entrada == 1:
                busqueda(entrada)
            if entrada == 2:
                break
            if entrada > 2:
                print(RED + "Debe ingresar un número válido." + RESET)
                time.sleep(1)
                continue
        except ValueError:
            print(RED + "Error: Debes ingresar un número entero válido." + RESET)
            time.sleep(1)

def resultado(fin,inicio,arreglo,entrada,posicion,valor):
    os.system("cls")
    linea()
    print(BOLD + WHITE + "RESULTADO" + RESET)
    linea()
    if entrada == 0:
        print(GREEN + "Arreglo ordenado:" + RESET, arreglo) 
    if entrada == 1:
        if len(arreglo) == 0:
            print(RED + "La lista está vacía." + RESET)
        elif posicion is None:
            print(RED + "El número no se encuentra en la lista." + RESET)
        else:
            print(GREEN + "El número", valor, "está en la posición:", posicion, RESET)
    tiempo_seg = fin - inicio
    tiempo_ms = (fin - inicio) * 1000
    linea()
    if tiempo_seg >= 1:
        print(f"Tiempo: {tiempo_seg:.4f} segundos ({tiempo_ms:.2f} ms)")
    else:
        print(f"Tiempo: {tiempo_ms:.4f} ms")
    linea()
    input(YELLOW + "Presione ENTER para volver al menú..." + RESET)

def busqueda(opcion):
    lista=[]
    valor = None
    os.system("cls")
    while True:
        linea()
        print(BOLD + WHITE + "BÚSQUEDA BINARIA" + RESET)
        linea()
        print("Ingrese números ORDENADOS.")
        print("Número negativo = ejecutar algoritmo.")
        print("Número -2 = cargar datos automáticamente.")
        linea()
        try:
            entrada = int(input(YELLOW + "Ingrese un número: " + RESET))
            if entrada < 0 and entrada != -2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("¿Cuántos datos agregar?: "))
                    numero_agregar = 1
                    index = 0
                    lista.append(numero_agregar)
                    if cantidad > 500:
                        raise RuntimeError("Muchos datos")
                    while index != cantidad:
                        numero_random = r.randint(0,10)
                        if numero_random % 2 == 0:
                            numero_agregar += 5
                        else:
                            numero_agregar += 1
                        lista.append(numero_agregar)
                        index += 1
                    print(GREEN + "Lista generada automáticamente:" + RESET, lista)
                    input("Continuar...")
                    break
                except ValueError:
                    print(RED + "Debe ingresar un número válido." + RESET)
                    time.sleep(2)
                    continue
            lista.append(entrada)
            print(GREEN + "Lista actual:" + RESET, lista)
            time.sleep(1)
            os.system("cls")
        except ValueError:
            print(RED + "Debe ingresar un número válido." + RESET)
            time.sleep(2)
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
            return busqueda_binaria(lista, mitad + 1, derecha, valor)
        return None
    while valor is None:
        try:
            valor = int(input(YELLOW + "Número a buscar: " + RESET))
            posicion = busqueda_binaria(lista, izquierda, derecha, valor)
        except ValueError:
            print(RED + "Debe ingresar un número válido." + RESET)
            time.sleep(2)
    fin = time.perf_counter()
    resultado(fin,inicio,lista,opcion,posicion,valor)

def ordenamiento(opcion):
    os.system("cls")
    arreglo = []
    while True:
        linea()
        print(BOLD + WHITE + "ORDENAMIENTO (INSERTION SORT)" + RESET)
        linea()
        print("Ingrese números DESORDENADOS.")
        print("Número negativo = ejecutar algoritmo.")
        print("Número -2 = cargar datos automáticamente.")
        linea()
        try:
            entrada = int(input(YELLOW + "Ingrese un número: " + RESET))
            if entrada < 0 and entrada != -2:
                break
            if entrada == -2:
                try:
                    cantidad = int(input("¿Cuántos datos agregar?: "))
                    if cantidad > 500:
                        raise RuntimeError("Muchos datos")
                    for _ in range(cantidad):
                        arreglo.append(r.randint(0,500))
                    break
                except ValueError:
                    print(RED + "Debe ingresar un número válido." + RESET)
                    time.sleep(2)
                    continue
            arreglo.append(entrada)
            print(GREEN + "Lista actual:" + RESET, arreglo)
            time.sleep(1)
        except ValueError:
            print(RED + "Debe ingresar un número válido." + RESET)
            time.sleep(2)

    def insertion_sort(Arreglo):
        global inicio
        inicio = time.perf_counter()
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
