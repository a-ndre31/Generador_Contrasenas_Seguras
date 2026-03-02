import random
import string
import math


# CONTRASEÑA ALTA SEGURIDAD


def generar_contrasena():
    longitud = random.randint (16, 64)
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*-_/"
    return ''.join(random.choice(caracteres) for _ in range(longitud))


# CONTRASEÑA MEMORABLE (ABUELITOS)


def generar_contrasena_memorable():
    palabras1 = [
        "Sol", "Luna", "Casa", "Perro", "Gato",
        "Rio", "Pan", "Flor", "Cielo", "Mar",
        "Nube", "Campo", "Bosque", "Mesa", "Libro",
        "Caleta", "Soplado", "Pelada", "Nena", "Libro",
         "Futbol", "Salida"
    ]
    palabras2 = [
        "Montaña", "Estrella", "Lago", "Árbol", "Viento",
        "Arena", "Fuego", "Risa", "Sombras", "Camino",
        "Trueno", "Selva", "Piedra", "Puente", "Escuela",
        "Isla", "Brisa", "Clara", "Niño", "Cuaderno",
         "Música", "Viaje"
    ]
    caracteres = [
        "!", "@", "#", "$", "%", "&", "*", "?"
        ]

    palabra1 = random.choice(palabras1)
    palabra2 = random.choice(palabras2)
    numero = random.randint(10, 99)
    caracteres = random.choice(caracteres)

    return f"{palabra1}-{palabra2}-{numero}-{caracteres}"



# CÁLCULO DE ENTROPÍA


def calcular_entropia(contrasena):
    conjunto = len(set(contrasena))
    if conjunto == 0:
        return 0
    return round(len(contrasena) * math.log2(conjunto), 2)



# EVALUAR FORTALEZA


def evaluar_fortaleza(contrasena):
    entropia = calcular_entropia(contrasena)

    if entropia < 20:
        return "Débil"
    elif entropia < 40:
        return "Media"
    elif entropia < 60:
        return "Fuerte"
    else:
        return "Muy Fuerte"
    