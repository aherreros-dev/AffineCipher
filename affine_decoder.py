"""
Decodificador de Cifrado Afín
Fórmula: Mi = a^(-1) (Ci + n - b) mod n
Donde:
- Mi es el caracter descifrado en texto en plano
- a^(-1) es el inverso multiplicativo modular de a
- Ci es el caracter cifrado
- n es el número de caracteres del alfabeto (26 o 27)
- a es la constante de decimación
- b es la constante de desplazamiento
"""

def calcular_inverso_modular(a, n):
    """
    Calcula el inverso multiplicativo modular de a mod n
    Utiliza el algoritmo extendido de Euclides
    """
    def extendido_euclides(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extendido_euclides(b % a, a)
            return gcd, y - (b // a) * x, x
    
    # Verificar si a y n son coprimos
    gcd, x, _ = extendido_euclides(a, n)
    if gcd != 1:
        raise ValueError(f"El inverso modular no existe porque {a} y {n} no son coprimos")
    
    return x % n

def obtener_valor_numerico(caracter, n):
    """
    Convierte un caracter a su valor numérico según su posición en el alfabeto
    A=0, B=1, ..., Z=25, Ñ=14 (si n=27)
    """
    caracter = caracter.upper()
    
    # Alfabeto español (con Ñ)
    if n == 27:
        alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        if caracter in alfabeto:
            return alfabeto.index(caracter)
        else:
            return None
    # Alfabeto inglés (sin Ñ)
    elif n == 26:
        if 'A' <= caracter <= 'Z':
            return ord(caracter) - ord('A')
        else:
            return None
    else:
        raise ValueError("El valor de n debe ser 26 o 27")

def obtener_caracter(valor_numerico, n):
    """
    Convierte un valor numérico a su caracter correspondiente
    0=A, 1=B, ..., 25=Z, 14=Ñ (si n=27)
    """
    # Alfabeto español (con Ñ)
    if n == 27:
        alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        return alfabeto[valor_numerico % n]
    # Alfabeto inglés (sin Ñ)
    elif n == 26:
        return chr((valor_numerico % n) + ord('A'))
    else:
        raise ValueError("El valor de n debe ser 26 o 27")

def decodificar_afin(caracter_cifrado, a_inv, b, n):
    """
    Decodifica un caracter usando el cifrado afín
    Mi = a^(-1) (Ci + n - b) mod n
    """
    # Obtener el valor numérico del caracter
    ci = obtener_valor_numerico(caracter_cifrado, n)
    
    # Si el caracter no está en el alfabeto, devolver None
    if ci is None:
        return None
    
    # Aplicar la fórmula de decodificación
    mi = (a_inv * (ci + n - b)) % n
    
    # Convertir el valor numérico de vuelta a caracter
    return obtener_caracter(mi, n)

def main():
    # Pedir los parámetros por teclado
    try:
        a = int(input("Introduce el valor de a (constante de decimación): "))
        b = int(input("Introduce el valor de b (constante de desplazamiento): "))
        
        # Verificar que n sea 26 o 27
        n = int(input("Introduce el valor de n (tamaño del alfabeto, 26 o 27): "))
        if n not in [26, 27]:
            print("Error: n solo puede ser 26 o 27")
            return
        
        # Calcular el inverso multiplicativo modular de a
        try:
            a_inv = calcular_inverso_modular(a, n)
            print(f"El inverso multiplicativo modular de {a} mod {n} es: {a_inv}")
        except ValueError as e:
            print(e)
            return
        
        # Pedir el nombre del archivo que contiene el mensaje cifrado
        nombre_archivo = input("Introduce el nombre del archivo que contiene el mensaje cifrado: ")
        
        try:
            # Abrir y leer el archivo
            with open(nombre_archivo, 'r') as archivo:
                texto_cifrado = archivo.read()
            
            # Decodificar el mensaje
            texto_decodificado = ""
            for caracter in texto_cifrado:
                resultado = decodificar_afin(caracter, a_inv, b, n)
                if resultado is not None:
                    texto_decodificado += resultado
                else:
                    # Si el caracter no está en el alfabeto, lo omitimos
                    continue
            
            # Mostrar el resultado
            print("\nTexto decodificado:")
            print(texto_decodificado)
            
            # Opcional: guardar el resultado en un nuevo archivo
            guardar = input("\n¿Deseas guardar el texto decodificado en un archivo? (s/n): ")
            if guardar.lower() == 's':
                nombre_salida = input("Introduce el nombre del archivo de salida: ")
                with open(nombre_salida, 'w') as archivo_salida:
                    archivo_salida.write(texto_decodificado)
                print(f"Texto decodificado guardado en {nombre_salida}")
        
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {nombre_archivo}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    except ValueError:
        print("Error: Debes introducir valores numéricos para a, b y n")

if __name__ == "__main__":
    main()
