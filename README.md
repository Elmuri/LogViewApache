<p align="center">
 <img width=20% height=20% src="https://i.imgur.com/bGizZPd.png" alt="Proyecto logo">
</p>

<h1 align="center"> Visor de log de apache </h1>


Este es un programa o mejor dicho una app que permite visualizar los log de apache, asi como incluir un pequeño buscador para resaltar las palabras que estamos buscando como fechas o directorios.


## Deployment

- Tener Python instalado en su maquina, descargar el lenguaje desde [aqui](https://www.python.org/downloads/).

## Crear un ejecutable

Para convertir el archivo en un ejecutable necesitaremos la libreria  pyinstaller
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
