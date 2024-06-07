from os import system

def limpiar_consola():
    system('cls')


def pausar_programa():
    print()
    system('pause')


def menu_funciones():
    limpiar_consola()
    print(f'\t---- MENU DE FUNCIONES ----')
    print("A. Mostrar nombre de superheroes MASCULINO")
    print("B. Mostrar nombre de superheroes FEMENINOS")
    print("C. MASCULINO más ALTO")
    print("D. FEMENINO más ALTO")
    print("E. MASCULINO más BAJO")
    print("F. FEMENINO más BAJO")
    print("G. PROMEDIO altura MASCULINO")
    print("H. PROMEDIO altura FEMENINO")
    print("I. Identidad M mas alto y F mas baja")
    print("J. Cantidad CADA tipo de color de OJOS")
    print("K. Cantidad CADA tipo de color de PELO")
    print("L. Cantidad CADA tipo de inteligencia")
    print("M. AGRUPAR por color de OJOS")
    print("N. AGRUPAR por color de PELO")
    print("O. AGRUPAR POR tipo de INTELIGENCIA")
    print("P. Finalizar programa")
    seleccion =  input(f'\n\tIngrese opcion: ').upper()
    while seleccion not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']:
        print(f'ERROR: OPCION {seleccion} NO VALIDA')
        seleccion =  input(f'\n\tIngrese opcion: ').upper()
    return seleccion


def verificar_lista(lista:list) -> None:
    if type(lista) != list:
        raise TypeError("Error. No se puede procesar un objeto que no es lista")
    elif len(lista) == 0:
        raise ValueError("Error. Lista vacia")


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
    verificar_lista(lista)
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
    verificar_lista(lista)
    return round(sumar_lista(lista) / len(lista), 2)


def obtener_cada_elemento_disponible(lista: list) -> list:
    """Esto es para que no se repitan las elementos de una lista.

    Args:
        lista (list): pasamos la lista.

    Returns:
        list: una lista de todos los elementos sin repeticiones.
    """
    verificar_lista(lista)

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
    verificar_lista(lista)

    lista_filtrada = []
    for elemento in lista:
        if elemento[key] == elemento_buscado:
            lista_filtrada.append(elemento)
    return lista_filtrada


def crear_lista_con_valores_de_clave(lista: list, clave: str) -> list:
    """Retorna una lista con los valores de una clave de una lista de diccionarios

    Args:
        lista (list): Lista de diccionarios donde buscar
        clave (str): clave para obtener los valores

    Returns:
        list: nueva lista con los valores de la clave, sin repeticiones
    """
    verificar_lista(lista)
    valores_obtenidos = mapear_lista(lambda super: super[clave], lista) # guardo en una lista cada valor de la clave del diccionario.
    valores_sin_repeticiones = obtener_cada_elemento_disponible(valores_obtenidos) # creo una lista sin repeticiones de cada dato mapeado.
    return valores_sin_repeticiones


def agrupar_segun_condicion(lista: list, lista_elemntos: list, clave_buscada: str, clave_a_mostrar: str) -> None:
    """ Devuelve los nombres agrupados segun cada caracteristica en comun.

    Args:
        lista (list): Pasamos la lista de diccionarios
        lista_elemntos (list): Pasamos la lista con las similitudes a agrupar
        clave_buscada (str): Pasamos la clave del diccionario a buscar
        clave_a_mostrar (str): Pasamos la clave del diccionario a mostrar por print.
    """
    verificar_lista(lista)
    verificar_lista(lista_elemntos)

    for i in range(len(lista_elemntos)):
        print(f"\n      ({lista_elemntos[i]})")
        for element in lista:
            if element[clave_buscada] == lista_elemntos[i]:
                print(F"> {element[clave_a_mostrar]}")