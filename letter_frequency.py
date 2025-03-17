import re
from collections import Counter

def contar_letras_txt(nombre_archivo):
    try:
        # Leer el archivo de texto
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
            
            # Filtrar solo letras A-Z y Ñ en mayúsculas
            texto = texto.upper()
            letras = re.findall(r'[A-ZÑ]', texto)
            
            # Contar ocurrencias de cada letra
            total_letras = len(letras)
            frecuencia = Counter(letras)
            
            # Mostrar resultados
            print("Letra | Cantidad | Frecuencia")
            print("--------------------------------")
            for letra in sorted("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
                cantidad = frecuencia.get(letra, 0)
                porcentaje = (cantidad / total_letras) * 100 if total_letras > 0 else 0
                print(f"{letra} | {cantidad} | {porcentaje:.2f}%")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

# Nombre del archivo de texto
archivo_txt = "afin.txt"
contar_letras_txt(archivo_txt)

