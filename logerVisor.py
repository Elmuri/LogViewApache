# NOTE - importaciones
from tkinter import *
from tkinter import scrolledtext as st
from tkinter import filedialog as fd
from tkinter import messagebox as mb

# NOTE - definiendo la ventana y el frame
root = Tk()
root.geometry("1000x1000")
root.title('Visor|Buscador de log de apache')
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
text = st.ScrolledText(root, width=300, height=300)
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
        text.tag_config('found', foreground='#FF0000')
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
    archi1 = open("C:/xampp/apache/logs/error.log", mode="r", encoding="utf-8")
    contenido = archi1.readlines()
    archi1.close()
    text.delete("1.0", END)
    text.insert("1.0", contenido)

# NOTE - funcion de abrir el log de access de apache
def abrir_access():
    with open("C:/xampp/apache/logs/access.log", mode="r", encoding="utf-8") as file_objet:
        leer = file_objet.read()
        text.delete("1.0", END)
        text.insert("1.0", leer)

# NOTE - funcion para ver abrir un log externo
def recuperar():
    nombrearch = fd.askopenfilename(initialdir="C:/xampp/apache/logs/access.log",
                                    title="Seleccione archivo", filetypes=(("txt files", "*.log"), ("todos los archivos", "*.*")))
    if nombrearch != '':
        archi1 = open(nombrearch, "r", encoding="utf-8")
        contenido = archi1.readlines()
        archi1.close()
        text.delete("1.0", END)
        text.insert("1.0", contenido)


# NOTE - añadiendo los comandos del menu
opciones1.add_command(label="abrir log de access", command=abrir_access)
opciones1.add_separator()
opciones1.add_command(label="abrir log de error", command=abrir_error)
opciones1.add_separator()
opciones1.add_command(label="Guardar Copia de seguridad", command=guardar)
opciones1.add_separator()
opciones1.add_command(label="Recuperar archivo", command=recuperar)
opciones1.add_separator()
opciones1.add_command(label="Salir", command=salir)
# NOTE - apartado de selección del menu
menubar1.add_cascade(label="Archivo", menu=opciones1)

# NOTE - ver la ventana
root.mainloop()
