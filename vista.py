from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from modelo import BaseDeDatos
class InterfazGrafica():
    
    def __init__(self,ventana):
        self.root = ventana
        self.base=BaseDeDatos()
        self.root.title("Proyecto Final")

        #TK carteles
        self.portada_cartel = Label(self.root,text="Sistema de stock para comercios",background="#81B3FF",width=100)
        self.portada_cartel.grid(row=0,columnspan=4)

        self.producto_cartel = Label(self.root, text = "Producto",width=15,height=2,anchor="e")
        self.producto_cartel.grid(row=2,column=0)

        self.cantidad_cartel = Label(self.root, text = "Cantidad",width=15,height=2,anchor="e")
        self.cantidad_cartel.grid(row=3,column=0)

        self.precio_cartel = Label(self.root, text = "Precio",width=15,height=2,anchor="e")
        self.precio_cartel.grid(row=4,column=0)

        #TK textarea

        self.producto_ingr = StringVar()
        self.cantidad_ingr = IntVar()
        self.precio_ingr = IntVar()

        self.producto_text = Entry(self.root, textvariable=self.producto_ingr,width=30)
        self.producto_text.grid(row=2,column=1,columnspan=2)

        self.cantidad_text = Entry(self.root, textvariable=self.cantidad_ingr,width=30)
        self.cantidad_text.grid(row=3,column=1,columnspan=2)

        self.precio_text = Entry(self.root, textvariable=self.precio_ingr,width=30)
        self.precio_text.grid(row=4,column=1,columnspan=2)
        #TK boton

        self.boton_agregar = Button(self.root, text="Agregar -->",activebackground="#A7A7A7",command=lambda:self.alta_vista(self.producto_ingr.get(),self.cantidad_ingr.get(),self.precio_ingr.get(), self.tree))
        self.boton_agregar.grid(row=5,column=2)

        self.boton_borrar =Button(self.root, text="borrar", command=lambda:self.baja_vista(self.tree),bg="#FA6954",activebackground="#BB3030",width=10)
        self.boton_borrar.grid(row=5,column=1)

        self.boton_modificar = Button(self.root, text="Modificar",activebackground="#A7A7A7", command=lambda:self.modificar_vista(self.producto_ingr.get(),self.cantidad_ingr.get(),self.precio_ingr.get(), self.tree))
        self.boton_modificar.grid(row=3,column=3,)

        self.boton_listar = Button(self.root, text="Cargar Sistema",command=lambda:self.listar_vista(self.tree),bg="#7BFA61",activebackground="#25A13A",width=30)
        self.boton_listar.grid(row=1,column=1,columnspan=2)

        #TK Treeview

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"]=("column_producto", "column_cantidad", "column_precio")
        self.tree.column("#0", width=50)
        self.tree.heading("#0", text="ID")
        self.tree.column("column_producto", width=200)
        self.tree.heading("column_producto", text="Producto")
        self.tree.column("column_cantidad", width=200)
        self.tree.heading("column_cantidad", text="cantidad")
        self.tree.column("column_precio", width=200)
        self.tree.heading("column_precio", text="precio")
        self.tree.grid(row=20, column=0, columnspan=4)


    def alta_vista(self,producto,cantidad,precio,tree):
        retorno = self.base.alta_sin_filtro(producto,cantidad,precio)

        if retorno == "producto_si":
            self.listar_vista(self.tree)
            self.producto_ingr.set("")
            self.cantidad_ingr.set("0")
            self.precio_ingr.set("0")
            showinfo ("Evento realizado","Producto cargado")
        else:
            showerror("Error al cargar", "El producto no puede comenzar con numeros ni caracteres especiales")

    def baja_vista(self,tree):
        valor = tree.selection()
        item = tree.item(valor)
        item_id = item['text']
        self.base.baja(item_id)
        tree.delete(valor)
        print("producto" , item_id , "borrado")
        self.listar_vista(tree)
        showinfo ("Evento realizado","Producto borrado")


    def modificar_vista(self,producto, cantidad, precio, tree):
        valor = tree.selection()
        item = tree.item(valor)
        item_id = item['text']
        if item_id:
            self.base.modificar(producto, cantidad, precio, item_id)
            self.listar_vista(tree)
            showinfo ("Evento realizado","Producto modificado")

    def listar_vista(self,tree_lista):
        lista = tree_lista.get_children()
        retorno = self.base.listar()
        for x in lista:
            self.tree.delete(x)
        for x in retorno:
            self.tree.insert("", 0, text=x[0], values=(x[1], x[2], x[3]))


"""if __name__ == "__main__":
    root = Tk()
    aplicacion = InterfazGrafica(root)
    root.mainloop()"""