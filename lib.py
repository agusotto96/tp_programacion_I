# Nucleótidos
ADENINA = 'A'
TIMINA = 'T'
CITOSINA = 'C'
GUANINA = 'G'
URACILO = 'U'

# Aminoácidos
ALANINA = 'A'
ARGININA = 'R'
ASPARAGINA = 'N'
ACIDO_ASPARTICO = 'D'
CISTEINA = 'C'
GLUTAMINA = 'Q'
ACIDO_GLUTAMICO = 'E'
GLICINA = 'G'
HISTIDINA = 'H'
ISOLEUCINA = 'I'
LEUCINA = 'L'
LISINA = 'K'
METIONINA = 'M'
FENILALANINA = 'F'
PROLINA = 'P'
SERINA = 'S'
TREONINA = 'T'
TRIPTOFANO = 'W'
TIROSINA = 'Y'
VALINA = 'V'

# Nucleótidos que forman el ADN
NUCLEOTIDOS_ADN = [ADENINA, TIMINA, CITOSINA, GUANINA]

# Nucleótidos que forman el ARN
NUCLEOTIDOS_ARN = [ADENINA, URACILO, CITOSINA, GUANINA]

# Aminoácidos que forman las proteínas
AMINOACIDOS_PROTEINA = [
    ALANINA, ARGININA, ASPARAGINA, ACIDO_ASPARTICO, CISTEINA,
    GLUTAMINA, ACIDO_GLUTAMICO, GLICINA, HISTIDINA, ISOLEUCINA,
    LEUCINA, LISINA, METIONINA, FENILALANINA, PROLINA,
    SERINA, TREONINA, TRIPTOFANO, TIROSINA, VALINA
]


def es_adn(secuencia):
    """
    Verifica si la secuencia es un ADN válido. Una secuencia es un ADN válido cuando no está vacía
    y solo contiene los nucleótidos A (Adenina), T (Timina), C (Citosina) y G (Guanina).

    Parámetros:
        - secuencia (str): Cadena que representa la secuencia de ADN a validar.

    Retorna:
        - bool: True si la secuencia es válida; False en caso contrario.
    """
    return len(secuencia) != 0 and all(nucleotido in NUCLEOTIDOS_ADN for nucleotido in secuencia)


def es_arn(secuencia):
    """
    Verifica si la secuencia es un ARN válido. Una secuencia es un ARN válido cuando no está vacía
    y solo contiene los nucleótidos A (Adenina), U (Uracilo), C (Citosina) y G (Guanina).

    Parámetros:
        - secuencia (str): Cadena que representa la secuencia de ARN a validar.

    Retorna:
        - bool: True si la secuencia es válida; False en caso contrario.
    """
    for i in secuencia:
        if i == ADENINA:
            continue
        elif i == URACILO:
            continue
        elif i == CITOSINA:
            continue
        elif i == GUANINA:
            continue
        else:
            return False

    if len(secuencia) >= 1:
        return True
    else:
        return False


def es_proteina(secuencia):
    """
    Verifica si la secuencia es una proteína válida. Una secuencia es una proteína válida cuando no está vacía
    y solo contiene símbolos de los 20 aminoácidos estándar: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V.

    Parámetros:
        - secuencia (str): Cadena que representa la secuencia proteica a validar.

    Retorna:
        - bool: True si la secuencia es válida; False en caso contrario.
    """
    pass


def adn_random(longitud):
    """
    Genera una secuencia válida de ADN aleatoria con la longitud indicada.

    Parámetros:
        - longitud (int): Cantidad de nucleótidos que debe tener la secuencia generada.

    Retorna:
        - str: Secuencia de ADN aleatoria de la longitud solicitada.
    """
    return ""


def mutar_adn(secuencia, cantidad_mutaciones):
    """
    Aplica mutaciones aleatorias sobre una secuencia de ADN dada.
    Cada mutación consiste en reemplazar un nucleótido por otro nucleótido válido del ADN.

    Parámetros:
        - secuencia (str): Secuencia de ADN original.
        - cantidad_mutaciones (int): Número de mutaciones a aplicar.

    Retorna:
        - str: Nueva secuencia de ADN, de la misma longitud, con la cantidad especificada de nucleótidos reemplazados por otros válidos.
    """
    return ""


