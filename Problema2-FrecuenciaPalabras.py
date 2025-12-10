import string

# Función que recibe por parámetro una lista de palabras y la ruta a un fichero de texto
# Devuelve un diccionario que muestra cuantas veces aparecen las distintas palabras de la lista en el fichero de texto
def frecuencia_palabras(lista_palabras, ruta_fichero):

    # Leer el contenido del archivo de entrada.
    with open(ruta_fichero, "r", encoding="utf-8") as archivo:
        contenido_archivo = archivo.read()
    
    # 1. Eliminar signos de puntuación y convertir todo a minúsculas
    texto_minusculas = contenido_archivo.lower()
    for signo in string.punctuation:
        texto_minusculas_sin_signos = texto_minusculas.replace(signo,"")

    # Dividir en palabras
    texto_en_palabras = texto_minusculas_sin_signos.split()

    # 2. Usar un diccionario donde la clave sea la palabra y el valor su frecuencia
    # Inicializar diccionario 
    frecuencias = {} 
    lista = [p.lower() for p in lista_palabras]

    # Contar frecuencia
    for palabra in lista:
        frecuencias[palabra] = texto_en_palabras.count(palabra)

    # 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra
    return dict(sorted(frecuencias.items()))


# Prueba del programa

palabras = ["inteligencia", "artificial", "python"] # Lista de palabras a buscar
ruta = "texto.txt" # Ruta al archivo de texto (ubicado en la misma carpeta)

# Debería imprimir {'artificial': 0, 'inteligencia': 1, 'python': 3}
print(frecuencia_palabras(palabras, ruta))