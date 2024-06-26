def contactanos():
    # Información de contacto predeterminada
    contactos = [
        ["Brian Difilipo", "2604511997", "Briandifilipo@hotmail.com"],
        ["Dalma Ponce", "3834000000", "dalma@hotmail.com"],
        ["Andrés Luna", "2604123456", "andresluna@hotmail.com"]
    ]

    print("\n\n************************************    CONTÁCTANOS    ************************************")
    print("* ATENCIÓN PERSONALIZADA\n"
          "* WHATSAPP\n"
          "* VISITAS A OBRAS\n"
          "* PAGOS INFORMADOS\n"
          "Nuestra información de contacto\n")

    # Mostrar la información de contacto
    for contacto in contactos:
        print(f"Nombre: {contacto[0]}")
        print(f"WhatsApp: {contacto[1]}")
        print(f"Email: {contacto[2]}\n")

    # Preguntar si el usuario quiere dejar un mensaje
    print("¿Quiere dejarnos un mensaje?\n"
          "Elija una opción\n"
          "1. Sí\n"
          "2. No")
    opcion2 = input()

    if opcion2 == '1':
        # Solicitar información de contacto y mensaje
        print("Por favor, proporcione su información de contacto y mensaje:")

        nombre = input("Nombre: ")
        email = input("Correo electrónico: ")
        telefono = input("Número de teléfono: ")
        mensaje = input("Mensaje: ")

        print("Gracias por ponerse en contacto con nosotros. Le responderemos lo antes posible.")
    else:
        print("Esperamos que te comuniques pronto")

    print("********************************************************************************************")


# Llamar a la función
contactanos()
