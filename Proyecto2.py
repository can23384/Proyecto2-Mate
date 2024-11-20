from Funciones import generar_llaves, encriptar, desencriptar, generar_primo, mcd, inverso_modular

def main():
    # Paso 1: Generar claves RSA
    rango_inferior = 100
    rango_superior = 200

    # Generar dos números primos p y q
    p = generar_primo(rango_inferior, rango_superior)
    q = generar_primo(rango_inferior, rango_superior)
    while p == q:  # Asegurar que p y q sean distintos
        q = generar_primo(rango_inferior, rango_superior)

    # Calcular n y ϕ(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Encontrar e
    e = None
    for candidate in range(2, phi):
        if mcd(candidate, phi) == 1:
            e = candidate
            break

    if e is None:
        print("Error: No se pudo encontrar un valor válido para 'e'.")
        return

    # Calcular d (inverso modular de e mod ϕ(n))
    d = inverso_modular(e, phi)
    if isinstance(d, str):
        print(f"Error al calcular d: {d}")
        return

    # Claves pública y privada
    clave_publica = (e, n)
    clave_privada = (d, n)

    # Imprimir los valores generados
    print("Valores generados:")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"n (p*q): {n}")
    print(f"ϕ(n): {phi}")
    print(f"e (clave pública): {e}")
    print(f"d (clave privada): {d}")
    print(f"Clave pública: {clave_publica}")
    print(f"Clave privada: {clave_privada}")

    # Paso 2: Mensajes para probar
    mensajes = [42, 123, 75]  # Mensajes numéricos, deben ser menores que 'n'
    resultados = []

    for mensaje in mensajes:
        print(f"\nMensaje original (m): {mensaje}")

        # Encriptar
        mensaje_encriptado = encriptar(mensaje, clave_publica)
        if isinstance(mensaje_encriptado, str):  # Verifica si hay un error
            print(f"Error durante la encriptación: {mensaje_encriptado}")
            continue

        print(f"Mensaje encriptado (c): {mensaje_encriptado}")

        # Desencriptar
        mensaje_desencriptado = desencriptar(mensaje_encriptado, clave_privada)
        if isinstance(mensaje_desencriptado, str):  # Verifica si hay un error
            print(f"Error durante la desencriptación: {mensaje_desencriptado}")
            continue

        print(f"Mensaje desencriptado (m): {mensaje_desencriptado}")
        resultados.append((mensaje, mensaje_encriptado, mensaje_desencriptado))

    # Paso 3: Documentar los resultados
    print("\nResultados de las pruebas:")
    for original, encriptado, desencriptado in resultados:
        print(f"Original (m): {original}, Encriptado (c): {encriptado}, Desencriptado (m): {desencriptado}")

if __name__ == "__main__":
    main()
