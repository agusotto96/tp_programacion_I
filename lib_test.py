import lib


def test_es_adn():
    casos = [
        ["", False, "vacio"],
        ["AT", True, "subset"],
        ["AXT", False, "caracter_desconocido"],
        ["ATCG", True, "completo"],
        ["atcg", False, "minúscula"],
        ["ATCGATCG", True, "caracteres_duplicados"],
    ]
    for secuencia, esperado, nombre in casos:
        resultado = lib.es_adn(secuencia)
        if resultado != esperado:
            print(f"test_es_adn_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_es_adn_{nombre} OK")


def test_es_arn():
    casos = [
        ["", False, "vacio"],
        ["AU", True, "subset"],
        ["AXU", False, "caracter_desconocido"],
        ["ATCG", False, "es_adn"],
        ["AUCG", True, "completo"],
        ["aucg", False, "minúscula"],
        ["AUCGAUCG", True, "caracteres_duplicados"],
    ]
    for secuencia, esperado, nombre in casos:
        resultado = lib.es_arn(secuencia)
        if resultado != esperado:
            print(f"test_es_arn_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_es_arn_{nombre} OK")


def test_es_proteina():
    casos = [
        ["", False, "vacio"],
        ["KMFP", True, "subset"],
        ["KMXFP", True, "caracter_desconocido"],
        ["ARNDCEQGHILKMFPSTWYV", True, "completo"],
        ["arndceqghilkmfpstwyv", True, "minúscula"],
        ["ARNDCEQGHILKMFPSTWYVARNDCEQGHILKMFPSTWYV", True, "caracteres_duplicados"],
    ]
    for secuencia, esperado, nombre in casos:
        resultado = lib.es_proteina(secuencia)
        if resultado != esperado:
            print(f"test_es_proteina_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_es_proteina_{nombre} OK")


def test_adn_random():
    casos = [
        [10, "longitud_10"],
        [5, "longitud_5"],
        [20, "longitud_20"],
    ]
    for longitud, nombre in casos:
        secuencia = lib.adn_random(longitud)
        hubo_error = False
        if len(secuencia) != longitud:
            print(f"test_adn_random_{nombre} ERROR: longitud incorrecta, obtenido {len(secuencia)}, esperado {longitud}")
            hubo_error = True
        if not lib.es_adn(secuencia):
            print(f"test_adn_random_{nombre} ERROR: secuencia inválida: {secuencia}")
            hubo_error = True
        if not hubo_error:
            print(f"test_adn_random_{nombre} OK")


def test_mutar_adn():
    casos = [
        ["ATCGATCG", 1, "una_mutacion"],
        ["ATCGATCG", 3, "tres_mutaciones"],
        ["GATTACA", 2, "dos_mutaciones"],
        ["CCGGTTAA", 4, "cuatro_mutaciones"],
    ]
    for sec_original, cant_mutaciones, nombre in casos:
        sec_mutada = lib.mutar_adn(sec_original, cant_mutaciones)
        hubo_error = False
        if len(sec_mutada) != len(sec_original):
            print(f"test_mutar_adn_{nombre} ERROR: longitud incorrecta, obtenido {len(sec_mutada)}, esperado {len(sec_original)}")
            hubo_error = True
        if not lib.es_adn(sec_mutada):
            print(f"test_mutar_adn_{nombre} ERROR: secuencia mutada no es ADN válido: {sec_mutada}")
            hubo_error = True
        dif = lib.distancia_hamming(sec_original, sec_mutada)
        if dif != cant_mutaciones:
            print(f"test_mutar_adn_{nombre} ERROR: cantidad de mutaciones incorrecta, obtenido {dif}, esperado {cant_mutaciones}")
            hubo_error = True
        if not hubo_error:
            print(f"test_mutar_adn_{nombre} OK")


def test_contenido_gc():
    casos = [
        ["AT", 0.0, "0"],
        ["ATGC", 50.0, "50"],
        ["GC", 100.0, "100"],
        ["GAT", 33.33, "con_decimales"],
    ]
    for secuencia, esperado, nombre in casos:
        resultado = lib.contenido_gc(secuencia)
        if resultado != esperado:
            print(f"test_contenido_gc_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_contenido_gc_{nombre} OK")


