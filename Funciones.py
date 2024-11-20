import random

def criba(n):
    """Genera una lista de números primos menores que n usando la Criba de Eratóstenes."""
    notprime = set()
    primes = []

    for i in range(2, n):
        if i in notprime:
            continue

        for j in range(i * 2, n, i):
            notprime.add(j)

        primes.append(i)

    return primes

def prime_test2(n):
    """Prueba de primalidad utilizando una lista de primos generados por criba."""
    prime_list = criba(int(n**0.5) + 1)

    for i in prime_list:
        if n % i == 0:
            return False
    return True

def generar_primo(rango_inferior, rango_superior):
    """
    Genera un número primo aleatorio dentro de un rango especificado.
    
    Entrada:
    - rango_inferior (int): Límite inferior del rango.
    - rango_superior (int): Límite superior del rango.
    
    Salida:
    - (int): Un número primo aleatorio dentro del rango, o None si no hay números primos.
    """
    # Validación de los límites del rango
    if rango_inferior > rango_superior:
        return "Error: El rango inferior no puede ser mayor al rango superior."
    
    # Generar lista de números primos dentro del rango utilizando prime_test2
    numeros_primos = []
    for n in range(rango_inferior, rango_superior + 1):
        if prime_test2(n):
            numeros_primos.append(n)
    
    # Devolver un primo aleatorio si existen
    if numeros_primos:
        return random.choice(numeros_primos)
    else:
        return "No se encontraron números primos en el rango."

# Ejemplo de uso
rango_inferior = 10
rango_superior = 50
primo_aleatorio = generar_primo(rango_inferior, rango_superior)
#print(f"Número primo generado: {primo_aleatorio}")



def mcd(a, b):
    """
    Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    
    Entrada:
    - a (int): Primer número entero.
    - b (int): Segundo número entero.
    
    Salida:
    - (int): El MCD de a y b.
    """
    while b != 0:
        r = a % b
        a = b
        b = r
    return abs(a)  # Devolver el valor positivo del MCD

# Ejemplos de uso
print(mcd(54, 24))  # Salida esperada: 6
print(mcd(17, 31))  # Salida esperada: 1
print(mcd(0, 25))   # Salida esperada: 25
print(mcd(0, 0))    # Salida esperada: 0

def inverso_modular(e, n):
    """
    Calcula el inverso modular de e módulo n utilizando el algoritmo extendido de Euclides.
    
    Entrada:
    - e (int): Número entero que se desea invertir en el contexto de módulo.
    - n (int): Módulo de la operación.
    
    Salida:
    - (int): El inverso modular de e módulo n, o None si no existe.
    """
    # Algoritmo extendido de Euclides
    t, nuevo_t = 0, 1
    r, nuevo_r = n, e

    while nuevo_r != 0:
        cociente = r // nuevo_r
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t
        r, nuevo_r = nuevo_r, r - cociente * nuevo_r

    # Si el máximo común divisor no es 1, no existe inverso modular
    if r != 1:
        return "error: No existe un inverso modular."

    # Asegurarse de que el resultado sea positivo
    return t % n

# Ejemplos de uso
print(inverso_modular(3, 7))  # Salida esperada: 4
print(inverso_modular(7, 40))  # Salida esperada: 23
print(inverso_modular(10, 20)) # Salida esperada: None (no tiene inverso modular)


