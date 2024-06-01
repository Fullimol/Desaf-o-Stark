from os import system

def limpiar_consola():
    system('cls')

def pausar():
    print()
    system('pause')

def mapear_lista(procesadora, lista: list) -> list:
    """ Recorre una lista de diccionarios y devuelve una lista de tuplas con el resultado de la llamada a la función

    Args:
        procesadora (_type_): pasamos la funcion lambda.
        lista (list): pasamos la lista de diccionarios donde buscar.

    Returns:
        list: Nueva lista de tuplas.
    """
    lista_retorno = []
    for elemento in lista:
        try:
            lista_retorno.append(procesadora(elemento))
        except:
            TypeError("No se puede procesar un objeto que no es lista")
    return lista_retorno



def mostrar_lista_tupla(lista:list) -> None:
    """Imprime una lista de tuplas

    Args:
        lista (list): pasamos la lista de tuplas a imprimir
    """
    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento}", end=" ")
        print()


def obtener_mayor_menor(clave, lista:list, mas_alto=False) -> list:
    """Obtengo el valor más alto o más bajo de la clave de un diccionario

    Args:
        clave (_type_): Ingreso la clave a buscar.
        lista (list): Ingreso la lista de diccionarios.
        mas_alto (bool, optional): Si es TRUE busca el valor mas alto.

    Raises:
        ValueError: Error. Lista vacia.

    Returns:
        list: una lista con SOLO el superheroe con el valor max o min.
    """
    if len(lista) == 0:
        raise ValueError("Error. Lista vacia")

    flag = False
    numero_inicial = 0
    superheroe_encontrado = {}

    for superheroe in lista:
        if mas_alto == True:
           if flag == False or float(superheroe[clave]) > float(numero_inicial):
               numero_inicial = float(superheroe[clave])
               superheroe_encontrado = superheroe
               flag = True
        else:
            if flag == False or float(superheroe[clave]) < float(numero_inicial):
                numero_inicial = float(superheroe[clave])
                superheroe_encontrado = superheroe
                flag = True

    return superheroe_encontrado


def sumar_lista(lista:list)->int:
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def calcular_promedio(lista:list) -> float:
    if len(lista) == 0:
        raise ValueError("Error. Lista vacia")
    else:
        return round(sumar_lista(lista) / len(lista), 2)
    

def obtener_cada_elemento_disponible(lista: list) -> list:
    """Esto es para que no se repitan las elementos de una lista

    Args:
        lista (list): pasamos la lista

    Returns:
        list: la lista sin repeticiones
    """
    nueva_lista = []
    for elemento in lista:
        if elemento not in nueva_lista:
            nueva_lista.append(elemento)
    return nueva_lista


def filtrar_lista(key, lista, elemento_buscado) -> list:
    """Esto devuelve la lista filtrada por el parametro buscado

    Args:
        key (_type_): pasamos la clave del diccionario
        lista (_type_): pasamos la lista
        elemento_buscado (_type_): pasamos el elemento para filtrar

    Returns:
        list: la lista filtrada
    """
    lista_filtrada = []
    for superheroe in lista:
        if superheroe[key] == elemento_buscado:
            lista_filtrada.append(superheroe)
    return lista_filtrada