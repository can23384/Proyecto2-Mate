#
#-----------------------------------------------------------
# Proyecto2.py
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
# Descripción: Encriptado y Desencriptado de mensajes
# mediante el sistema RSA.
#-----------------------------------------------------------

from Funciones import *

def main():
    try:
        # Solicitar rango inferior y superior al usuario
        rango_inferior = int(input("Ingrese el rango inferior para generar primos: "))
        rango_superior = int(input("Ingrese el rango superior para generar primos: "))

        # Validar que el rango sea correcto
        if rango_inferior >= rango_superior:
            raise ValueError("El rango inferior debe ser menor que el rango superior.")

        # Generar dos numeros primos p y q
        p = generar_primo(rango_inferior, rango_superior)
        q = generar_primo(rango_inferior, rango_superior)
        while p == q:  # Asegurar que p y q sean distintos
            q = generar_primo(rango_inferior, rango_superior)

        # Calcular n y ϕ(n)
        n = p * q
        phi = (p - 1) * (q - 1)

        # Encontrar e
        e = next((x for x in range(2, phi) if mcd(x, phi) == 1), None)
        if e is None:
            raise ValueError("No se pudo encontrar un valor válido para 'e'.")

        # Calcular d 
        d = inverso_modular(e, phi)
        if isinstance(d, str):
            raise ValueError(f"Error al calcular d: {d}")

        # Claves publica y privada
        clave_publica = (e, n)
        clave_privada = (d, n)

        # Imprimir los valores generados
        print("\nValores generados:")
        print(f"p: {p}")
        print(f"q: {q}")
        print(f"n (p*q): {n}")
        print(f"ϕ(n): {phi}")
        print(f"e : {e}")
        print(f"d : {d}")
        print(f"Clave pública: {clave_publica}")
        print(f"Clave privada: {clave_privada}")

        # Solicitar mensajes al usuario
        mensajes = []
        print("\nIngrese los mensajes que desea probar (valores enteros menores que 'n'). Escriba 'done' para terminar:")
        while True:
            entrada = input("Mensaje: ")
            if entrada.lower() == "done":
                break
            try:
                mensaje = int(entrada)
                if mensaje >= n:
                    print(f"El mensaje debe ser menor que {n}. Intente nuevamente.")
                else:
                    mensajes.append(mensaje)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        # Probar encriptacion y desencriptacion con los mensajes ingresados
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

        # Documentar los resultados
        print("\nResultados de las pruebas:")
        for original, encriptado, desencriptado in resultados:
            print(f"Original (m): {original}, Encriptado (c): {encriptado}, Desencriptado (m): {desencriptado}")

    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()
