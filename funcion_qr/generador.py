from PIL import Image, ImageDraw, ImageFont
import qrcode

def generador_qr():
    try:
        link_usuario = str(input("Ingresa el link para generar el codigo QR: "))
        mensaje_qr = str(input("Ingresa el mensaje que contendra el qr: "))
        img = qrcode.make(f"{link_usuario}")
        new_image = Image.new("RGB", (img.size[0],img.size[1]+50),"white")
        new_image.paste(img,(0,0))
        draw = ImageDraw.Draw(new_image)
        mensaje = f"{mensaje_qr}"
        draw.text((10,img.size[1]+10), mensaje, fill="black")
        new_image.save("Nuevo_qr.png")
    except ValueError:
        print("valor incorrecto volver a ingresar.")
