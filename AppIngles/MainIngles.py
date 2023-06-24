import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview, Separator
from ConexionBBDD import *
from RUD_BBDD import *

root = tkinter.Tk()

frameN = Frame(root)
frameC = Frame(root)
frameS = Frame(root)

frameN.pack(pady=20)

separador1 = Separator(root, orient="horizontal")
separador1.pack(fill="x", pady=2)

frameC.pack(pady=20)

separador2 = Separator(root, orient="horizontal")
separador2.pack(fill="x", pady=2)
frameS.pack(pady=20)

# ----------- Etiquetas Frame N ---------------
lnIngles = Label(frameN, text="Inglés")
lnIngles.grid(row=0, column=0)
lnIngles.config(padx=10, pady=10)

lnEspagnol = Label(frameN, text="Español")
lnEspagnol.grid(row=0, column=1)
lnEspagnol.config(padx=10, pady=10)

lnEspagnol2 = Label(frameN, text="Español 2")
lnEspagnol2.grid(row=0, column=2)
lnEspagnol2.config(padx=10, pady=10)

lnEjemplo = Label(frameN, text="Frase de ejemplo")
lnEjemplo.grid(row=2, column=0)
lnEjemplo.config(padx=10, pady=10)

# ----------- Entries Frame N ---------------

eIngles = Entry(frameN)
eIngles.grid(row=1, column=0)

eEspagnol = Entry(frameN)
eEspagnol.grid(row=1, column=1)

eEspagnol2 = Entry(frameN)
eEspagnol2.grid(row=1, column=2)

tEjemplo = Text(frameN, width=60, height=5)
tEjemplo.grid(row=3, columnspan=3, padx=10)

scrollEjemplo = Scrollbar(frameN, command=tEjemplo.yview)
scrollEjemplo.grid(row=3, column=3, sticky="nsew")

tEjemplo.config(yscrollcommand=scrollEjemplo.set)

# ----------- Etiquetas Frame C ---------------

lcIngles = Label(frameC, text="Inglés")
lcIngles.grid(row=0, column=0)
lcIngles.config(padx=10, pady=10)

lcEspagnol = Label(frameC, text="Español")
lcEspagnol.grid(row=1, column=0)
lcEspagnol.config(padx=10, pady=10)

lcEspagnol2 = Label(frameC, text="Español 2")
lcEspagnol2.grid(row=2, column=0)
lcEspagnol2.config(padx=10, pady=10)

lcEjemplo = Label(frameC, text="Frase de ejemplo")
lcEjemplo.grid(row=3, column=0)
lcEjemplo.config(padx=10, pady=10)

# ----------- Entries Frame C ---------------

eCIngles = Entry(frameC)
eCIngles.grid(row=0, column=1)

eCEspagnol = Entry(frameC)
eCEspagnol.grid(row=1, column=1)

eCEspagnol2 = Entry(frameC)
eCEspagnol2.grid(row=2, column=1)

tCEjemplo = Text(frameC, width=40, height=5)
tCEjemplo.grid(row=3, column=1, columnspan=4)

scrollCEjemplo = Scrollbar(frameC, command=tEjemplo.yview)
scrollCEjemplo.grid(row=3, column=6, sticky="nsew")

tCEjemplo.config(yscrollcommand=scrollCEjemplo.set)

# ----------- Botones Frame S ---------------

bConectar = Button(frameS, text="Conectar", command=conectar)
bConectar.grid(row=0, column=0, padx=10)

bLeer = Button(frameS, text="Leer", command=read)
bLeer.grid(row=0, column=1, padx=10)

bBuscar = Button(frameS, text="Insertar", command=insertar)
bBuscar.grid(row=0, column=2, padx=10)

bAcutalizar = Button(frameS, text="Actualizar")
bAcutalizar.grid(row=0, column=3, padx=10)

bBorrar = Button(frameS, text="Borrar")
bBorrar.grid(row=0, column=4, padx=10)

bTest = Button(frameS, text="Test")
bTest.grid(row=0, column=5, padx=10)

root.mainloop()
