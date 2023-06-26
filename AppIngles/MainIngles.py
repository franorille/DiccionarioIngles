import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

from tkinter import ttk
from tkinter.ttk import Treeview, Separator

# ----------------- CONEXION BBDD --------------------

DDBB_name = "Diccionario"


def conectar():
    try:
        conexion = sqlite3.connect(DDBB_name)
        miCursor = conexion.cursor()
        miCursor.execute('''CREATE TABLE DICCIONARIO(
                    INGLES VARCHAR2(30) PRIMARY KEY NOT NULL,
                    ESPAÑOL VARCHAR2(50) NOT NULL,
                    ESPAÑOL2 VARCHAR2(50),
                    EJEMPLO VARCHAR2(300))''')

        # ''' rodear instrucciones con tres comillas simples permite escribir código en varias líneas con saltos de línea'''

        messagebox.showinfo("Conexión", "Base de datos creada correctamente")

    except:
        messagebox.showwarning("Conexión", "La base de datos ya había sido creada previamente")


# ---------------- SALIR APLICACION ------------------------------

def exitApp():
    respuesta = messagebox.askquestion("Salir", "¿Quieres salir de la aplicación?")
    if respuesta == "yes":
        root.destroy()


# ------------ RUD_BBDD-------------------------

def read():
    conexion = sqlite3.connect(DDBB_name)
    miCursorRUD = conexion.cursor()

    InsertarIngles=veIngles.get().strip()
    if len(InsertarIngles)==0:
        messagebox.showwarning("Necesario introducir campo", "No se ha especificado palabra en inglés a buscar")

    else:
        miCursorRUD.execute("SELECT * FROM DICCIONARIO WHERE INGLES='" + eIngles.get() + "'")
        palabras = miCursorRUD.fetchall()
        tabla.delete(*tabla.get_children())

        for i, fila in enumerate(palabras):
            tabla.insert(parent='', index='end', iid=i, text=i, values=fila)

        conexion.commit()

    conexion.close()


def insertar():
    conexion = sqlite3.connect(DDBB_name)
    miCursorRUD = conexion.cursor()
    datos_introducidos = veIngles.get().strip(), veEspagnol.get().strip(), veEspagnol2.get().strip(), tEjemplo.get("1.0", "end").strip()

    InsertarIngles=veIngles.get()
    InsertarEspagnol=veEspagnol.get()

    if len(InsertarIngles)==0 or len(InsertarEspagnol)==0:
        messagebox.showerror("Campos obligatorios", "Es necesario introducir los campos Inglés y Español")

    else:
        miCursorRUD.execute("INSERT INTO DICCIONARIO VALUES(?,?,?,?)", (datos_introducidos))
        conexion.commit()
        messagebox.showinfo("Insertar registro", "Registro insertado con éxito")

    conexion.close()



def borrar():
    conexion = sqlite3.connect(DDBB_name)
    miCursorRUD = conexion.cursor()

    try:

        clave = str(tabla.item(tabla.selection())["values"][0])

        respuesta = messagebox.askquestion("Borrar registro", "Estas seguro de querer borrar el registro " + clave)
        if respuesta == "yes":

            miCursorRUD.execute("DELETE FROM DICCIONARIO WHERE INGLES='" + clave + "'")
            conexion.commit()
            messagebox.showinfo("Borrar registro", "Registro borrado con éxito")
            tabla.delete(*tabla.get_children())

    except:
        messagebox.showwarning("Advertencia", "No hay registro para borrar")

    conexion.close()

def actualizar():
    pass

def leerTodos():
    pass




# --------------- Creación ventana principal -----------------------
root = tkinter.Tk()

# -------------- Creamos menu -----------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)
# estas dimensiones de la ventana se irán adaptando a lo que metamos en su interior

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conectar)
bbddMenu.add_command(label="Salir", command=exitApp)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de")

# Añadir items de menu creados de cada uno de los menus en el que la barra de menu,
# debe agregar con etiqueta Archivo los items de menu creados en bbddMenu
barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# --------------- FRAME SUPERIOR -------------------------------------
frameN = Frame(root)
frameN.pack()
frameN.config(pady=10)

