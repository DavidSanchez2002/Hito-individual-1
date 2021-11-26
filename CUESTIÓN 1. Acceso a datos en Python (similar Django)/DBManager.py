import sqlite3
from sqlite3 import Error

from matplotlib.pyplot import fill


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

    cursorObj.execute(f"INSERT INTO clientes ('nombre','apellidos','telefono') VALUES('{nombre}','{apellidos}','{telefono}')")
    con.commit()


def sql_update(con):
    resfiltro1=input("Introduzca el id del cliente que desea modificar\n")
    filtro2= input("¿Que quieres cambiar?\nnombre\nappellidos\ntelefono\n")
    resfiltro2=input(f"Introduce el nuevo\n")

    cursorObj = con.cursor()
    cursorObj.execute(f'UPDATE clientes SET {filtro2} = "{resfiltro2}" where id = {resfiltro1}')
    con.commit()

def sql_select(con):
    filtros=input("Introduzca las columnas que desea ver separadas por',' o si quiere ver todo introduzca '*'\n")
    condicion=input("¿Desea aplicar alguna condicion? escriba si o no")
    cursorObj = con.cursor()
    cursorObj.execute(f'SELECT {filtros} FROM clientes')

    [print(row) for row in cursorObj.fetchall()]

def sql_delete(con):
    filtro1=input("¿Porque columna desea filtrar su busqueda para el borrado?\nnombre\nappellidos\ntelefono\n")
    resfiltro1=input(f"Borrar filas que su {filtro1} sea =  ")

    cursorObj = con.cursor()

    print("Va a eliminar estos clientes: ")
    cursorObj.execute(f"SELECT * FROM clientes where {filtro1} = '{resfiltro1}'")
    [print(row) for row in cursorObj.fetchall()]
    seguro=input("¿Esta usted seguro? s/n")

    if(seguro=="s"):
        cursorObj.execute(f"DELETE FROM clientes where {filtro1} = '{resfiltro1}'")
        con.commit()



con = sql_connection()
#sql_Creartabla(con)
#sql_añadirCliente(con)
#sql_update(con)
#sql_select(con)
sql_delete(con)