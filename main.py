#New project for Brayant Flores
# Programa que tenga dos secciones para registrar productos o venderlos y ticket
# catalago creado por el usuario 
# y en la venta agregar lo que esta en el catalogo e imprimir el ticket con iva
from clases import Productos
import modulos
producto = Productos("refresco", "Refresco de 1lt", "01021201", 35)

print("Prodcuto",  "Descripcion", "\t ", "\tPrecio")
producto.set()

lista = []
nombreUsuario = input("Quien eres?")
modulos.saludo(nombreUsuario)
while True:
    
    opcion = modulos.menu()
    
    if(opcion == 'NewProduct'):
        while True:
            print("Agregar nuevo prodcuto")
            nombre = input("Nombre del Producto: ")
            descripcion = input("Descripcion del Producto: ")
            codigoBarras = input("Codigo de Barras: ")
            precio = input("Precio del producto")
            lista.append(Productos(nombre, descripcion, codigoBarras, precio))
            exitIf = modulos.exit()
            if( exitIf == 'Exit' or exitIf == 'exit'):
                break
            
    elif(opcion == 'ShowProducts'):
        for producto in lista:
            print(producto.nombre)

    elif(opcion == 'Exit' or opcion == 'exit'):
       break
    
    else:
        print(opcion, " no se reconoce como comando")