def contenido_gc(secuencia):
    """
    Calcula el porcentaje de Guanina (G) y Citosina (C) en una secuencia.

    Parámetros:
        - secuencia (str): Cadena de ADN o ARN.

    Retorna:
        - float: Porcentaje de bases G o C sobre el total, redondeado a 2 decimales.
    """
    gc = sum(1 for c in secuencia if c in [GUANINA, CITOSINA])
    porcentaje = (gc / len(secuencia)) * 100
    return round(porcentaje, 2)


def transcripcion(secuencia):
    """
    Convierte una secuencia de ADN a ARN.

    Parámetros:
        - secuencia (str): Secuencia de ADN.

    Retorna:
        - str: Secuencia de ARN, donde cada Timina (T) del ADN fue reemplazada por Uracilo (U).
    """
    pass


def retrotranscripcion(secuencia):
    """
    Convierte una secuencia de ARN a ADN.

    Parámetros:
        - secuencia (str): Secuencia de ARN.

    Retorna:
        - str: Secuencia de ADN, donde cada Uracilo (U) del ARN fue reemplazado por Timina (T).
    """
    pass


def distancia_hamming(a, b):
    """
    Calcula el número de diferencias entre dos secuencias del mismo largo.

    Parámetros:
        - a (str): Primera secuencia.
        - b (str): Segunda secuencia, de la misma longitud que 'a'.

    Retorna:
        - int: Cantidad de posiciones donde las secuencias difieren.
    """
    pass


def buscar_motivo(secuencia, motivo, distancia_hamming_maxima=0):
    """
    Busca las posiciones donde aparece un motivo en una secuencia.

    Parámetros:
        - secuencia (str): Secuencia principal donde se busca.
        - motivo (str): Subcadena que se desea encontrar.
        - distancia_hamming_maxima (int): Número máximo de diferencias permitidas.

    Retorna:
        - list: Lista de índices (int) donde comienza cada coincidencia que cumple con la distancia de Hamming máxima permitida.
    """
    pass


def homopolimero_mas_largo(secuencia):
    """
    Encuentra el homopolímero más largo dentro de una secuencia.

    Parámetros:
        - secuencia (str): Secuencia de ADN o ARN.

    Retorna:
        - str: Subcadena más larga compuesta por repeticiones consecutivas del mismo nucleótido.
    """
    pass


def complemento_reverso(secuencia):
    """
    Devuelve el complemento reverso de una secuencia de ADN.

    Para ello, se invierte el orden de la secuencia y se reemplaza cada nucleótido por su complemento:
        - A -> T
        - T -> A
        - C -> G
        - G -> C

    Parámetros:
        - secuencia (str): Secuencia de ADN.

    Retorna:
        - str: Secuencia de ADN resultante al invertir el orden de los nucleótidos y reemplazar cada uno por su complemento correspondiente.
    """
    pass


def palindromos(secuencia):
    """
    Busca subcadenas palindrómicas de ADN en la secuencia.

    Una secuencia de ADN es palindrómica cuando coincide con su complemento reverso.

    Esta función identifica todas las subcadenas de longitud entre 4 y 10 nucleótidos
    que cumplen esa condición.

    Parámetros:
        - secuencia (str): Secuencia de ADN.

    Retorna:
        - list: Lista de subcadenas (str) palindrómicas, es decir, que coinciden con su complemento reverso.
    """
    pass


def contar_transiciones_y_transversiones(a, b):
    """
    Cuenta cuántas transiciones y transversiones hay entre dos secuencias de ADN
    del mismo largo.

    Definiciones:
        - Purinas: adenina (A) y guanina (G)
        - Pirimidinas: citosina (C) y timina (T)
        - Transición: sustitución entre purinas o entre pirimidinas
        - Transversión: sustitución entre una purina y una pirimidina

    Parámetros:
        - a (str): Primera secuencia de ADN.
        - b (str): Segunda secuencia de ADN, de la misma longitud que 'a'.

    Retorna:
        - int, int: Cantidades de transiciones y transversiones, en ese orden.
    """
    es_purina = lambda n: n in (ADENINA, GUANINA)
    es_pirimidina = lambda n: n in (CITOSINA, TIMINA)
    transiciones = 0
    transversiones = 0
    for n1, n2 in zip(a, b):
        if n1 == n2:
            continue
        elif (es_purina(n1) and es_purina(n2)) or (es_pirimidina(n1) and es_pirimidina(n2)):
            transiciones += 1
        else:
            transversiones += 1
    return transiciones, transversiones


