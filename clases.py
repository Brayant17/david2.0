class Productos:
    def __init__(self, nombre, descripcion, codigoBarras, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.codigoBarras = codigoBarras
        self.precio = precio

    def set(self):
        print(self.nombre, self.descripcion, "\t ",self.precio)