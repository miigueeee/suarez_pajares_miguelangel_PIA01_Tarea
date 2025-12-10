# Función que recibe una lista de enteros por parámetro y devuelve una lista de los positivos sin duplicados
def procesar_lista(lista_enteros):
    # 1. Eliminar los números negativos de la lista
    lista_positivos = [num  for num  in lista_enteros if num  >= 0]

    # 2. Eliminar los valores que están repetidos, quedándonos con uno de ellos
    lista_sin_duplicados = list(set(lista_positivos))

    # 3. Ordenar los números resultantes de menor a mayor
    lista_sin_duplicados.sort()

    return lista_sin_duplicados

# Ejemplo de prueba, pasamos [4, -1, 2, 4, 3, -5, 2], debería imprimir [2,3,4]