# ----------- Etiquetas Frame N ---------------
lnIngles = Label(frameN, text="Inglés")
lnIngles.grid(row=0, column=0, padx=10, sticky="n")

lnEspagnol = Label(frameN, text="Español")
lnEspagnol.grid(row=0, column=1, padx=10, sticky="n")

lnEspagnol2 = Label(frameN, text="Español 2")
lnEspagnol2.grid(row=0, column=2, padx=10, sticky="n")

lnEjemplo = Label(frameN, text="Frase de ejemplo")
lnEjemplo.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="n")

# ---------- entries frame superior -------------------------------------

# creo variables para las entries,
# que luego me permiten manipular su contenido
# le decimos que en cada entry habrá una cadena de caracteres

veIngles = StringVar()
veEspagnol = StringVar()
veEspagnol2 = StringVar()

# vtEjemplo=StringVar() -- esta no hace falta porque no es tipo entry sino tipo Text

eIngles = Entry(frameN, textvariable=veIngles)
eIngles.grid(row=1, column=0, padx=10, pady=3)
eIngles.config(fg="red")

eEspagnol = Entry(frameN, textvariable=veEspagnol)
eEspagnol.grid(row=1, column=1, padx=10, pady=3)

eEspagnol2 = Entry(frameN, textvariable=veEspagnol2)
eEspagnol2.grid(row=1, column=2, padx=10, pady=3)

tEjemplo = Text(frameN, width=60, height=5, padx=10, pady=3)
tEjemplo.grid(row=3, columnspan=3, padx=10)

scrollEjemplo = Scrollbar(frameN, command=tEjemplo.yview)
scrollEjemplo.grid(row=3, column=3, sticky="nsew")

# Indica que la barra de desplazamiento
# creada funciona junto con el Área de texto tEjemplo
tEjemplo.config(yscrollcommand=scrollEjemplo.set)

# ---------------- CREACION DE SEPARADOR N-C ------------------------

separadorNC = Separator(root, orient="horizontal")
separadorNC.pack(fill="x", pady=2)

# ----------------- CREACION FRAME SUR -----------------------------

frameS = Frame(root)
frameS.pack()
frameS.config(pady=10, padx=0)

# ------------- TABLA FRAME SUR ---------------------
# creación de la tabla
tabla = ttk.Treeview(frameS, columns=("col1", "col2", "col3", "col4"), show="headings")
# show headings para que solo muestre encabezados y no el índice #0 que es columna reservada para los índices, que aunque no se vea, está ahi


# Creación de las columnas
tabla.column("#0", anchor=CENTER)
tabla.column("col1", anchor=CENTER)
tabla.column("col2", anchor=CENTER)
tabla.column("col3", anchor=CENTER)
tabla.column("col4", anchor=CENTER)

# Creación de los encabezados de las columnas

tabla.heading("col1", text="Ingles", anchor=CENTER)
tabla.heading("col2", text="Español", anchor=CENTER)
tabla.heading("col3", text="Español 2", anchor=CENTER)
tabla.heading("col4", text="Ejemplo", anchor=CENTER)

tabla.pack()

# ----------- Botones Frame N ---------------


bConectar = Button(frameN, text="Conectar", width=10, command=conectar)
bConectar.grid(row=0, column=5, sticky="e", padx=1)

bSalir = Button(frameN, text="Salir", width=10, command=exitApp)
bSalir.grid(row=0, column=6, sticky="w", padx=1)

bLeer = Button(frameN, width=10, text="Leer", command=read)
bLeer.grid(row=1, column=5, sticky="e", padx=1)

bInsertar = Button(frameN, text="Insertar", width=10, command=insertar)
bInsertar.grid(row=2, column=5, sticky="e", padx=1)

bAcutalizar = Button(frameN, width=10, text="Actualizar", command=actualizar)
bAcutalizar.grid(row=2, column=6, padx=1, sticky="w")

bBorrar = Button(frameN, width=10, text="Borrar", command=borrar)
bBorrar.grid(row=1, column=6, sticky="w", padx=1)

bLeerTodos = Button(frameN, width=20, text="Leer todos", command=leerTodos)
bLeerTodos.grid(row=3, column=5, columnspan=2, padx=1)

root.mainloop()
