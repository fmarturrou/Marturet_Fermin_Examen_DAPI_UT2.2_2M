def OrdenarLista(numeros):

    numeros_ordenados = sorted(numeros, reverse=True)
    
    with open('listaordenada.txt', 'w') as archivo:
        for numero in numeros_ordenados:
            archivo.write(f"{numero}\n")

    """
    Esta función ordena una lista de números enteros de mayor a menor y escribe la lista ordenada 
    en el archivo ListaOrdenada.txt.
    
    La función ordena los números de la lista de mayor a menor
    utilizando la función sorted(), y luego escribe cada número en el archivo 
    ListaOrdenada.txt.
    
    Esta función no devuelve ningún valor, solo modifica el archivo de salida.
    """

OrdenarLista([257, 249, 252, 301, 234, 250, 87, 4414, 2455, 107, 2307])

def NumeroPar():
    """
    Esta función lee un archivo que contiene una lista de números, filtra los números pares y 
    los escribe en un archivo llamado ListaDePares.txt.
    
    Esta función no recibe argumentos y no devuelve nada.
    La lista de números debe estar en el archivo ListaOrdenada.txt.
    """
    
    with open('ListaOrdenada.txt', 'r') as archivo_entrada:
        numeros = [int(linea.strip()) for linea in archivo_entrada]
        
        numeros_pares = [numero for numero in numeros if numero % 2 == 0]
        with open('ListaDePares.txt', 'w') as archivo_salida:
            for numero in numeros_pares:
                archivo_salida.write(f"{numero}\n")

NumeroPar()