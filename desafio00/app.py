from data_stark import lista_personajes
from functions import *

# Desafío #00:

# A. Analizar detenidamente el set de datos
# x B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# x C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# x D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# x E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# x F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
# x G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# x H. Calcular e informar cual es el superhéroe más y menos pesado.
# x I. Ordenar el código implementando una función para cada uno de los valores informados.
# x J. Construir un menú que permita elegir qué dato obtener


#B)
mostrar_lista_tupla(mapear_lista(lambda super: (super["nombre"]), lista_personajes))

print("------------------------------------------")
#C)
mostrar_lista_tupla(mapear_lista(lambda super: (super["nombre"], round(float(super["altura"]), 2)), lista_personajes))

print("------------------------------------------")
#D y E)
super_max_altura = obtener_mayor_menor("altura", lista_personajes, True)
super_min_altura = obtener_mayor_menor("altura", lista_personajes, False)
print(f"Superheroe MAS ALTO: {super_max_altura["nombre"]} con {round(float(super_max_altura['altura']), 2)}")
print(f"Superheroe MAS BAJO: {super_min_altura["nombre"]} con {round(float(super_min_altura['altura']), 2)}")

print("------------------------------------------")
#F)
promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), lista_personajes))
print(f"El PROMEDIO de las alturas es: {promedio}")

print("------------------------------------------")

#G)
print(f"La IDENTIDAD del mas ALTO es: {super_max_altura['identidad']} y el mas BAJO es: {super_min_altura['identidad']}")

print("------------------------------------------")
#H)
super_mas_pesado = obtener_mayor_menor("peso", lista_personajes, True)
super_menos_pesado = obtener_mayor_menor("peso", lista_personajes, False)

print(f"El superheroe MAS PESADO es {super_mas_pesado['nombre']} con {round(float(super_mas_pesado['peso']), 2)} kg y el MAS LIVIANO es {super_menos_pesado['nombre']} con {round(float(super_menos_pesado['peso']), 2)} kg")

print("------------------------------------------")
#J)

def mostrar_menu() -> None:
    print("----- MENU -----")
    print("1. Obtener altura maxima")
    print("2. Obtener altura minima")
    print("3. Obtener altura promedio")
    print("4. Obtener el superheroe mas alto")
    print("5. Obtener el superheroe mas bajo")

    seleccion = input("Elija una OPCION: ")

    while seleccion not in ["1", "2", "3", "4", "5"]:
        print("OPCION INVALIDA")
        seleccion = input("Elija una OPCION: ")

    match seleccion:
        case "1":
            super_max_altura = obtener_mayor_menor("altura", lista_personajes, True)
            respuesta = f"La altura MAS ALTA es: {round(float(super_max_altura['altura']), 2)}"

        case "2":
            super_min_altura = obtener_mayor_menor("altura", lista_personajes, False)
            respuesta = f"La altura MAS BAJA es: {round(float(super_min_altura['altura']), 2)}"

        case "3":
            promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), lista_personajes))
            respuesta = f"El PROMEDIO de las alturas es: {promedio}"

        case "4":
            super_max_altura = obtener_mayor_menor("altura", lista_personajes, True)
            respuesta = f"Superheroe MAS ALTO: {super_max_altura["nombre"]} con {round(float(super_max_altura['altura']), 2)}"

        case "5":
            super_min_altura = obtener_mayor_menor("altura", lista_personajes, False)
            respuesta = f"Superheroe MAS BAJO: {super_min_altura['nombre']} con {round(float(super_min_altura['altura']), 2)}"
    return respuesta    

print(mostrar_menu())