
def eliminarDuplicados(arreglo):
    arregloSinDuplicados = []
    for elemento in arreglo:
        if elemento not in arregloSinDuplicados:
            arregloSinDuplicados.append(elemento)
    print (arregloSinDuplicados)

eliminarDuplicados([4,2,6,7,4,6,3,2])