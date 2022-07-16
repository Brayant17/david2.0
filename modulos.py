def saludo(nombre):
    print("hola", nombre)
    return True

def menu():
    opcion = input("comandos disponibles \n --NewProduct --venta --ShowProdcuts\n --")
    return opcion

def exit():
    command = input("Comando 'exit' para salir del programa \n --")
    return command