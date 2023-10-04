def mejor_Ajuste(tamano_Proceso, espacio_Memoria, procesos_Memoria):    #Funcion del algoritmo del mejor ajuste
    mejor_Ajuste_Idx = -1
    espacio_Libre = float('inf')

    for i in range(len(espacio_Memoria)):
        if espacio_Memoria[i] >= tamano_Proceso and espacio_Memoria[i] - tamano_Proceso < espacio_Libre:
            mejor_Ajuste_Idx = i
            espacio_Libre = espacio_Memoria[i] - tamano_Proceso

    if mejor_Ajuste_Idx != -1:
        procesos_Memoria.append(tamano_Proceso)
        espacio_Memoria[mejor_Ajuste_Idx] -= tamano_Proceso
        print(f"Proceso de {tamano_Proceso} KB asignado al espacio {mejor_Ajuste_Idx}")
    else:
        print(f"Proceso {proceso}: Tamaño {tamano_Proceso} KB no hay suficiente espacio en la memoria")

def primer_Ajuste(tamano_Proceso, espacios_Memoria):    #Funcion del algoritmo del primer ajuste
    for i in range(len(espacios_Memoria)):
        if espacios_Memoria[i] >= tamano_Proceso:
            print(f"Proceso de {tamano_Proceso} KB asignado al espacio {i}")
            espacios_Memoria[i] -= tamano_Proceso
            return True
    return False

def peor_Ajuste(espacios_Memoria, tamano_Proceso):  #Funcion del algoritmo del peor ajuste
    for proceso in tamano_Proceso:
        peor_Ajuste_Index = -1
        peor_Ajuste_Tamano = -1

        for i in range(len(espacios_Memoria)):
            if espacios_Memoria[i] >= proceso[1]:
                if peor_Ajuste_Index == -1 or espacios_Memoria[i] > espacios_Memoria[peor_Ajuste_Index]:
                    peor_Ajuste_Index = i
                    peor_Ajuste_Tamano = espacios_Memoria[i]

        if peor_Ajuste_Index != -1:
            espacios_Memoria[peor_Ajuste_Index] -= proceso[1]
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"Proceso de {proceso[1]} KB asignado en el espacio {peor_Ajuste_Index}")
        else:
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"Proceso {proceso[0]}: Tamaño {proceso[1]} KB no hay suficiente espacio en la memoria")

def siguiente_Ajuste(espacios_Memoria, tamano_Proceso): #Funcion del algoritmo del siguiente ajuste
    ultimo_Indice_Asignado = 0

    for proceso in tamano_Proceso:
        proceso_Asignado = False

        for i in range(ultimo_Indice_Asignado, len(espacios_Memoria)):
            if espacios_Memoria[i] >= proceso[1]:
                espacios_Memoria[i] -= proceso[1]
                print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
                print(f"Proceso de {proceso[1]} KB asignado en el espacio {i}")
                proceso_Asignado = True
                ultimo_Indice_Asignado = i + 1
                break

        if not proceso_Asignado:
            print(f"Procesando: {proceso[0]} ({proceso[1]} KB)")
            print(f"No se pudo asignar el proceso {proceso[0]} de {proceso[1]} KB")

#Espacios de memoria para los algoritmos
espacio_Memoria1 = [1000, 400, 1800, 700, 900, 1200, 1500]
espacio_Memoria2 = [1000, 400, 1800, 700, 900, 1200, 1500]
espacio_Memoria3 = [1000, 400, 1800, 700, 900, 1200, 1500]
espacio_Memoria4 = [1000, 400, 1800, 700, 900, 1200, 1500]

#Menu del programa
while True:
    print("\n\tMenu\n")
    print("Espacio de Memoria: [1000, 400, 1800, 700, 900, 1200, 1500]\n")
    print("Selecciona un algoritmo de asignación de memoria:")
    print("1. Mejor Ajuste")
    print("2. Primer Ajuste")
    print("3. Peor Ajuste")
    print("4. Siguiente Ajuste")
    print("5. Salir")

    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == '1':
        print("\n\tMejor Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso, tamano = linea.strip().split(', ')
            tamano_Proceso = int(tamano.replace('kb', ''))
            print(f"Procesando: {proceso} ({tamano_Proceso} KB)")
            mejor_Ajuste(tamano_Proceso, espacio_Memoria1, procesos_en_Memoria)

        # Estado actual de la memoria después de asignar procesos
        print("\n\tEstado actual de la memoria:\n")
        for i in range(len(espacio_Memoria1)):
            print(f"Espacio {i}: {espacio_Memoria1[i]} KB")

    elif opcion == '2':
        print("\n\tPrimer Ajuste\n")
        with open('archivos.txt', 'r') as file:
            lineas = file.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso, tamano = linea.strip().split(', ')
            tamano = int(tamano[:-2])
            procesos_en_Memoria.append((proceso, tamano))
            
        for proceso, tamano in procesos_en_Memoria:
            print(f"Procesando: {proceso} ({tamano} KB)")
            if not primer_Ajuste(tamano, espacio_Memoria2):
                print(f"Proceso {proceso}: Tamaño {tamano} KB no hay suficiente espacio en la memoria")
        
        # Estado actual de la memoria después de asignar procesos
        print("\n\tEstado actual de la memoria:\n")
        for i in range(len(espacio_Memoria2)):
            print(f"Espacio {i}: {espacio_Memoria2[i]} KB")

    elif opcion == '3':
        print("\n\tPeor Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso = linea.strip().split(", ")
            nombre_Proceso = proceso[0]
            tamano_Proceso = int(proceso[1].replace("kb", ""))
            procesos_en_Memoria.append((nombre_Proceso, tamano_Proceso))

        peor_Ajuste(espacio_Memoria3, procesos_en_Memoria)

        # Estado actual de la memoria después de asignar procesos
        print("\n\tEstado actual de la memoria:\n")
        for i in range(len(espacio_Memoria3)):
            print(f"Espacio {i}: {espacio_Memoria3[i]} KB")

    elif opcion == '4':
        print("\n\tSiguiente Ajuste\n")
        with open("archivos.txt", "r") as archivo:
            lineas = archivo.readlines()

        procesos_en_Memoria = []
        for linea in lineas:
            proceso = linea.strip().split(", ")
            nombre_Proceso = proceso[0]
            tamano_Proceso = int(proceso[1].replace("kb", ""))
            procesos_en_Memoria.append((nombre_Proceso, tamano_Proceso))

        siguiente_Ajuste(espacio_Memoria4, procesos_en_Memoria)

        # Estado actual de la memoria después de asignar procesos
        print("\n\tEstado actual de la memoria:\n")
        for i in range(len(espacio_Memoria4)):
            print(f"Espacio {i}: {espacio_Memoria4[i]} KB")

    elif opcion == '5':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
