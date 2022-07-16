#New project for Brayant Flores
# Programa que tenga dos secciones para registrar productos o venderlos y ticket
# catalago creado por el usuario 
# y en la venta agregar lo que esta en el catalogo e imprimir el ticket con iva

class Productos:
    def __init__(self, nombre, descripcion, codigoBarras, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.codigoBarras = codigoBarras
        self.precio = precio

        