from ConexionBBDD import *
import sqlite3

conexion = sqlite3.connect(DDBB_name)
miCursorRUD = conexion.cursor()

def read():
    datos=[]
    datos = miCursorRUD.execute("SELECT * FROM DICCIONARIO")

    for d in datos:
        print(d)

    """
    ingles=datos[0]
    espagnol=datos[1]
    espagnol2=datos[2]
    ejemplo=datos[3]

    print(ingles)
    print(espagnol)
    print(espagnol2)
    print(ejemplo)
    """


def insertar():
    miCursorRUD.execute("INSERT INTO DICCIONARIO VALUES('ingles1','ingles1','ingles1','ingles1')")
    conexion.commit()