def generar_llaves(rango_inferior, rango_superior):
    """
    Genera un par de llaves pública y privada para el algoritmo RSA.
    
    Entrada:
    - rango_inferior (int): Límite inferior del rango de búsqueda de números primos.
    - rango_superior (int): Límite superior del rango de búsqueda de números primos.
    
    Salida:
    - (tuple): Dos tuplas, donde la primera representa la clave pública (e, n)
      y la segunda representa la clave privada (d, n).
    """
    # Generar dos números primos distintos p y q
    p = generar_primo(rango_inferior, rango_superior)
    q = generar_primo(rango_inferior, rango_superior)
    
    while p == q:  # Asegurar que los primos sean distintos
        q = generar_primo(rango_inferior, rango_superior)
    
    # Calcular n = p * q y phi = (p-1) * (q-1)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Elegir e, tal que 1 < e < phi y e sea coprimo con phi
    e = None
    for candidate in range(2, phi):
        if mcd(candidate, phi) == 1:  # Usar la función MCD para verificar coprimalidad
            e = candidate
            break
    
    if e is None:
        return "Error: No se pudo encontrar un 'e' válido en el rango dado."
    
    # Calcular d, el inverso modular de e módulo phi
    d = inverso_modular(e, phi)
    
    if d is None or d == e:  # Asegurar que d y e sean distintos
        return "Error: No se pudo calcular una clave privada válida."
    
    # Devolver las llaves pública y privada
    clave_publica = (e, n)
    clave_privada = (d, n)
    return clave_publica, clave_privada

# Ejemplo de uso
rango_inferior = 53
rango_superior = 61

llaves = generar_llaves(rango_inferior, rango_superior)
if llaves:
    clave_publica, clave_privada = llaves
    print(f"Clave pública: {clave_publica}")
    print(f"Clave privada: {clave_privada}")
else:
    print("No se pudieron generar las llaves.")


def encriptar(caracter, llave_publica):
    """
    Encripta un carácter usando la llave pública de RSA.
    
    Entrada:
    - caracter (int): El carácter a encriptar, representado como un número M < n.
    - llave_publica (tuple): La llave pública (e, n).s
    
    Salida:
    - (int): El carácter encriptado C.
    """
    e, n = llave_publica  # Extraer e y n de la clave pública

    # Validación de entrada
    if not (0 <= caracter < n):
        return f"Error: El carácter {caracter} debe ser un número entero positivo menor que {n}."

    # Cálculo de C = (M^e) mod n
    c = pow(caracter, e, n)  # pow() con tres argumentos es eficiente para cálculo modular
    return c

# Ejemplos de uso corregidos
clave_publica1 = (17, 3233)
clave_publica2 = (5, 899)

# Ejemplos con cálculo manual para confirmar
resultado1 = encriptar(65, clave_publica1)  # Cálculo: (42^7) % 221 = 196
resultado2 = encriptar(15, clave_publica2)  # Cálculo: (15^5) % 899 = 759

print(f"Resultado 1 (42 con clave {clave_publica1}): {resultado1}")  # Salida esperada: 196
print(f"Resultado 2 (15 con clave {clave_publica2}): {resultado2}")  # Salida esperada: 759
print(encriptar(230, clave_publica1))  # Manejo del error: el carácter no es válido


def desencriptar(caracter_encriptado, llave_privada):
    """
    Desencripta un carácter encriptado usando la llave privada de RSA.
    
    Entrada:
    - caracter_encriptado (int): El carácter encriptado que se desea desencriptar.
    - llave_privada (tuple): La llave privada (d, n).
    
    Salida:
    - (int): El carácter original M.
    """
    d, n = llave_privada  # Extraer d y n de la clave privada

    # Validación de entrada
    if not (0 <= caracter_encriptado < n):
        return f"Error: El carácter encriptado {caracter_encriptado} debe ser un número entero positivo menor que {n}."

    # Cálculo de M = (C^d) mod n
    m = pow(caracter_encriptado, d, n)  # pow() con tres argumentos para cálculo modular eficiente
    return m

# Verificar ejemplos
llave_privada1 = (2753, 3233)
llave_privada2 = (77, 899)

resultado1 = desencriptar(2790, llave_privada1)  # Cálculo esperado: (196^103) % 221
resultado2 = desencriptar(759, llave_privada2)  # Cálculo esperado: (759^77) % 899

print(f"Resultado 1 (196 con clave privada {llave_privada1}): {resultado1}")  # Salida esperada: ?
print(f"Resultado 2 (759 con clave privada {llave_privada2}): {resultado2}")  # Salida esperada: ?
print(desencriptar(1000, llave_privada1))  # Manejo del error

