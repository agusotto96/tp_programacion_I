import lib


def ingresar_secuencia():
    while True:
        tipo = input("Ingrese el tipo de secuencia (ADN o ARN): ")
        if tipo in ["ADN", "ARN"]:
            secuencia = input("Ingrese la secuencia (mayúsculas): ")
            return tipo, secuencia
        else:
            print("Tipo inválido. Debe ser 'ADN' o 'ARN'.")


def main():
    while True:
        print("=== BioSeq – Análisis de Secuencias ===")
        print("1. Validar secuencia")
        print("2. Calcular contenido GC")
        print("3. Salir")
        opcion = input("Ingrese una opción (1-3): ")

        if opcion == "1":
            tipo, secuencia = ingresar_secuencia()
            if tipo == "ADN":
                valido = lib.es_adn(secuencia)
            if tipo == "ARN":
                valido = lib.es_arn(secuencia)
            if valido:
                print(f"La secuencia es un {tipo} válido")
            else:
                print(f"La secuencia no es un {tipo} válido")


        elif opcion == "2":
            tipo, secuencia = ingresar_secuencia()
            if tipo == "ADN":
                valido = lib.es_adn(secuencia)
            if tipo == "ARN":
                valido = lib.es_arn(secuencia)
            if not valido:
                print(f"La secuencia no es un {tipo} válido")
                continue

            gc = lib.contenido_gc(secuencia)
            print(f"El contenido de G y C en la secuencia es: {gc}%")

        elif opcion == "3":
            print("Fin del programa")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


main()
