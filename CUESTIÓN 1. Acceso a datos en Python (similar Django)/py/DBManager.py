import sqlite3
from sqlite3 import Error
from tabulate import tabulate



def sql_connection():

    try:

        con = sqlite3.connect('tienda.db')

        return con

    except Error:

        print(Error)

def sql_Creartabla(con):

    cursorObj = con.cursor()
    try:
        cursorObj.execute("CREATE TABLE clientes(id integer PRIMARY KEY AUTOINCREMENT, nombre text, apellidos, telefono text)")
    except:
        print("La tabla ya ha sido creada")
    con.commit()


def sql_añadirCliente(con):
    cursorObj = con.cursor()
    print("Añadir un cliente:")
    nombre=input("Introduce el nombre:")
    apellidos = input("Introduce los 2 apellidos:")
    telefono = input("Introduce el telefono:")

    try:
        cursorObj.execute(f"INSERT INTO clientes ('nombre','apellidos','telefono') VALUES('{nombre}','{apellidos}','{telefono}')")
        con.commit()
    except:
        print("Ha habido un error con los datos introducidos")

def sql_update(con):
    resfiltro1=input("Introduzca el id del cliente que desea modificar\n")
    filtro2= input("¿Que quieres cambiar?\nnombre\nappellidos\ntelefono\n")
    resfiltro2=input(f"Introduce el nuevo\n")

    cursorObj = con.cursor()
    try:
        cursorObj.execute(f'UPDATE clientes SET {filtro2} = "{resfiltro2}" where id = {resfiltro1}')
        con.commit()
    except:
        print("Ha habido un error con los datos introducidos")

def sql_select(con):
    filtros=input("Introduzca las columnas que desea ver separadas por',' o si quiere ver todo introduzca '*'\n")
    filtros=filtros.lower()
    cursorObj = con.cursor()
    try:
        mostrar=f'SELECT id,{filtros} FROM clientes' if filtros!="*" else f'SELECT{filtros} FROM clientes'
        cursorObj.execute(mostrar)
        imprimir=[]

        nombreColum = list(map(lambda x: x[0], cursorObj.description))

        for row in cursorObj.fetchall():
            i = 0
            cliente=[]
            for colums in row:
                cliente.append(row[i])
                i += 1
            imprimir.append(cliente)

        salida=tabulate(imprimir,headers=nombreColum) if filtros!="*" else tabulate(imprimir,headers=["id", "nombre","apellidos","telefono"])
        print(salida)
    except:
        print("Ha habido un error con los datos introducidos")


def sql_delete(con):
    filtro1=input("¿Porque columna desea filtrar su busqueda para el borrado?\nnombre\nappellidos\ntelefono\n")
    resfiltro1=input(f"Borrar filas que su {filtro1} sea =  ")

    cursorObj = con.cursor()

    print("Va a eliminar estos clientes: ")
    try:
        cursorObj.execute(f"SELECT * FROM clientes where {filtro1} = '{resfiltro1}'")
        #[print(row) for row in cursorObj.fetchall()]

        imprimir = []

        nombreColum = list(map(lambda x: x[0], cursorObj.description))

        for row in cursorObj.fetchall():
            i = 0
            cliente = []
            for colums in row:
                cliente.append(row[i])
                i += 1
            imprimir.append(cliente)
        salida = tabulate(imprimir, headers=nombreColum)
        print(salida)

        seguro=input("\n¿Esta usted seguro? s/n   ")

        if(seguro=="s"):
            cursorObj.execute(f"DELETE FROM clientes where {filtro1} = '{resfiltro1}'")
            con.commit()
            print("cliente/s eliminado/s")
    except:
        print("Ha habido un error con los datos introducidos")


con = sql_connection()
#sql_Creartabla(con)
#sql_añadirCliente(con)
#sql_update(con)
#sql_select(con)
#sql_delete(con)
def error():
    print("Fatal Error")
def menu(con):
    decision=int(input("¿Que quieres hacer (Elija un numero del 1 al 5?\n"
                    "1-CREAR TABLA CLIENTES\n"
                    "2-AÑADIR UN CLIENTE\n"
                    "3-MODIFICAR UN CLIENTE\n"
                    "4-MOSTRAR LOS CLIENTES\n"
                    "5-BORRAR UN CLIENTE\n"))

    switch_metodos={
        1:sql_Creartabla,
        2:sql_añadirCliente,
        3:sql_update,
        4:sql_select,
        5:sql_delete
    }
    switch_metodos.get(decision, error)(con)

menu(con)