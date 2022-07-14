import datetime
import time
import sys
import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("BDProgramacion.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS empresa (folio INTEGER PRIMARY KEY, fecha_servicio TIMESTAMP, nombre_cliente TEXTNOT NULL, monto REAL NOT NULL);")
        print("Tabla creada exitosamente")

        while True:
            folio = int(input(f"\nDime el folio: "))
            if folio == 0:
                break
            fecha = input("Dime la fecha del servicio (dd/mm/aaaa): \n")
            nombre_cliente = input("Dime su nombre: ")
            monto = float(input(f"\n Dime el monto: "))
            valores = (folio,fecha,nombre_cliente,monto)
            mi_cursor.execute("INSERT INTO empresa VALUES ()", valores)
            print(f"\nSe guardaron los datos con exito")
            print("hola como estas")
except Error as e:
    print(e)
except:
    print(f"\nSe produjo el siguiente error: {sys.exc_info()[0]}")
finally:
    conn.close()