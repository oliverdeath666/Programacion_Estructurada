#1er utilizar los modulos
import modulos

modulos.borrarPantalla
print(modulos.saludar("Diego Graciano Gonzalez"))

#2da forma de utilizar moddulos
from modulos import saludar,borrarPantalla


print(saludar("Diego Graciano Gonzalez"))

nombre=input("ingresa el nombre del contacto")
telefono=input("ingresa su numero de telefono")

nom,tel=modulos.solicitarDatos4(nombre,telefono)
