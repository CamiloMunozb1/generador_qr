from funcion_qr.uso import uso_qr


while True:
    print("""
            BIENVENIDO AL GENERADOR DE QR
            1. Generar codigo QR.
            2. Modo de uso.
            3. Salir.
        """)
    try:
        usuario = int(input("Ingresa una opcion: "))
        if usuario == 1:
            print("Funcion proxima.")
        elif usuario == 2:
            uso_qr()
        else:
            print("Hasta la proxima.")
            break
    except ValueError:
        print("Error de digitacion, volver a intentar.")