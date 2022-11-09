# NOTE - importaciones
from tkinter import *
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import json

# NOTE - Extracción de la configuración del json
cofg = open("config.json", "r")
config = cofg.read()
configuracion = json.loads(config)

# NOTE - creación de la ventana
root = Tk()
root.title('Visor|Buscador de log de apache')

for conf in configuracion["Ventana"]:
    # NOTE - Definiendo el tamaño de la ventana
    root.geometry(conf['whidth']+"x"+conf['height'])

fram = Frame(root)
# NOTE - definiendo el apartado de busqueda
Label(fram, text='buscar:').pack(side=LEFT, padx=4, pady=4)
edit = Entry(fram)
edit.pack(side=LEFT, fill=BOTH, expand=1)
edit.focus_set()
butt = Button(fram, text='Buscar')
butt.pack(side=RIGHT)
fram.pack(side=TOP)
# NOTE - definiendo la ventana de visualización del log
for conf in configuracion["custom"]:
    text = st.ScrolledText(root, width=300, height=300,
                           font=("Arial",conf['size']),fg = conf['Texto_color'], bg=conf['contenedorDeTexto_color'])
text.pack(side=BOTTOM)
# NOTE - creando el menu
menubar1 = Menu(root)
root.config(menu=menubar1)
opciones1 = Menu(menubar1, tearoff=0)

# NOTE - declaraciones de las funciones
# NOTE - función de busqueda


def find():
    text.tag_remove('found', '1.0', END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(s))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        for conf in configuracion["Color_Busqueda"]:
            text.tag_config('found', foreground=conf['color'])
    edit.focus_set()


butt.config(command=find)

# NOTE - funcion de salir del programa


def salir():
    root.destroy()

# NOTE - funcion de guardado


def guardar():
    nombrearch = fd.asksaveasfilename(initialdir="/", title="Guardar como", filetypes=(
        ("txt files", "*.log"), ("todos los archivos", "*.*")))
    if nombrearch != '':
        archi1 = open(nombrearch, "w", encoding="utf-8")
        archi1.write(text.get("1.0", END))
        archi1.close()
        mb.showinfo("Información", "Los datos fueron guardados en el archivo.")


# NOTE - funcion de abrir el log de error de apache
def abrir_error():
    for conf in configuracion["Directorios"]:
        # NOTE - Definiendo el tamaño de la ventana
        with open(conf["error"], mode="r", encoding="utf-8") as file_objet:
            contenido = file_objet.readlines()
            text.delete("1.0", END)
            text.insert("1.0", contenido)


# NOTE - funcion de abrir el log de access de apache
def abrir_access():
    for conf in configuracion["Directorios"]:
        with open(conf["acces"], mode="r", encoding="utf-8") as file_objet:
            leer = file_objet.read()
            text.delete("1.0", END)
            text.insert("1.0", leer)

# NOTE - funcion para ver abrir un log externo


def abrir():
    nombrearch = fd.askopenfilename(initialdir="C:/xampp/apache/logs/access.log",
                                    title="Seleccione archivo", filetypes=(("txt files", "*.log"), ("todos los archivos", "*.*")))
    if nombrearch != '':
        archi1 = open(nombrearch, "r", encoding="utf-8")
        contenido = archi1.readlines()
        archi1.close()
        text.delete("1.0", END)
        text.insert("1.0", contenido)


# NOTE - añadiendo los comandos del menu
opciones1.add_command(label="Abrir log de access", command=abrir_access)
opciones1.add_separator()
opciones1.add_command(label="Abrir log de error", command=abrir_error)
opciones1.add_separator()
opciones1.add_command(label="Guardar Copia de seguridad", command=guardar)
opciones1.add_separator()
opciones1.add_command(label="Abrir log", command=abrir)
opciones1.add_separator()
opciones1.add_command(label="Salir", command=salir)
# NOTE - apartado de selección del menu
menubar1.add_cascade(label="Archivo", menu=opciones1)

# NOTE - ver la ventana
root.mainloop()
