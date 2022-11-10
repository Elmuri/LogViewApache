<h1>Estos son los pasos que se deverian seguir si el instalador no funciona.</h1>
<ul>
   <li>1- Descargar los archivos de esta subcarpeta.</li>
   <li>2- Ejecutar el .exe para ver si funciona.(si este funciona crear un acceso directo y listo)</li>
   <li>3- En caso que el .exe no funciona abra la terminal de comando en la dirección de la carpeta descargada.</li>
   <li>4- cree un nuevo .exe con el comando siguiente.</li>
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
   <li>Luego ejecutar los comandos buscamos el .exe e lo colocamos en la misma carpeta que el congig.json.</li>
   <li>por ultimo creamos un acceso directo del .exe para abrirlo desde donde queramos y listo nuestra app esta en funcionamiento.</li>
</ul>
