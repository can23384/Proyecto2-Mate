#
#-----------------------------------------------------------
# Funciones.py
#-----------------------------------------------------------
# UNIVERSIDAD DEL VALLE DE GUATEMALA
# FACULTAD DE Ciencias y Humanidades
# DEPARTAMENTO DE Matematica
# MM2015 - MATEMATICA DISCRETA 1
#
# Creadores:
# Eliazar José Pablo Canastuj Matías - 23384
# Diego Alejandro Ramírez Velásquez - 23601
# María José Yee Vidal - 231193
#-----------------------------------------------------------
# Descripción: Funciones interdependientes para el uso del
# sistema RSA.
#-----------------------------------------------------------

import random

# Funcion que genera una lista de numero primos menores que 'n' usando la Criba de Eratóstenes
def criba(n):
    # Conjunto para marcar numero no primos
    notprime = set()
    # Lista para almacenar los numero primos encontrados
    primes = []

    # Iterar desde 2 hasta n-1
    for i in range(2, n):
        # Si el numero ya esta marcado como no primo, saltarlo
        if i in notprime:
            continue

        # Marcar todos los múltiplos de 'i' como no primos
        for j in range(i * 2, n, i):
            notprime.add(j)

        # Agregar 'i' a la lista de primos
        primes.append(i)

    # Retornar la lista de numero primos
    return primes

# Funcion que verifica si un numero es primo usando la lista de primos generada por 'criba'
def prime_test2(n):
    prime_list = criba(int(n**0.5) + 1)

    # Comprobar si 'n' es divisible por algún primo en la lista
    for i in prime_list:
        if n % i == 0:
            return False  # Si es divisible, no es primo
    return True  # Si no es divisible, es primo

# Funcion que genera un numero primo aleatorio dentro de un rango
def generar_primo(rango_inferior, rango_superior):
    # Validar que el rango sea correcto
    if rango_inferior > rango_superior:
        return "Error: El rango inferior no puede ser mayor al rango superior."
    
    # Crear una lista de numero primos dentro del rango utilizando 'prime_test2'
    numeros_primos = [n for n in range(rango_inferior, rango_superior + 1) if prime_test2(n)]

    # Retornar un primo aleatorio si la lista no está vacía
    if numeros_primos:
        return random.choice(numeros_primos)
    else:
        return "No se encontraron numero primos en el rango."

# Funcion que calcula el Máximo Común Divisor (MCD) usando el algoritmo de Euclides
def mcd(a, b):
    while b != 0:  # Repetir mientras el residuo no sea 0
        a, b = b, a % b  # Actualizar 'a' y 'b'
    return abs(a)  # Retornar el MCD en valor absoluto ya que no puede ser negativo

# Funcion que calcula el inverso modular usando el algoritmo extendido de Euclides
def inverso_modular(e, n):
    t, nuevo_t = 0, 1
    r, nuevo_r = n, e

    # Iterar mientras el residuo no sea 0
    while nuevo_r != 0:
        cociente = r // nuevo_r  # Calcular el cociente
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t  
        r, nuevo_r = nuevo_r, r - cociente * nuevo_r  

    # Verificar si no existe un inverso modular
    if r != 1:
        return "Error: No existe un inverso modular."

    # Retornar el inverso modular en positivo
    return t % n

# Funcion que genera un par de claves pública y privada para el algoritmo RSA
def generar_llaves(rango_inferior, rango_superior):
    # Generar dos numero primos aleatorios diferentes
    p = generar_primo(rango_inferior, rango_superior)
    q = generar_primo(rango_inferior, rango_superior)
    while p == q:  # Asegurar que 'p' y 'q' sean distintos
        q = generar_primo(rango_inferior, rango_superior)

    # Calcular 'n' como el producto de los primos y 'phi' como (p-1)*(q-1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Buscar un valor 'e' coprimo con 'phi'
    e = next((x for x in range(2, phi) if mcd(x, phi) == 1), None)
    if e is None:
        return "Error: No se pudo encontrar un 'e' válido."

    # Calcular 'd', el inverso modular de 'e' módulo 'phi'
    d = inverso_modular(e, phi)
    if isinstance(d, str):  # Verificar si ocurrió un error
        return f"Error: {d}"

    # Retornar las claves pública y privada
    return (e, n), (d, n)

# Funcion que encripta un carácter usando la clave pública
def encriptar(caracter, llave_publica):
    e, n = llave_publica  # Desempaquetar la clave pública
    # Validar que el carácter sea menor que 'n'
    if not (0 <= caracter < n):
        return f"Error: El carácter {caracter} debe ser menor que {n}."
    # Calcular el carácter encriptado como (caracter^e) % n
    return pow(caracter, e, n)

# Funcion que desencripta un carácter encriptado usando la clave privada
def desencriptar(caracter_encriptado, llave_privada):
    d, n = llave_privada  # Desempaquetar la clave privada
    # Validar que el carácter encriptado sea menor que 'n'
    if not (0 <= caracter_encriptado < n):
        return f"Error: El carácter encriptado {caracter_encriptado} debe ser menor que {n}."
    # Calcular el carácter original como (caracter_encriptado^d) % n
    return pow(caracter_encriptado, d, n)
