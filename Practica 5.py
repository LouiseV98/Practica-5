def extract_size(size_str):
    # Eliminar "kb" y convertir a entero
    return int(size_str.replace("kb", ""))

def first_fit(memory, process_name, process_size):
    for i in range(len(memory)):
        if memory[i] is None:
            if allocate(memory, i, process_size, process_name):
                return i
    return -1

def allocate(memory, process_name, process_size, memory_sizes, block_start):
    for i in range(block_start, len(memory_sizes)):
        if process_size <= memory_sizes[i]:
            for j in range(len(memory)):
                if memory[j] is None and j + process_size <= len(memory):
                    block_free = True
                    for k in range(j, j + process_size):
                        if memory[k] is not None:
                            block_free = False
                            break
                    if block_free:
                        for k in range(j, j + process_size):
                            memory[k] = process_name
                        return i  # Devuelve el índice del bloque de memory_sizes asignado
    return -1  # Devuelve -1 si no se pudo asignar

def algoritmo_Primer_Ajuste():
    memory_sizes = [1000, 400, 1800, 700, 900, 1200, 1500]  # Tamaños de los bloques de memoria en KB
    memory = [None] * sum(memory_sizes)  # Crear la lista de memoria con la suma de los tamaños

    # Procesar el archivo con nombres de archivos y tamaños
    with open("archivos.txt", "r") as file:
        block_start = 0
        for line in file:
            line = line.strip()
            process_name, process_size_str = line.split(",")
            process_name = process_name.strip()
            process_size = int(process_size_str.replace("kb", ""))
            allocated_index = allocate(memory, process_name, process_size, memory_sizes, block_start)
            if allocated_index != -1:
                print(f"Proceso '{process_name}' asignado al bloque {allocated_index}.")
                block_start = allocated_index + 1  # Actualiza el inicio del bloque
            else:
                print(f"No se pudo asignar el proceso '{process_name}' debido a la falta de memoria.")

if __name__ == "__main__":
    algoritmo_Primer_Ajuste()





