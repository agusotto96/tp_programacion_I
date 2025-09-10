import lib

# Tipos de secuencias
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
        print("3. Calcular transiciones y transversiones")
        print("4. Calcular motivo compartido")
        print("5. Calcular perfil")
        print("6. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            tipo, secuencia = ingresar_secuencia([ADN, ARN])
            print(f"La secuencia ingresada es una secuencia válida de {tipo}.")

        elif opcion == "2":
            tipo, secuencia = ingresar_secuencia([ADN, ARN])
            gc = lib.contenido_gc(secuencia)
            print(f"El contenido de G y C en la secuencia es: {gc}%")

        elif opcion == "3":
            tipo_a, a = ingresar_secuencia([ADN, ARN])
            tipo_b, b = ingresar_secuencia([ADN, ARN])
            if tipo_a != tipo_b:
                print("Error: ambas secuencias deben tener el mismo tipo.")
                break
            transiciones, transversiones = lib.contar_transiciones_y_transversiones(a, b)
            print(f"La cantidad de transiciones y transversiones entre ambas secuencias es de {transiciones} y {transversiones} respectivamente.")

        elif opcion == "4":
            secuencias = []
            n = input("Ingrese la cantidad de secuencias: ")
            if not n.isdigit():
                print("Cantidad invalida.")
                break
            for i in range(int(n)):
                secuencia = input("Ingrese una secuencia: ")
                secuencias.append(secuencia)
            motivo = lib.motivo_compartido(secuencias)
            if motivo == "":
                print("No hay motivo compartido")
            else:
                print(f"El motivo compartido es {motivo}.")

        elif opcion == "5":
            secuencias = []
            n = input("Ingrese la cantidad de secuencias: ")
            if not n.isdigit():
                print("Cantidad invalida.")
                break
            for i in range(int(n)):
                secuencia = input("Ingrese una secuencia: ")
                secuencias.append(secuencia)
            perfil = lib.perfil(secuencias)
            print("Perfil:")
            for fila in perfil:
                print(" ".join(f"{v:2}" for v in fila))

        elif opcion == "6":
            print("Fin del programa")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
