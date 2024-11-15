
# FUNCIONES PARA IMPORTAR AL INDEX.

from funcion_qr.uso import uso_qr
from funcion_qr.generador import generador_qr


while True:

    # MENU DE USUARIO.

    print("""
            BIENVENIDO AL GENERADOR DE QR
            1. Generar codigo QR.
            2. Modo de uso.
            3. Salir.
        """)
    try:

        # ENTRADA DE USUARIO PARA ELECCION DEL USUARIO.

        usuario = int(input("Ingresa una opcion: "))

        # CONDIONES SEGUN LA ELECCION DE USUARIO.

        if usuario == 1:
            generador_qr()
        elif usuario == 2:
            uso_qr()
        else:

            # SALIDA DE USUARIO.

            print("Hasta la proxima.")
            break
    
    # MANEJO DE ERRORES.
    
    except ValueError:
        print("Error de digitacion, volver a intentar.")