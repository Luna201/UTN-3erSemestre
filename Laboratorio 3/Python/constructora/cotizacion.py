import main


def ir_cotizacion():

    while True:
        tamanio = int(input("""
__ Bienvenido a la sección de Cotización __
Seleccione el tamaño de la construcción:
(1) Small
(2) Medium
(3) Big
(4) Volver
    """))

        match tamanio:
            case 1:
                m2 = int(input("""
__ Seleccione el tamaño de m2: __
(1) 45 m2
(2) 60 m2
(3) 75 m2
(4) Volver
            """))
                match 1:
                    case 1:
                        print('1.1')
                    case 2:
                        print('1.2')
                    case 3:
                        print('1.3')
                    case 4:
                        ir_cotizacion()
            case 2:
                print('2')
            case 3:
                print('3')
            case 4:
                main.ir_main()
