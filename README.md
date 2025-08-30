# BioSeq – Análisis de Secuencias Biológicas

**Tema:** Desarrollo de una herramienta para realizar análisis básicos de secuencias de ADN, ARN y proteínas

**Integrantes:** Ottolini Agustin, Ancalay Enzo Jose Tomas, Barreto Sofia, Salvucci Ramiro, Bahit Lopez Lisandro, Mazzoni Teo Geronimo

## Introducción

La bioinformática es una disciplina que combina biología, informática y matemáticas para estudiar y comprender información biológica mediante herramientas computacionales. Entre sus tareas más frecuentes se encuentra el análisis de **secuencias biológicas**, que representan la información fundamental de los organismos vivos. Estas secuencias pueden ser de diferentes tipos:

- **ADN (ácido desoxirribonucleico):** molécula que contiene la información genética de los seres vivos y determina características hereditarias.
- **ARN (ácido ribonucleico):** molécula relacionada con el ADN que cumple un papel central en la síntesis de proteínas y en la regulación genética.
- **Proteínas:** macromoléculas formadas por aminoácidos que cumplen funciones estructurales, enzimáticas o de señalización dentro de la célula.

Estas secuencias se representan mediante **cadenas de caracteres**, donde cada letra corresponde a una base (para ADN/ARN) o un aminoácido (para proteínas). Por ejemplo:

- Secuencia ADN: `ATGCGTAC`
- Secuencia ARN: `AUGCGUAC`
- Secuencia proteica: `MRTLQ`

Analizar estas secuencias permite responder preguntas esenciales de la biología y la medicina: identificar genes específicos, detectar mutaciones que puedan provocar enfermedades, comparar especies para estudiar evolución o entender la función de proteínas críticas en procesos celulares. La bioinformática facilita este análisis al automatizar operaciones que de otro modo serían tediosas y propensas a errores humanos.

Algunos ejemplos de operaciones que la herramienta realizará incluyen:

- **Contenido de GC:**

  ```text
  Entrada -> ATGCGTAC
  Salida  -> 50%
  ```

- **Transcripción:**
  ```text
  Entrada -> ATGCGTAC
  Salida  -> AUGCGUAC
  ```
- **Búsqueda de motivos:**
  ```text
  Entrada -> ATGCGTAC, CG
  Salida  -> 3, 5
  ```
- **Homopolímero más largo:**
  ```text
  Entrada -> ATGGGCT
  Salida  -> GGG
  ```
  
- **Complemento reverso:**
  ```text
  Entrada -> AAAACCCGGT
  Salida  -> ACCGGGTTTT
  ```

## Planteo del problema

El proyecto surge de la necesidad de contar con una aplicación accesible que permita realizar análisis básicos de secuencias biológicas, sin depender de herramientas complejas o sistemas especializados. La aplicación se enfocará en tareas comunes y fundamentales para el estudio de secuencias, por ejemplo:

- Cálculo de estadísticas simples sobre la secuencia: longitud total, frecuencia de cada base o aminoácido, porcentaje de GC en ADN/ARN.
- Obtención de secuencias complementarias o reversas en ADN/ARN.
- Traducción de secuencias de ADN a proteínas según el código genético estándar.
- Comparaciones básicas entre secuencias para identificar regiones de coincidencia o divergencia, permitiendo al usuario observar de manera inmediata qué posiciones difieren entre dos genes o proteínas.

Los resultados esperados se organizarán en tres tipos de reportes:

1. **Métricas descriptivas:** longitud de la secuencia, porcentaje de cada nucleótido o aminoácido, presencia de homopolímeros y motivos específicos.
2. **Secuencias transformadas:** secuencias complementarias, reversas o traducidas a proteína, listas para análisis posteriores.
3. **Comparaciones entre secuencias:** identificación de coincidencias, diferencias y distancias entre motifs.

## Alcance

El proyecto se centrará en funcionalidades básicas de análisis de secuencias, por lo que **no incluirá**:

- Algoritmos avanzados de alineamiento de secuencias o predicción estructural.
- Manejo de secuencias extremadamente largas.
- Procesamiento concurrente o distribuido.
- Integración con sistemas externos, bases de datos o servicios web.

El objetivo es crear una herramienta sencilla, que permita realizar operaciones rápidas y confiables sobre secuencias biológicas de tamaño moderado, manteniendo claridad y accesibilidad para el usuario.

## Roadmap

La versión inicial (V1) se centrará en:

- Funcionalidades básicas de análisis de secuencias.
- Uso exclusivo de listas y matrices, sin estructuras complejas.
- Generación de reportes y secuencias transformadas de forma directa en consola.

En una versión futura (V2) se prevé:

- Implementar funciones más avanzadas que aprovechen diccionarios y estructuras complejas para perfiles de secuencias, secuencia consenso, motifs compartidos y cálculos de transición/transversión.
- Incorporar manejo de archivos, permitiendo al usuario guardar y cargar secuencias y reportes de manera persistente.

## Estructura de la aplicación

La aplicación se dividirá en tres módulos principales:

1. **Módulo de funciones:** Contendrá todas las funciones de análisis de secuencias, organizadas de manera modular y reusable, facilitando su extensión en futuras versiones.
2. **Módulo de pruebas:** Incluirá funciones que simulen diferentes escenarios de uso, permitiendo al desarrollador verificar que cada funcionalidad produzca resultados correctos y consistentes.
3. **Módulo principal (CLI):** Interfaz de usuario que permitirá cargar secuencias, ejecutar análisis y visualizar resultados, sirviendo como punto de entrada al programa y facilitando la interacción directa con los datos.

## Referencias útiles

- [What is Bioinformatics?](https://www.youtube.com/watch?v=W-Ov2cUaYQY)  
  Video introductorio sobre bioinformática.
- [Bioinformatics in Python](https://www.youtube.com/playlist?list=PLpSOMAcxEB_jUKMvdl8rHqNiZXFIrtd5G)  
  Playlist de tutoriales sobre bioinformática en Python.
- [Bioinformatics Algorithms: An Active Learning Approach](https://cogniterra.org/course/64/promo)  
  Curso interactivo sobre algoritmos de bioinformática.
- [Bioinformatic Algorithms](https://www.cl.cam.ac.uk/~pl219/Bioinformatics2015.pdf)  
  Presentación sobre algoritmos de bioinformática.
- [Rosalind platform for learning bioinformatics](https://rosalind.info/problems/locations/)  
  Plataforma educativa con problemas prácticos de bioinformática.
