from data_stark import lista_personajes
from functions import *

# Desafío #01:
# X A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# X B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# x C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# x D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# X E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# X F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# X G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# X H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
# X I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# x J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# x K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# x L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
# x M. Listar todos los superhéroes agrupados por color de ojos.
# x N. Listar todos los superhéroes agrupados por color de pelo.
# x O. Listar todos los superhéroes agrupados por tipo de inteligencia.

personajes_masculinos = filtrar_lista("genero", lista_personajes, 'M')
personajes_femeninos = filtrar_lista("genero", lista_personajes, 'F')

while True:
    match menu_funciones():
        case "A":
            print(f'\n\tSUPERHEROES MASCULINOS: ')
            for super in personajes_masculinos:
                print(super["nombre"])
            pausar_programa()

        case "B":
            print(f'\n\tSUPERHEROES FEMENINOS: ')
            for super in personajes_femeninos:
                print(super["nombre"])
            pausar_programa()

        case "C":
            masculino_mas_alto = obtener_mayor_menor("altura", personajes_masculinos, True)
            print(f'El Masculino mas Alto es: {masculino_mas_alto["nombre"]} con {round(float(masculino_mas_alto["altura"]), 2)}')
            pausar_programa()

        case "D":
            femenino_mas_alto = obtener_mayor_menor("altura", personajes_femeninos, True)
            print(f'El Femenino mas Alto es: {femenino_mas_alto["nombre"]} con {round(float(femenino_mas_alto["altura"]), 2)}')
            pausar_programa()

        case "E":
            masculino_mas_bajo = obtener_mayor_menor("altura", personajes_masculinos, False)
            print(f'El Masculino mas Bajo es: {masculino_mas_bajo["nombre"]} con {round(float(masculino_mas_bajo["altura"]), 2)}')
            pausar_programa()

        case "F":
            femenino_mas_bajo = obtener_mayor_menor("altura", personajes_femeninos, False)
            print(f'El Femenino mas Bajo es: {femenino_mas_bajo["nombre"]} con {round(float(femenino_mas_bajo["altura"]), 2)}')
            pausar_programa()

        case "G":
            todas_alturas_masculinos = mapear_lista(lambda super: (float(super["altura"])), personajes_masculinos)
            promedio = calcular_promedio(todas_alturas_masculinos)
            print(f'El PROMEDIO de las alturas de MASCULINOS es: {promedio}')
            pausar_programa()

        case "H":
            promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), personajes_femeninos))
            print(f'El PROMEDIO de las alturas de FEMENINOS es: {promedio}')
            pausar_programa()

        case "I":
            masculino_mas_alto = obtener_mayor_menor("altura", personajes_masculinos, True)
            femenino_mas_bajo = obtener_mayor_menor("altura", personajes_femeninos, False)
            print(f'El Masculino mas Alto es {masculino_mas_alto["identidad"]} y la Femenina mas Baja es {femenino_mas_bajo["identidad"]}')
            pausar_programa()

        case "J":
            for elemento in crear_lista_con_valores_de_clave(lista_personajes, "color_ojos"):
                print(f"La cantidad con OJOS COLOR '{elemento}' es {len(filtrar_lista('color_ojos', lista_personajes, elemento))}")
            pausar_programa()

        case "K":
            for elemento in crear_lista_con_valores_de_clave(lista_personajes, "color_pelo"):
                print(f"La cantidad con PELO COLOR '{elemento}' es {len(filtrar_lista('color_pelo', lista_personajes, elemento))}")
            pausar_programa()

        case "L":
            for elemento in crear_lista_con_valores_de_clave(lista_personajes, "inteligencia"):
                if elemento == "":
                    print(f"{len(filtrar_lista('inteligencia', lista_personajes, elemento))} No tiene inteligencia")
                else:
                    print(f"La cantidad de inteligencia '{elemento}' es {len(filtrar_lista('inteligencia', lista_personajes, elemento))}")
            pausar_programa()

        case "M":
            print(f'\n\tAGRUPAR POR COLOR DE OJOS: ')
            colores_ojos = crear_lista_con_valores_de_clave(lista_personajes, "color_ojos")
            agrupar_segun_condicion(lista_personajes, colores_ojos, "color_ojos", "nombre")
            pausar_programa()

        case "N":
            print(f'\n\tAGRUPAR POR COLOR DE PELO: ')
            colores_pelo = crear_lista_con_valores_de_clave(lista_personajes, "color_pelo")
            agrupar_segun_condicion(lista_personajes, colores_pelo, "color_pelo", "nombre")
            pausar_programa()

        case "O":
            print(f'\n\tAGRUPAR POR TIPO DE INTELIGENCIA:')
            nivel_inteligencia = crear_lista_con_valores_de_clave(lista_personajes, "inteligencia")
            agrupar_segun_condicion(lista_personajes, nivel_inteligencia, "inteligencia", "nombre")
            pausar_programa()

        case "P":
            break

print(f'\n\t¡¡ FIN DEL PROGRAMA !!')