def motivo_compartido(secuencias):
    """
    Busca el motivo compartido más largo entre todas las secuencias de ADN dadas.

    Un motivo es una subcadena continua que aparece en múltiples secuencias.
    Esta función analiza todas las secuencias recibidas y determina la subcadena
    más larga que está presente en todas ellas.

    Parámetros:
        - secuencias (list): Lista de secuencias de ADN (str).

    Retorna:
        - str: Motivo más largo que aparece en todas las secuencias. Devuelve una cadena vacía si no existe ningún motivo compartido.
    """
    assert len(secuencias) != 0
    # Selecciono la secuencia más corta, porque ningún motivo puede ser más largo
    motivo_max = min(secuencias, key=len)
    largo_max = len(motivo_max)

    # Recorro posibles largos de motivo, desde el máximo hacia el mínimo
    for largo in range(largo_max, 0, -1):

        # Calculo el mayor índice de inicio posible para este largo
        # Ejemplo: si largo == largo_max, solo puedo empezar en 0
        mayor_inicio = largo_max - largo

        # Recorro todos los inicios posibles y genero el motivo candidato
        for inicio in range(0, mayor_inicio + 1):
            motivo = motivo_max[inicio:inicio + largo]

            # Verifico si el motivo está presente en todas las secuencias
            # Si lo está, es el motivo común más largo posible
            if all(motivo in secuencia for secuencia in secuencias):
                return motivo

    # Si no se encontró ningún motivo común, devuelvo cadena vacía
    return ""


def marcos_de_lectura(secuencia):
    """
    Genera hasta tres marcos de lectura posibles de una secuencia de ARN.

    Un marco de lectura es la forma en que se agrupan los nucleótidos de una secuencia
    para leerlos en tripletes (codones). Dependiendo del punto de inicio, una misma
    cadena puede leerse de tres maneras diferentes: comenzando desde el primer, el
    segundo o el tercer nucleótido.

    Esta función devuelve las subsecuencias que representan cada marco de lectura
    posible. Si la secuencia es demasiado corta, puede haber menos de tres marcos.

    Parámetros:
        - secuencia (str): Secuencia de ARN.

    Retorna:
        - list: Lista con hasta tres secuencias (str), cada una representando un marco de lectura que comienza en los índices 0, 1 y 2 respectivamente.

    Ejemplo:
        - Secuencia: AUGGCU
        - Marco 1: AUG GCU
        - Marco 2: UGG CU
        - Marco 3: GGC U
    """
    pass


def perfil(secuencias):
    """
    Calcula el perfil de un conjunto de secuencias de ADN de igual longitud.

    El perfil es una tabla 4×n donde n es la longitud de las secuencias:
        - La fila 0 cuenta las A (Adenina) en cada posición.
        - La fila 1 cuenta las C (Citosina) en cada posición.
        - La fila 2 cuenta las G (Guanina) en cada posición.
        - La fila 3 cuenta las T (Timina) en cada posición.

    Cada columna representa una posición en las secuencias y cada valor indica
    cuántas veces aparece ese nucleótido en esa posición en todas las secuencias.

    Esta función es útil para:
        - Analizar conservación de nucleótidos.
        - Detectar posiciones altamente variables.
        - Preparar datos para generar la secuencia consenso.
    """
    assert len(secuencias) != 0
    len_secuencias = len(secuencias[0])
    perfil = [
        [0] * len_secuencias,  # A
        [0] * len_secuencias,  # C
        [0] * len_secuencias,  # G
        [0] * len_secuencias,  # T
    ]
    for i in range(len_secuencias):  # columnas
        for j in range(len(secuencias)):  # filas
            nucleotido = secuencias[j][i]
            if nucleotido == ADENINA:
                perfil[0][i] += 1
            elif nucleotido == CITOSINA:
                perfil[1][i] += 1
            elif nucleotido == GUANINA:
                perfil[2][i] += 1
            elif nucleotido == TIMINA:
                perfil[3][i] += 1
    return perfil
