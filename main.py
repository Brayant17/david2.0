#New project for Brayant Flores
# Programa que tenga dos secciones para registrar productos o venderlos y ticket
# catalago creado por el usuario 
# y en la venta agregar lo que esta en el catalogo e imprimir el ticket con iva
from clases import Productos

producto = Productos("refresco", "Refresco de 1lt", "01021201", 35)

print("Prodcuto",  "Descripcion", "\t ", "\tPrecio")
producto.set()