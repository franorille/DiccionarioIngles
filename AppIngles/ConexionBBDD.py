import sqlite3
from tkinter import messagebox

DDBB_name="Diccionario"
def conectar():

    try:
        conexion = sqlite3.connect(DDBB_name)
        miCursor = conexion.cursor()
        miCursor.execute('''CREATE TABLE DICCIONARIO(
                    INGLES TEXT PRIMARY KEY,
                    ESPAÑOL TEXT NOT NULL,
                    ESPAÑOL2 TEXT,
                    EJEMPLO TEXT)''')

        messagebox.showinfo("Conexión", "Base de datos creada correctamente")

    except:
        messagebox.showwarning("Conexión", "La base de datos ya había sido creada previamente")
