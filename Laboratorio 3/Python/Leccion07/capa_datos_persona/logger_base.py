import logging as log       # log= logging    Es igual

# docs.python.org/3/howto/logging.html
# llamamos una configuración básica

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
                #error hora, nivel, nombre archivo, linea y mensaje
                datefmt='%I:%M:%S %p',  #DATE FORMAT FORMATO DE FECHA: hora, min, seg, pm
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')
