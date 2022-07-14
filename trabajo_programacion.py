from datetime import datetime
now = datetime.now()

nombre_cliente=input(f"escriba su nombre ") # rodrigo garcia
fecha = now

mantenimiento_computadora=250 #erik gonzales
instalacion_windows=150
pasta_termica=200
revision=50
resultado=0
resultadototal=0
iva=0.16
numero=100
#david solis
folio=format(id(numero),"x")
print(folio)
lista1=[] #lista vacia para luego agregar con append para mostras el registro de compra david solis


#david solis
menuprincipal=int(input("Menu Principal:\n 1-Mantenimiento de computadoras \n 2-Instalacion windows \n 3-pasta termica \n 4-revision \n 0-salir y obtener el total de la cuenta" ))
#david solis
while menuprincipal !=0:
    if menuprincipal== 1:
        print(f"TICKET",nombre_cliente,fecha,) 
        resultado=mantenimiento_computadora*iva
        print(f"el total de pagar de iva es",resultado)
        print(f"el pago toal es de",resultado+mantenimiento_computadora)
        resultadototal=resultadototal+resultado+mantenimiento_computadora
        lista1.append("Mantenimiento de computadora = 250")
        
   
   
   #de aqui en adelante participamos todos
    elif menuprincipal==2:
        print(f"TICKET",nombre_cliente,fecha) 
        resultado=instalacion_windows*iva
        print(f"el total de pagar de iva es",resultado)
        print(f"el pago toal es de",resultado+instalacion_windows)
        resultadototal=resultadototal+resultado+instalacion_windows
        lista1.append("instalacion windows = 150")
        
        
    elif menuprincipal==3:
            print(f"TICKET",nombre_cliente,fecha) 
            resultado= pasta_termica*iva
            print(f"el total de pagar de iva es",resultado)
            print(f"el pago toal es de",resultado+pasta_termica)
            resultadototal=resultadototal+resultado+pasta_termica
            lista1.append("pasta_termica = 200")
            
            
    elif menuprincipal==4:
             print(f"TICKET",nombre_cliente,fecha) 
             resultado=revision*iva
             print(f"el total de pagar de iva es",resultado)
             print(f"el pago toal es de",resultado+revision)
             resultadototal=resultadototal+resultado+revision
             lista1.append("revision = 50")
             
    elif menuprincipal==0:
             print(f"TICKET",nombre_cliente,fecha) 
             print ("total de la cuuenta ",resultadototal)
             print(f"Su Folio Es")
             folio=format(id(revision),"x")
             print(folio)
    else:
        print ("Porfavor digite una opcion valida ")
        
    
    print("escoja otro servicio si lo requiere o presione 0")
    
    menuprincipal=int(input("\n 0-salir y obtener el total de su cuenta:  " ))
    
if menuprincipal==0:
             print(f"TICKET",nombre_cliente,fecha) 
             print ("total de la cuenta ",resultadototal)
             print(f"Su Folio Es")
             folio=format(id(revision),"x")
             print(folio)
             print(lista1)