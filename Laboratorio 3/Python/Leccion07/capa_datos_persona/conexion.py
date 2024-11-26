import psycopg2 as bd
from logger_base import log
import sys

class Conexion:
    _DATABASE = 'test_bd'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5

    @classmethod
    def obtenerConexion(cls):
        pass

    @classmethod
    def obtenerCursor(cls):
        pass

if __name__ == '__main__':
    pass