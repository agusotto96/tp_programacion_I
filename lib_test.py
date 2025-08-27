from lib import es_adn, es_arn, contenido_gc


def test_es_adn_vacio():
    secuencia = ""
    esperado = False
    resultado = es_adn(secuencia)
    if resultado != esperado:
        print(f"test_es_adn_vacio ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_adn_vacio OK")


def test_es_adn_caracter_desconocido():
    secuencia = "ATCXG"
    esperado = False
    resultado = es_adn(secuencia)
    if resultado != esperado:
        print(f"test_es_adn_caracter_desconocido ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_adn_caracter_desconocido OK")


def test_es_adn_subset():
    secuencia = "AT"
    esperado = True
    resultado = es_adn(secuencia)
    if resultado != esperado:
        print(f"test_es_adn_subset ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_adn_subset OK")


def test_es_adn_completo():
    secuencia = "ATCGATCG"
    esperado = True
    resultado = es_adn(secuencia)
    if resultado != esperado:
        print(f"test_es_adn_completo ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_adn_completo OK")


def test_es_arn_vacio():
    secuencia = ""
    esperado = False
    resultado = es_arn(secuencia)
    if resultado != esperado:
        print(f"test_es_arn_vacio ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_arn_vacio OK")


def test_es_arn_caracter_desconocido():
    secuencia = "AUCXG"
    esperado = False
    resultado = es_arn(secuencia)
    if resultado != esperado:
        print(f"test_es_arn_caracter_desconocido ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_arn_caracter_desconocido OK")


def test_es_arn_subset():
    secuencia = "AU"
    esperado = True
    resultado = es_arn(secuencia)
    if resultado != esperado:
        print(f"test_es_arn_subset ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_arn_subset OK")


def test_es_arn_completo():
    secuencia = "AUCGAUCG"
    esperado = True
    resultado = es_arn(secuencia)
    if resultado != esperado:
        print(f"test_es_arn_completo ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print("test_es_arn_completo OK")


def test_contenido_gc_50():
    secuencia = "ATGC"
    esperado = 50.0
    resultado = contenido_gc(secuencia)
    if resultado != esperado:
        print(f"test_contenido_gc_50 ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print(f"test_contenido_gc_50 OK")


def test_contenido_gc_100():
    secuencia = "GC"
    esperado = 100.0
    resultado = contenido_gc(secuencia)
    if resultado != esperado:
        print(f"test_contenido_gc_100 ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print(f"test_contenido_gc_100 OK")


def test_contenido_gc_0():
    secuencia = "AT"
    esperado = 0.0
    resultado = contenido_gc(secuencia)
    if resultado != esperado:
        print(f"test_contenido_gc_0 ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print(f"test_contenido_gc_0 OK")


def test_contenido_gc_con_decimales():
    secuencia = "GAT"
    esperado = 33.33
    resultado = contenido_gc(secuencia)
    if resultado != esperado:
        print(f"test_contenido_gc_con_decimales ERROR: resultado = {resultado}, esperado = {esperado}")
    else:
        print(f"test_contenido_gc_con_decimales OK")


# tests es_adn
test_es_adn_vacio()
test_es_adn_caracter_desconocido()
test_es_adn_subset()
test_es_adn_completo()

# tests es_arn
test_es_arn_vacio()
test_es_arn_caracter_desconocido()
test_es_arn_subset()
test_es_arn_completo()

# tests contenido_gc
test_contenido_gc_50()
test_contenido_gc_100()
test_contenido_gc_0()
test_contenido_gc_con_decimales()