def test_transcripcion():
    casos = [
        ["ATGC", "AUGC", "basico"],
        ["AACG", "AACG", "sin_T"],
        ["TTTT", "UUUU", "solo_T"],
    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.transcripcion(secuencia)
        if obtenido != esperado:
            print(f"test_transcripcion_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_transcripcion_{nombre} OK")


def test_retrotranscripcion():
    casos = [
        ["AUGC", "ATGC", "basico"],
        ["AACG", "AACG", "sin_U"],
        ["UUUU", "TTTT", "solo_U"],
    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.retrotranscripcion(secuencia)
        if obtenido != esperado:
            print(f"test_retrotranscripcion_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_retrotranscripcion_{nombre} OK")


def test_distancia_hamming():
    casos = [
        ["AAAA", "AAAA", 0, "distancia_0"],
        ["AAAA", "AAAT", 1, "distancia_1"],
        ["AAAA", "AATT", 2, "distancia_2"],
    ]
    for a, b, esperado, nombre in casos:
        obtenido = lib.distancia_hamming(a, b)
        if obtenido != esperado:
            print(f"test_distancia_hamming_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_distancia_hamming_{nombre} OK")


def test_buscar_motivo():
    casos = [
        ["ACGTACGT", "ACG", 0, [0, 4], "coincidencias_exactas"],
        ["ACGTACGT", "ACC", 1, [0, 4], "coincidencias_con_una_dif"],
        ["TTGGAATT", "AAA", 2, [2, 3, 4, 5], "coincidencias_con_dos_dif"],
    ]
    for secuencia, motivo, dist_max, esperado, nombre in casos:
        obtenido = lib.buscar_motivo(secuencia, motivo, dist_max)
        if obtenido != esperado:
            print(f"test_buscar_motivo_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_buscar_motivo_{nombre} OK")


def test_homopolimero_mas_largo():
    casos = [
        ["GGGATTCCA", "GGG", "homopolimero_al_inicio"],
        ["ATTGGGCCA", "GGG", "homopolimero_al_medio"],
        ["ATTCCAGGG", "GGG", "homopolimero_al_final"],
        ["ATCG", "A", "sin_homopolimeros_relevantes"],
        ["CCCCCCCC", "CCCCCCCC", "toda_la_secuencia_es_un_homopolimero"],

    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.homopolimero_mas_largo(secuencia)
        if obtenido != esperado:
            print(f"test_homopolimero_mas_largo_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_homopolimero_mas_largo_{nombre} OK")


def test_complemento_reverso():
    casos = [
        ["ATCG", "CGAT", "basico"],
        ["AAAA", "TTTT", "homopolimero"],
        ["AGCT", "AGCT", "palindromo"],
    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.complemento_reverso(secuencia)
        if obtenido != esperado:
            print(f"test_complemento_reverso_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_complemento_reverso_{nombre} OK")


def test_palindromos():
    casos = [
        ["GATATC", ["GATATC", "ATAT"], "palindromo_completo"],
        ["AGAATTCGA", ["GAATTC", "AATT", "TCGA"], "palindromo_embebido"],
        ["ATATATATATAT", ["ATATATATAT", "TATATATATA", "ATATATATAT", "TATATATA", "ATATATAT", "TATATA", "ATATAT", "TATA", "ATAT"], "palindromos_mayores_a_10"],
    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.palindromos(secuencia)
        if obtenido != esperado:
            print(f"test_palindromos_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_palindromos_{nombre} OK")


def test_contar_transiciones_y_transversiones():
    casos = [
        ["ACGT", "ACGT", 0, 0, "sin_cambios"],
        ["ACGT", "GTAC", 4, 0, "solo_transiciones"],
        ["AACCGGTT", "CTAGCTAG", 0, 8, "solo_transversiones"],
        ["ACGTAACCGGTT", "GTACCTAGCTAG", 4, 8, "mas_transversiones"],
        ["ACGTACGTACGTAACCGGTT", "GTACGTACGTACCTAGCTAG", 12, 8, "mas_transiciones"],
        ["ACGTACGTAACCGGTT", "GTACGTACCTAGCTAG", 8, 8, "igual_proporcion"],
    ]
    for a, b, esperado_ti, esperado_tv, nombre in casos:
        ti, tv = lib.contar_transiciones_y_transversiones(a, b)
        if ti != esperado_ti or tv != esperado_tv:
            print(f"test_contar_transiciones_y_transversiones_{nombre} ERROR: obtenido ({ti}, {tv}), esperado ({esperado_ti}, {esperado_tv})")
        else:
            print(f"test_contar_transiciones_y_transversiones_{nombre} OK")


def test_motivo_compartido():
    casos = [
        [["ACGTACGT", "AACCGTATA"], "CGTA", "coincidencia_parcial"],
        [["AAAA", "CCCC", "GGGG", "TTTT"], "", "sin_coincidencia"],
        [["ACGT", "ACGT", "ACGT"], "ACGT", "coincidencia_completa"],
    ]
    for secuencias, esperado, nombre in casos:
        obtenido = lib.motivo_compartido(secuencias)
        if obtenido != esperado:
            print(f"test_motivo_compartido_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_motivo_compartido_{nombre} OK")


def test_marcos_de_lectura():
    casos = [
        ["AUGGCU", ["AUGGCU", "UGGCU", "GGCU"], "basico"],
        ["AGGUGACACCGCAAGCCUUAUAUUAGCA", ["AGGUGACACCGCAAGCCUUAUAUUAGC", "GGUGACACCGCAAGCCUUAUAUUAGCA", "GUGACACCGCAAGCCUUAUAUUAG"], "longitud_no_multiplo_3"],
    ]
    for secuencia, esperado, nombre in casos:
        obtenido = lib.marcos_de_lectura(secuencia)
        if obtenido != esperado:
            print(f"test_marcos_de_lectura_{nombre} ERROR: obtenido {obtenido}, esperado {esperado}")
        else:
            print(f"test_marcos_de_lectura_{nombre} OK")


test_es_adn()
test_es_arn()
test_es_proteina()
test_adn_random()
test_mutar_adn()
test_contenido_gc()
test_transcripcion()
test_retrotranscripcion()
test_distancia_hamming()
test_buscar_motivo()
test_homopolimero_mas_largo()
test_complemento_reverso()
test_palindromos()
test_contar_transiciones_y_transversiones()
test_motivo_compartido()
test_marcos_de_lectura()
