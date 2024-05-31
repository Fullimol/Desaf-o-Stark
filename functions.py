# def obtener_dato_por_key(key: str, lista: list) -> list:
#     """Retorna una lista con los valores de una clave de una lista de diccionarios

#     Args:
#         key (str): pasamos la clave del diccionario a buscar
#         lista (list): pasamos la lista de diccionarios donde buscar

#     Returns:
#         list: nueva lista con los valores de la clave
#     """
#     TAM = len(lista)
#     lista_retorno = []
#     for i in range(TAM):
#         lista_retorno.append(lista[i][key])
#     return lista_retorno


def mapear_lista(procesadora, lista: list) -> list:
    """ mapea una lista de diccionarios a una lista de tuplas

    Args:
        procesadora (_type_): pasamos la funcion lambda
        lista (list): pasamos la lista de diccionarios donde buscar

    Returns:
        list: _description_
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


# def superheroe_alturas_limites(lista:list, mas_alto=False) -> list:
#     """Retorna una tupla con el superhéroe mas alto y el superhéroe mas bajo"""
#     flag = False
#     altura_encontrada = 0
#     superheroe_encontrado = {}

#     for superheroe in lista:
#         if mas_alto == True:
#            if flag == False or float(superheroe["altura"]) > float(altura_encontrada):
#                altura_encontrada = float(superheroe["altura"])
#                superheroe_encontrado = superheroe
#                flag = True
#         else:
#             if flag == False or float(superheroe["altura"]) < float(altura_encontrada):
#                 altura_encontrada = float(superheroe["altura"])
#                 superheroe_encontrado = superheroe
#                 flag = True

#     return superheroe_encontrado


def obtener_mayor_menor(clave, lista:list, mas_alto=False) -> list:
    """Retorna una tupla con el superhéroe mas alto y el superhéroe mas bajo"""
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