from paquete1 import modulos_paquetes

print(modulos_paquetes.saludar("Daniel Contreras"))
nombre,tel=modulos_paquetes.solicitarDatos4()

print(f"\n\t.::Agenda Telefonica::.\n\tNombre:{nombre}\n\tTelefono: {tel}")
modulos_paquetes.esperarTecla()