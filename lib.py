def es_adn(secuencia):
    """
    Devuelve True si la secuencia es ADN válido (no vacía, solo A, T, C, G), False si no.
    """
    return len(secuencia) > 0 and all(base in "ATCG" for base in secuencia)


def es_arn(secuencia):
    """
    Devuelve True si la secuencia es ARN válido (no vacía, solo A, U, C, G), False si no.
    """
    return len(secuencia) > 0 and all(base in "AUCG" for base in secuencia)


def contenido_gc(secuencia):
    """Calcula el porcentaje de G y C en una secuencia de ADN o ARN, redondeado a 2 decimales."""
    porcentaje = sum(1 for base in secuencia if base in "GC") / len(secuencia) * 100
    return round(porcentaje, 2)
