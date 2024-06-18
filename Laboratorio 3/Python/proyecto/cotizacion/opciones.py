import ventana


while True:
    tamanio = int(input("""
    __ Bienvenido a la sección de Cotización __
    Seleccione el tamaño de la construcción:
    (1) Small
    (2) Medium
    """))

    match tamanio:
        case 1:
            print('1')
        case 2:
            command.ir_cotizaciones()

