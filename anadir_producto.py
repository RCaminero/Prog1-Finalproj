from tkinter import *
import utilidades
import db_conection


class Ventana_anadir_producto:
    def __init__(self, root, my_treeview, articulos_var):
        self.articulos_var = articulos_var
        self.root = root
        self.my_treeview = my_treeview

        self.productos_por_categoria = {}
        self.my_db = db_conection.Db_connection('sistema')
        self.categorias = self.my_db.run_query('SELECT * FROM categorias').fetchall()
        self.productos = self.my_db.run_query('SELECT * FROM productos').fetchall()

        

        for categoria in self.categorias:
            self.productos_por_categoria[categoria[0]] = []
            
        for producto in self.productos:
            self.productos_por_categoria[producto[4]].append(producto)

        print(self.productos_por_categoria)

        self.cantidad = IntVar()

        self.ventana_de_anadir_producto = Toplevel(self.root)
        self.ventana_de_anadir_producto.title('Procesos')
        self.ventana_de_anadir_producto.geometry("750x600")
        self.ventana_de_anadir_producto.resizable(0, 0)
        utilidades.center(self.ventana_de_anadir_producto)
        Label(self.ventana_de_anadir_producto, text = 'Selecciona un producto', font = 'Arial 16 bold').grid(row = 0, column = 0, pady = (20, 0))
        self.campo = Frame(self.ventana_de_anadir_producto)
        self.campo.grid(row = 1, column = 0, columnspan =3, padx = (30, 0), pady = (15, 5))
        self.treeview = ttk.Treeview(self.campo, height = 15, style="mystyle.Treeview",selectmode='browse')
        self.treeview.pack(side = 'left')

        self.treeview.column("#0", width=680, anchor='c', minwidth = 100, stretch = False)

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.treeview.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.treeview.configure(yscrollcommand = self.verscrlbar.set)
        


        item = self.treeview.insert("", 'end', text="Elemento 1")
        self.treeview.insert(item, 'end', text="Subelemento 1")
        items = []

        for categoria in self.categorias:
            item = self.treeview.insert("", 'end', text=f"{categoria[1]}")
            for producto in self.productos_por_categoria[categoria[0]]:

                self.treeview.insert(item, 'end', text=f"{producto[1]}")
                
            items.append(item)
        print(items)

        Label(self.ventana_de_anadir_producto, text = 'Cantidad:', font = 'Arial 12').grid(row = 2, column = 0, sticky = 'e', padx = (0, 5))
        Entry(self.ventana_de_anadir_producto, font = 'Arial 11', textvariable = self.cantidad, width = 6).grid(row = 2, column = 1, sticky = 'w')
        Button(self.ventana_de_anadir_producto, text = 'Añadir', command = self.añadirProducto).grid(row = 3, column = 1)



        self.ventana_de_anadir_producto.grab_set()
        self.root.wait_window(self.ventana_de_anadir_producto)


    def añadirProducto(self):
        
        self.treeview.item(self.treeview.selection())['values']
        # except IndexError:
            # print('Por favor seleccione un producto')
            # return
        self.nombre = self.treeview.item(self.treeview.selection())['text']
        print(self.nombre)
        self.precio = self.my_db.run_query(f"SELECT producto_Precio FROM productos WHERE producto_Nombre LIKE '{self.nombre}'").fetchone()
        print(self.precio, type(self.precio))
        print(self.cantidad.get(), type(self.cantidad.get()))

        self.my_treeview.insert("",'end',text= f"{self.nombre}", values=(
            self.cantidad.get(),
            self.nombre,
            self.precio,
            (int(self.cantidad.get()) * float((self.precio[0]))
        )))
        self.cantidad_articulos.append(self.cantidad.get())
            
        self.articulos_var[self.nombre] = self.cantidad.get()


    def contar_articulos(self):
        # contar articulos
        contador = 0
        for num in self.cantidad_articulos:
            contador += num
        
        return contador

    def get_cant_articuos(self):
        pass