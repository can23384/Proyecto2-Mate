# Proyecto2 - Encriptación RSA

## Autores

-   [Eliazar José Pablo Canastuj Matías - 23384]
-   [Diego Alejandro Ramírez Velásquez - 23601]
-   [María José Yee Vidal - 231193]

## Descripción
El objetivo de este proyecto fue implementar un sistema criptográfico basado en el algoritmo RSA utilizando el lenguaje de programación Python. RSA es uno de los métodos más seguros y ampliamente utilizados para la encriptación de datos, basado en la dificultad de factorizar números grandes en sus factores primos. Este proyecto se centró en desarrollar una implementación funcional que permita generar claves, encriptar y desencriptar mensajes, mientras se aplican los principios matemáticos de teoría de números y álgebra modular.

El desarrollo del proyecto incluyó la creación de varias funciones clave, como la generación de números primos, el cálculo del máximo común divisor (MCD), la determinación del inverso modular, y el cálculo de las claves pública y privada. Estas funciones se integraron para construir un sistema completo de cifrado y descifrado de mensajes, que fue probado con distintos casos prácticos.

Además, se diseñaron y ejecutaron casos de prueba para verificar el correcto funcionamiento del algoritmo y documentar los resultados obtenidos. La implementación de este proyecto permitió no solo comprender los fundamentos teóricos del algoritmo RSA, sino también aplicar conocimientos matemáticos y de programación para resolver un problema real de seguridad en la comunicación.


### Instalacion
Para ejecutar el programa de manera eficiente y sin errores, se deben seguir los siguientes pasos:

Verificar la instalación de Python: El programa requiere Python 3.6 o superior.
Preparar los archivos necesarios: Los archivos Funciones.py y Proyecto2.py deben estar en el mismo directorio de trabajo.
Ejecutar el programa principal: Desde una terminal o un entorno de desarrollo como Visual Studio Code o PyCharm, se debe navegar hasta el directorio que contiene los archivos y ejecutar el programa principal utilizando el comando: python Proyecto2.py
Seleccionar rangos adecuados: Durante la ejecución, se deben especificar rangos amplios para la generación de números primos (por ejemplo, entre 100 y 200). Esto aumenta la probabilidad de obtener números primos válidos para las claves.
Probar los mensajes predeterminados: El programa incluye mensajes de prueba predeterminados (42, 123, 75) que son compatibles con las claves generadas. Si se desean probar otros mensajes, estos deben ser menores que 𝑛 para garantizar que el cifrado y descifrado funcionen correctamente.
Atender mensajes de error: El programa maneja errores comunes, como la ausencia de números primos en el rango o mensajes fuera del rango permitido. Si ocurre algún error, se recomienda revisar el mensaje mostrado en la consola para realizar los ajustes necesarios.
