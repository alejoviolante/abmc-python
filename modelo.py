import sqlite3
import re
from modelo_regex import ModuloRegex
from decorador_log import *
from observador import Subject

class BaseDeDatos(Subject):

    def __init__(self,):
        super().__init__() ##
        self.crear_base()
        self.crear_tabla()
        self.filtro = ModuloRegex()
        

    def crear_base(self,):
        base = sqlite3.connect("base_de_datos.db")
        return base
    def crear_tabla(self,):
        base = self.crear_base()
        cursor=base.cursor()
        sql= "CREATE TABLE IF NOT EXISTS inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, producto text, cantidad text, precio text)"
        cursor.execute(sql)
        base.commit()
        print("tabla creada")
    
    
    def alta_sin_filtro(self,producto, cantidad, precio):
        print("ejecutando alta")
        filtro = self.filtro.filtrar()
        if re.match(filtro, producto) == None:
            return 
        else:
            print("filtro aprobado")
            return self.alta(producto, cantidad, precio)

    @registro_log
    def alta(self,producto, cantidad, precio):
        funcion = "Alta"
        print("ejecutando alta con filtro")
        base = self.crear_base()
        cursor = base.cursor()
        data = (producto, cantidad, precio)
        sql = "INSERT INTO inventario(producto, cantidad ,precio) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        base.commit()
        print("producto cargado")
        self.notificar(funcion)
        return "producto_si"
    

        



    @registro_log
    def baja(self,tree):
        base = self.crear_base()
        cursor=base.cursor()
        funcion = "Baja"
        data = (tree,)
        sql = "DELETE FROM inventario WHERE id = ?;"
        cursor.execute(sql, data)
        base.commit()
        self.notificar(funcion)
        print("borrando producto")

    @registro_log
    def modificar(self,producto, cantidad, precio, item_id):
        base = self.crear_base()
        cursor=base.cursor()
        funcion = "Modificar"
        data = (producto, cantidad, precio,item_id)
        sql = "UPDATE inventario SET producto=?, cantidad=?, precio=? WHERE id =? "
        cursor.execute(sql,data)
        base.commit()
        self.notificar(funcion)
        print("producto N°id= ", item_id, " modificado")



    def listar(self,):
            sql = "SELECT * FROM inventario ORDER BY id ASC"
            base=self.crear_base()
            cursor = base.cursor()
            datos=cursor.execute(sql)
            base_datos= datos.fetchall()
            print("tree actualizado")
            return base_datos

