
# USO DE LA LIBRERIA "PIL" PARA EL MANEJO Y PERSOONALIZACION DEL QR.

from PIL import Image, ImageDraw, ImageFont

# USO DE LA LIBRERIA "QRCODE" PARA CREACION DEL QR.

import qrcode


# USO DE UNA FUNCION QUE SE IMPORTARA AL INDEX.

def generador_qr():
    try:

        # ENTRADAS DE USUARIO PARA EL INGRESO DEL LINK DEL QR Y EL MENSAJE QUE SE QUIERE MOSTRAR.

        link_usuario = str(input("Ingresa el link para generar el codigo QR: "))
        mensaje_qr = str(input("Ingresa el mensaje que contendra el qr: "))

        # GENERACION DEL CODIGO CON EL LINK DADO POR EL USUARIO.

        img = qrcode.make(f"{link_usuario}")

        # SE DIBIJA LA IMAGEN DEL CODIGO QR JUNTO CON EL TEXTO.

        new_image = Image.new("RGB", (img.size[0],img.size[1]+50),"white")

        # SE PEGA EL TEXTO EN LA IMAGEN DEL QR.

        new_image.paste(img,(0,0))

        # SE ESCRIBE EL TEXTO SOBRE LA IMAGEN.

        draw = ImageDraw.Draw(new_image)

        # EN ESTA VARIABLE SE ALMACENA EL MENSAJE DEL USUARIO

        mensaje = f"{mensaje_qr}"

        # COORDENADAS PARA COLOCAR EL TEXTO DENAJO DEL QR Y QUE SUI LETRA SEA NEGRA.

        draw.text((10,img.size[1]+10), mensaje, fill="black")

        # SE ALAMACENA LA NUEWVA IMAGEN.

        new_image.save("Nuevo_qr.png")

    # MANEJO DE ERRORES.
    
    except ValueError:
        print("valor incorrecto volver a ingresar.")
