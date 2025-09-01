from lib import es_adn, es_arn, contenido_gc, es_proteina, adn_random, mutar_adn, distancia_hamming


def test_es_adn():
    casos = [
        ["", False, "vacio"],
        ["AT", True, "subset"],
        ["AXT", False, "caracter_desconocido"],
        ["ATCG", True, "completo"],
    ]
    for caso in casos:
        secuencia, esperado, nombre = caso[0], caso[1], caso[2]
        resultado = es_adn(secuencia)
        if resultado != esperado:
            print(f"test_es_adn_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_es_adn_{nombre} OK")


def test_es_arn():
    casos = [
        ["", False, "vacio"],
        ["AU", True, "subset"],
        ["AXU", False, "caracter_desconocido"],
        ["AUCG", True, "completo"],
    ]
    for caso in casos:
        secuencia, esperado, nombre = caso[0], caso[1], caso[2]
        resultado = es_arn(secuencia)
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
    ]
    for caso in casos:
        secuencia, esperado, nombre = caso[0], caso[1], caso[2]
        resultado = es_proteina(secuencia)
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
    for caso in casos:
        longitud, nombre = caso[0], caso[1]
        secuencia = adn_random(longitud)
        hubo_error = False
        if len(secuencia) != longitud:
            print(f"test_adn_random_{nombre} ERROR: longitud incorrecta, obtenido {len(secuencia)}, esperado {longitud}")
            hubo_error = True
        if not es_adn(secuencia):
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
    for caso in casos:
        sec_original, cant_mutaciones, nombre = caso[0], caso[1], caso[2]
        sec_mutada = mutar_adn(sec_original, cant_mutaciones)
        hubo_error = False
        if len(sec_mutada) != len(sec_original):
            print(f"test_mutar_adn_{nombre} ERROR: longitud incorrecta, obtenido {len(sec_mutada)}, esperado {len(sec_original)}")
            hubo_error = True
        if not es_adn(sec_mutada):
            print(f"test_mutar_adn_{nombre} ERROR: secuencia mutada no es ADN válido: {sec_mutada}")
            hubo_error = True
        dif = distancia_hamming(sec_original, sec_mutada)
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
    for caso in casos:
        secuencia, esperado, nombre = caso[0], caso[1], caso[2]
        resultado = contenido_gc(secuencia)
        if resultado != esperado:
            print(f"test_contenido_gc_{nombre} ERROR: resultado = {resultado}, esperado = {esperado}")
        else:
            print(f"test_contenido_gc_{nombre} OK")


test_es_adn()
test_es_arn()
test_es_proteina()
test_adn_random()
test_mutar_adn()
test_contenido_gc()
