# Función que recibe dos listas de enteros y devuelve un diccionario con la siguiente información 
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto, pero no en ambos).

def operaciones_conjuntos(lista1, lista2):
    # Convertir listas a conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Devolver diccionario diccionario con las operaciones de conjuntos
    diccionario = {
        # 1. La intersección de ambos conjuntos (elementos comunes).
        "Intersección": conjunto1 & conjunto2,

        # 2. La unión de ambos conjuntos (todos los elementos sin duplicados)
        "Unión": conjunto1 | conjunto2,
        
        # 3. La diferencia simétrica
        "Diferencia simétrica": conjunto1 ^ conjunto2
    }

    return diccionario

# Ejemplo de prueba
print(operaciones_conjuntos([1,2,3], [3,4,5]))