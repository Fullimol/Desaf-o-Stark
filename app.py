from data_stark import lista_personajes
from functions import *

# Desafío #00:

# A. Analizar detenidamente el set de datos
# x B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# x C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# x D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# x E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# x F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
# G. Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores informados.
# J. Construir un menú que permita elegir qué dato obtener


#B)
mostrar_lista_tupla(mapear_lista(lambda super: (super["nombre"]), lista_personajes))

print("------------------------------------------")

#C)
# personajes = mapear_lista(lambda sup: (sup["nombre"], round(float(sup["altura"]), 2)), lista_personajes)
# for personaje in personajes:
#     print(f"NOMBRE: {personaje[0]} - ALTURA: {personaje[1]}")

mostrar_lista_tupla(mapear_lista(lambda super: (super["nombre"], round(float(super["altura"]), 2)), lista_personajes))

print("------------------------------------------")

#D y E)
super_max_altura = superheroe_alturas_limites(lista_personajes, True)
super_min_altura = superheroe_alturas_limites(lista_personajes, False)

print(f"Superheroe MAS ALTO: {super_max_altura[0]} con {super_max_altura[1]}")
print(f"Superheroe MAS BAJO: {super_min_altura[0]} con {super_min_altura[1]}")

print("------------------------------------------")

#F)
promedio = calcular_promedio(mapear_lista(lambda super: (float(super["altura"])), lista_personajes))

print(f"El PROMEDIO de las alturas es: {promedio}")

print("------------------------------------------")

#G)
