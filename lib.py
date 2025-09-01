def es_adn(secuencia):
    """
    Verifica si la secuencia es un ADN válido.

    Una secuencia de ADN es válida si no está vacía y contiene solo los nucleótidos:
    A (Adenina), T (Timina), C (Citosina) y G (Guanina).
    """
    return len(secuencia) > 0 and all(base in "ATCG" for base in secuencia)


def es_arn(secuencia):
    """
    Verifica si la secuencia es un ARN válido.

    Una secuencia de ARN es válida si no está vacía y contiene solo los nucleótidos:
    A (Adenina), U (Uracilo), C (Citosina) y G (Guanina).
    """
    return len(secuencia) > 0 and all(base in "AUCG" for base in secuencia)


def es_proteina(secuencia):
    """
    Verifica si la secuencia es una proteína válida.

    Una secuencia proteica es válida si no está vacía y esta compuesta solo por alguno de los 20 aminoácidos:
    A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V.
    """
    pass


def adn_random(longitud):
    """
    Genera una secuencia de ADN aleatoria de una longitud dada.

    La secuencia estará compuesta únicamente por los nucleótidos:
    A (Adenina), T (Timina), C (Citosina) y G (Guanina).
    """
    return ""


def mutar_adn(secuencia, cantidad_mutaciones):
    """
    Aplica mutaciones aleatorias sobre una secuencia de ADN dada.

    Cada mutación consiste en reemplazar un nucleótido por otro nucleótido válido de ADN.
    """
    return ""


def contenido_gc(secuencia):
    """Calcula el porcentaje de Guanina (G) y Citosina (C) en una secuencia de ADN o ARN, redondeado a 2 decimales."""
    pass


def transcripcion(secuencia):
    """
    Convierte una secuencia de ADN a ARN.

    Reemplaza cada Timina (T) por Uracilo (U).
    """
    pass


def retrotranscripcion(arn_seq):
    """
    Convierte una secuencia de ARN a ADN.

    Reemplaza cada Uracilo (U) por Timina (T).
    """
    pass


def distancia_hamming(a, b):
    """
    Calcula el número de diferencias entre dos secuencias del mismo largo.
    """
    pass


def buscar_motivo(secuencia, motivo, distancia_hamming_maxima=0):
    """
    Devuelve una lista con las posiciones donde aparece un 'motivo' en 'secuencia',
    permitiendo hasta 'distancia_hamming_maxima' diferencias.

    La distancia de Hamming indica cuántos elementos pueden diferir entre el motivo
    y la subsecuencia correspondiente para considerarla una coincidencia.

    - distancia_hamming_maxima = 0 → coincidencias exactas
    - distancia_hamming_maxima > 0 → coincidencias aproximadas
    """
    pass


def homopolimero_mas_largo(secuencia):
    """
    Devuelve el homopolímero más largo de una secuencia.

    Un homopolímero es una repetición consecutiva de la misma base.
    """
    pass


def complemento_reverso(secuencia):
    """
    Devuelve el complemento reverso de una secuencia de ADN.

    Se obtiene invirtiendo el orden de los nucleótidos y reemplazando cada base por su complemento:

    - A -> T
    - T -> A
    - C -> G
    - G -> C
    """
    pass


def palindromos(secuencia):
    """
    Devuelve las subcadenas palindrómicas de ADN en la secuencia, de longitud entre 4 y 12 nucleótidos.

    Se consideran palíndromos aquellas subcadenas que coinciden con su complemento reverso.
    """
    pass


def proporcion_transiciones_transversiones(a, b):
    """
    Calcula la proporción entre transiciones y transversiones entre dos secuencias de ADN del mismo largo.

    - Purinas: adenina (A) y guanina (G)
    - Pirimidinas: citosina (C) y timina (T)
    - Transición: sustitución entre purinas o entre pirimidinas
    - Transversión: sustitución entre purina y pirimidina
    """
    pass


def motivo_compartido(secuencias):
    """
    Busca el motivo compartido más largo entre todas las secuencias.
    """
    pass


def marcos_de_lectura(secuencia):
    """
    Genera los tres marcos de lectura posibles de una secuencia de ARN.

    Los nucleótidos del ARN se agrupan en tripletes durante la traducción a proteínas,
    y cada triplete se asocia a un aminoácido específico. Cada secuencia de ARN puede
    leerse de tres formas distintas, comenzando desde el primer, segundo o tercer nucleótido.
    Cada una de estas formas constituye un marco de lectura diferente, que puede dar lugar
    a proteínas distintas dependiendo de dónde se inicia la traducción.

    Ejemplo:
        - Secuencia: AUGGCU
        - Marco 1: AUG GCU
        - Marco 2: UGG CU.
        - Marco 3: GGC U..
    """
    pass
