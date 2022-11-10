<p align="center">
 <img width=20% height=20% src="https://i.imgur.com/bGizZPd.png" alt="Proyecto logo">
 <h1> Visor/Buscador en los registros|log de Apache PYTHON TKINTER</h1>
</p>

<p>Este es un programa o mejor dicho una app que permite visualizar los log de apache /u otros log que queramos visualizar, asi como incluir un pequeño buscador para resaltar las palabras que estamos buscando como fechas o directorios.</p>

<h2>A tener en cuenta</h2>
<p>Puede descargar el repositorio pero el .exe tiene que estar en la misma carpeta que config.json, luego puede crear un acceso directo e abrirlo desde donde quiera, asu ves si cambia los valores del config.json para efectar los cambios en la app tiene que reiniciarla.</p>

## Deployment

- Tener Python instalado en su maquina, descargar el lenguaje desde [aqui](https://www.python.org/downloads/).

## Crear un ejecutable

Para convertir el archivo en un ejecutable necesitaremos la libreria pyinstaller.
Para instalarla la libreria escribimos.
```
pip install pyinstaller
```

Debemos abrir una terminal en el directorio donde se encuentre el archivo.
```
pyinstaller logerVisor.py --onefile --noconsole
```
Por si desea un icono custom para el exe.
```
pyinstaller logerVisor.py --onefile --noconsole --icon=icono_loger.ico
```

# Instalador

si se quisiera crear un instalador para la app puede seguir el sigiente [tutorial](https://www.youtube.com/watch?v=W4QQ-ua9Ips).

<h2>Configuración de la app</h2>
<p align="center">
 <p>En el <strong>config.json</strong> Puede encontrar los parametros a poder cambiarse a gustos del usuario.</p>
 <p>En en apartado de <strong>Ventana</strong> podemos encontrar el <strong>whidth</strong> que representa al ancho de la ventana y el <strong>height</strong> que representa el alto de la ventana.</p>
 <p>En el apartado de <strong>Directorios</strong> podemos encontrar <strong>acces</strong> y <strong>error</strong> que son los que definen que archivos abrir para las funciones de del menu de abrir acces o abrir error, por defecto esta seleccionado los resgistros de apache.</p>
 <p>En el apartado de custom podemos encontrar los cambios de colores tanto del resaltado del texto al buscarlo (<strong>find</strong>), el color del contenedor del texto (<strong>contenedorDeTexto_color</strong>), el color del texto (<strong>Texto_color</strong>) y el tamaño del texto (<strong>size</strong>).</p>
 <img width=40% height=40% src="https://i.imgur.com/Rc1L0Dz.png" alt="Proyecto logo">
</p>
