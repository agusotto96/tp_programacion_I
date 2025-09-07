import lib

ADN = "ADN"
ARN = "ARN"
PROTEINA = "PROTEINA"


def ingresar_secuencia(tipos):
    while True:
        print("Tipos disponibles:", ", ".join(tipos))
        tipo = input("Ingrese el tipo de secuencia: ")

        if tipo not in tipos:
            print("Tipo inválido. Intente nuevamente.")
            continue

        secuencia = input("Ingrese la secuencia: ")
        if tipo == ADN:
            valido = lib.es_adn(secuencia)
        elif tipo == ARN:
            valido = lib.es_arn(secuencia)
        elif tipo == PROTEINA:
            valido = lib.es_proteina(secuencia)
        else:
            valido = False

        if valido:
            return tipo, secuencia
        else:
            print(f"La secuencia ingresada no es una secuencia válida de {tipo}. Intente nuevamente.")


def main():
    while True:
        print("=== BioSeq – Análisis de Secuencias ===")
        print("1. Validar secuencia")
        print("2. Calcular contenido GC")
        print("3. Salir")
        opcion = input("Ingrese una opción (1-3): ")

        if opcion == "1":
            tipo, secuencia = ingresar_secuencia([ADN, ARN, PROTEINA])
            print(f"La secuencia ingresada es una secuencia válida de {tipo}.")

        elif opcion == "2":
            tipo, secuencia = ingresar_secuencia([ADN, ARN])
            gc = lib.contenido_gc(secuencia)
            print(f"El contenido de G y C en la secuencia es: {gc}%")

        elif opcion == "3":
            print("Fin del programa")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


main()
