from data_stark import lista_personajes
from functions import *
from os import system

# Desafío #01:

# X A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# X B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# x C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# x D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# X E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# X F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# X G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# X H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
# CONSULTAR       I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# x J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# x K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# x L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).

# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia


def menu_funciones():
    print(f'\t---- MENU DE FUNCIONES ----')
    print("A. Mostrar nombre de superheroes MASCULINO")
    print("B. Mostrar nombre de superheroes FEMENINOS")
    print("C. MASCULINO más ALTO")
    print("D. FEMENINO más ALTO")
    print("E. MASCULINO más BAJO")
    print("F. FEMENINO más BAJO")
    print("G. PROMEDIO altura MASCULINO")
    print("H. PROMEDIO altura FEMENINO")
    print("I. (sin hacer)")
    print("J. Cantidad CADA tipo de color de OJOS")
    print("K. Cantidad CADA tipo de color de PELO")
    print("L. Cantidad CADA tipo de color inteligencia")
    print("M. (sin hacer)")
    print("N. (sin hacer)")
    print("O. (sin hacer)")

    seleccion =  input(f'\n\tIngrese opcion: ')
    while seleccion not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']:
        print(f'ERROR: OPCION {seleccion} NO VALIDA')
        seleccion =  input(f'\n\tIngrese opcion: ')
    return seleccion


while True:
    match menu_funciones():
        case "A":
            print(f'\n\tSUPERHEROES MASCULINOS: ')
            for super in filtrar_lista("genero", lista_personajes, 'M'):
                print(super["nombre"])
        case "B":
            print(f'\n\tSUPERHEROES FEMENINOS: ')
            for super in filtrar_lista("genero", lista_personajes, 'F'):
                print(super["nombre"])
        case "C":
            personajes_masculinos = filtrar_lista("genero", lista_personajes, 'M')
            masculino_mas_alto = obtener_mayor_menor("altura", personajes_masculinos, True)
            print(f'El Masculino mas Alto es: {masculino_mas_alto["nombre"]} con {round(float(masculino_mas_alto["altura"]), 2)}')
        case "D":
            personajes_femeninos = filtrar_lista("genero", lista_personajes, 'F')
            femenino_mas_alto = obtener_mayor_menor("altura", personajes_femeninos, True)
            print(f'El Femenino mas Alto es: {femenino_mas_alto["nombre"]} con {round(float(femenino_mas_alto["altura"]), 2)}')
        case "E":
            personajes_masculinos = filtrar_lista("genero", lista_personajes, 'M')
            masculino_mas_bajo = obtener_mayor_menor("altura", personajes_masculinos, False)
            print(f'El Masculino mas Bajo es: {masculino_mas_bajo["nombre"]} con {round(float(masculino_mas_bajo["altura"]), 2)}')
        case "F":
            personajes_femeninos = filtrar_lista("genero", lista_personajes, 'F')
            femenino_mas_bajo = obtener_mayor_menor("altura", personajes_femeninos, False)
            print(f'El Femenino mas Bajo es: {femenino_mas_bajo["nombre"]} con {round(float(femenino_mas_bajo["altura"]), 2)}')
        case "G":
            personajes_masculinos = filtrar_lista("genero", lista_personajes, 'M')
            mapear_lista(lambda super: (float(super["altura"])), personajes_masculinos)
            promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), personajes_masculinos))
            print(f'El PROMEDIO de las alturas de MASCULINOS es: {promedio}')
        case "H":
            personajes_femeninos = filtrar_lista("genero", lista_personajes, 'F')
            mapear_lista(lambda super: (float(super["altura"])), personajes_femeninos)
            promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), personajes_femeninos))
            print(f'El PROMEDIO de las alturas de FEMENINOS es: {promedio}')
        case "I":
            print("NO SE QUE HAY QUE HACER!!!!")
        case "J":
            lista_colores_ojos = mapear_lista(lambda super: super["color_ojos"], lista_personajes)  #Obtengo la lista de colores
            colores_ojos = obtener_cada_elemento_disponible(lista_colores_ojos) #Obtengo la lista de colores sin repetición

            for elemento in colores_ojos:
                print(f"La cantidad con OJOS COLOR {elemento} es {len(filtrar_lista('color_ojos', lista_personajes, elemento))}")
        case "K":
            lista_colores_pelo = mapear_lista(lambda super: super["color_pelo"], lista_personajes)  #Obtengo la lista de colores
            colores_pelo = obtener_cada_elemento_disponible(lista_colores_pelo) #Obtengo la lista de colores sin repetición

            for elemento in colores_pelo:
                print(f"La cantidad con PELO COLOR {elemento} es {len(filtrar_lista('color_pelo', lista_personajes, elemento))}")
        case "L":
            lista_por_inteligencia= mapear_lista(lambda super: super["inteligencia"], lista_personajes)  #Obtengo la lista de colores
            nivel_inteligencia = obtener_cada_elemento_disponible(lista_por_inteligencia) #Obtengo la lista de colores sin repetición

            for elemento in nivel_inteligencia:
                if elemento == "":
                    print(f"{len(filtrar_lista('inteligencia', lista_personajes, elemento))} No tiene inteligencia")
                else:
                    print(f"La cantidad de inteligencia {elemento} es {len(filtrar_lista('inteligencia', lista_personajes, elemento))}")
        case "M":
            print("sin hacer")
        case "N":
            print("sin hacer")
        case "O":
            print("sin hacer")

        


    print(f'\n\tFIN DEL PROGRAMA') 