import db_conection
from tkinter import *
import utilidades

class Productos_Adm:
    def __init__(self, root, ventana_padre):
        self.root = root
        self.ventana_padre = ventana_padre
        #Conexion con base de Datos
        self.my_db = db_conection.Db_connection('sistema')
        self.lista_productos = self.my_db.run_query('SELECT * FROM productos').fetchall()
        self.lista_categorias = self.my_db.run_query('SELECT * FROM categorias').fetchall()
        self.mis_categorias = []
        

        self.nombre_var = StringVar()
        self.precio_var = DoubleVar()
        self.stock_var = IntVar()
        self.categoria_var = StringVar()
        # Marco de registro
        

        # Entrada de nombre por teclado
        Label(self.root, text = 'Nombre: ', font = 'Arial 11').grid(row = 1, column = 0, padx = (40,5))
        self.nombre = Entry(self.root, width = 65, font = 'Arial 11', textvariable = self.nombre_var)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1, padx = (20,10), pady = 10, sticky = 'w')

        #Entrada de precio por teclado
        Label(self.root, text = 'Precio: ', font = 'Arial 11').grid(row = 2, column = 0, padx = (40,5))
        self.precio = Entry(self.root, font = 'Arial 11', textvariable = self.precio_var)
        self.precio.grid(row = 2, column = 1, padx = (20,10), pady = 10, sticky = 'w')

        #Entrada de cantidad por teclado
        Label(self.root, text = 'Cantidad en Stock: ', font = 'Arial 11').grid(row = 3, column = 0, padx = (40,5))
        self.stock = Entry(self.root, font = 'Arial 11', textvariable = self.stock_var)
        self.stock.grid(row = 3, column = 1, padx = (20,10), pady = 10, sticky = 'w')

        
        Label(self.root, text = 'Categoria: ', font = 'Arial 11').grid(row = 4, column = 0, padx = (40,5))
        self.categoria = StringVar()
        self.selecciona_categoria = ttk.Combobox(self.root, width = 23, textvariable = self.categoria_var, state ='readonly', font = 'Arial 11')
        for self.categoria in self.lista_categorias:
            self.mis_categorias.append(self.categoria[1])
        print(self.mis_categorias)
        self.selecciona_categoria['values'] = self.mis_categorias#Sacar de la base de datos
        self.selecciona_categoria.grid(row = 4, column = 1, sticky = 'w')
        
        Button(self.root, text = "Añadir categoria", command = lambda: self.anadir_categoria(self.ventana_padre)).grid(row = 4, column = 1)
        # 

        # Boton añadir producto 
        Button(self.root, text = 'Guardar', font = 'Arial 9 bold', command = self.añadirProducto).grid(row = 5,column =  2, sticky = W + E, padx = 10, pady = 10)
        # 
        
        # Mensaje de salida 
        self.mensaje = Label(self.ventana_padre, text = '', fg = 'red')
        self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

        # Tabla
        self.campo = Frame(self.ventana_padre)
        self.campo.grid(row = 4, column = 0, columnspan =2, padx = (150, 0))
        self.tree = ttk.Treeview(self.campo, height = 10, columns = 4)
        self.tree.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.tree.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = self.verscrlbar.set)

        self.tree["columns"] = ("1", "2","3","4")
        self.tree['show'] = 'headings'

        self.tree.column("1", width=340, anchor='c', minwidth = 100, stretch = False)
        self.tree.column("2", width=130, anchor='c')
        self.tree.column("3", width=130, anchor='c')
        self.tree.column("4", width=200, anchor='c')

        self.tree.heading('1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('2', text = 'Precio', anchor = CENTER)
        self.tree.heading('3', text = 'Cantidad en Stock', anchor = CENTER)
        self.tree.heading('4', text = 'Categoria', anchor = CENTER)
        
        self.listar_productos()


        # Botones
        Button(self.ventana_padre, text = 'Eliminar',width = 40,  font = 'Arial 9 bold', command = self.borrarProducto).grid(row = 5, column = 1, sticky = 'w', padx = (0, 0), pady = (10,0))
        # ,
        Button(self.ventana_padre, text = 'EDITAR',width = 40,  font = 'Arial 9 bold', command = lambda: self.editarProducto(self.ventana_padre)).grid(row = 5, column = 1, sticky ='e', pady = (10,0))
        # ,

        
    def añadirProducto(self):
        self.id_categoria = self.my_db.run_query(f"SELECT * FROM categorias WHERE categoria_Nombre LIKE '{self.categoria_var.get()}'").fetchone()

        self.my_db.run_query(f"INSERT INTO productos VALUES (null, ?, ?, ?, ?)",(self.nombre_var.get(), self.precio_var.get(), self.stock_var.get(), self.id_categoria[0]))
        self.listar_productos()

    def listar_productos(self):
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        self.lista_productos = self.my_db.run_query("SELECT * FROM productos").fetchall()


        for self.producto in self.lista_productos:
            self.cate_name = self.my_db.run_query(f"SELECT categoria_Nombre FROM categorias WHERE categoria_ID = '{self.producto[4]}'").fetchone()
            
            self.tree.insert("",'end',text= f"{self.producto[1]}", values=(
                self.producto[1],
                self.producto[2],
                self.producto[3],
                self.cate_name
            ))

    def borrarProducto(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            print('Complete los campos')
            return

        nombre = self.tree.item(self.tree.selection())['text']
        print(nombre)
        self.my_db.run_query(f"DELETE FROM productos WHERE producto_Nombre IS '{nombre}'")
        
        print(f'El producto {nombre} se elimino correctamente')
        self.listar_productos()

    def anadir_categoria(self, ventana_de_mantenimiento):
        self.ventana_de_mantenimiento = ventana_de_mantenimiento
        self.anadir_categoria_window = Toplevel(self.ventana_de_mantenimiento)
        self.anadir_categoria_window.title = 'Añadir categoria'
        self.categoria_seleccionada = StringVar()
        self.marco = LabelFrame(self.anadir_categoria_window, text = 'Añadir categoria', font = 'Arial 12 bold')
        self.marco.pack(padx = 15, pady = 10)
        Label(self.marco, text = 'Nombre de la categoria:', font ='Arial 11').grid(row = 0, column = 0, padx = 10, pady = 15)
        self.categoria_a_anadir = Entry(self.marco, font = 'Arial 11', textvariable = self.categoria_seleccionada)
        self.categoria_a_anadir.grid(row = 0, column = 1, pady  = 15)

        Button(self.marco, text = 'Añadir Categoria', font = 'Arial 10', command = self.anadir).grid(row = 1, column = 1, pady = 5)


        utilidades.center(self.anadir_categoria_window)
        self.anadir_categoria_window.grab_set()
        self.ventana_de_mantenimiento.wait_window(self.anadir_categoria_window)
        self.anadir_categoria_window.mainloop()

    def anadir(self):
        self.dato = self.categoria_seleccionada.get()
        self.my_db.run_query(f"""
            INSERT INTO categorias VALUES (null, '{self.dato}')
        """)
        self.mis_categorias.append(self.dato)
        self.selecciona_categoria['values'] = self.mis_categorias
        self.categoria_seleccionada.set('')

    def editarProducto(self, ventana_de_mantenimiento):
        self.ventana_de_mantenimiento = ventana_de_mantenimiento
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError:
            print('Por favor seleccione un producto')
            return
        nombre = self.tree.item(self.tree.selection())['text']
        precio_viejo = self.tree.item(self.tree.selection())['values'][1]
        stock_viejo = self.tree.item(self.tree.selection())['values'][2]
        categoria_vieja = self.tree.item(self.tree.selection())['values'][3]
        self.edit_window = Toplevel(self.ventana_de_mantenimiento)
        self.edit_window.title = 'Editar producto'
        # Old Name
        Label(self.edit_window, text = 'Nombre Antiguo:', font = 'Arial 11').grid(row = 0, column = 1, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = nombre), state = 'readonly', font = 'Arial 11', width = 30).grid(row = 0, column = 2, padx = 5 , pady = 10, sticky = 'w')
        # New Name
        Label(self.edit_window, text = 'Nombre Nuevo:', font = 'Arial 11').grid(row = 1, column = 1, padx = 5, pady = 10)
        nombre_nuevo = Entry(self.edit_window, font = 'Arial 11')
        nombre_nuevo.grid(row = 1, column = 2, padx = 5, pady = 10, sticky = 'w')

        # Old Price 
        Label(self.edit_window, text = 'Precio Antiguo:', font = 'Arial 11').grid(row = 2, column = 1, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = precio_viejo), state = 'readonly', font = 'Arial 11').grid(row = 2, column = 2, padx = 5, pady = 10, sticky = 'w')
        # New Price
        Label(self.edit_window, text = 'Precio Nuevo:', font = 'Arial 11').grid(row = 3, column = 1, padx = 5, pady = 10)
        precio_nuevo= Entry(self.edit_window, font = 'Arial 11')
        precio_nuevo.grid(row = 3, column = 2, padx = 5, pady = 10, sticky = 'w')

        # Old stock 
        Label(self.edit_window, text = 'Stock Antiguo:', font = 'Arial 11').grid(row = 4, column = 1, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = stock_viejo), state = 'readonly', font = 'Arial 11').grid(row = 4, column = 2, padx = 5, pady = 10, sticky = 'w')
        # New Stock
        Label(self.edit_window, text = 'Stock Nuevo:', font = 'Arial 11').grid(row = 5, column = 1, padx = 5, pady = 10)
        stock_nuevo= Entry(self.edit_window, font = 'Arial 11')
        stock_nuevo.grid(row = 5, column = 2, padx = 5, pady = 10, sticky = 'w')

        # Old Categoria 
        Label(self.edit_window, text = 'Categoria Antigua:', font = 'Arial 11').grid(row = 6, column = 1, padx = 5, pady = 10, sticky = 'w')
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = categoria_vieja), state = 'readonly', font = 'Arial 11').grid(row = 6, column = 2, padx = 5, pady = 10, sticky = 'w')
        self.categoria_var1 = StringVar()
        self.categorias = self.my_db.run_query('SELECT * FROM categorias').fetchall()
        self.mis_categorias1 = []
        Label(self.edit_window, text = 'Categoria: ', font = 'Arial 11').grid(row = 7, column = 1)
        self.selecciona_categoria = ttk.Combobox(self.edit_window, width = 15, textvariable = self.categoria_var1, state ='readonly', font = 'Arial 11')
        for self.categoria in self.categorias:
            self.mis_categorias1.append(self.categoria[1])
        print(self.mis_categorias1)
        self.selecciona_categoria['values'] = tuple(self.mis_categorias1)#Sacar de la base de datos
        self.selecciona_categoria.grid(row = 7, column = 2, sticky = 'w', padx = 5, pady = 10)
        
        
        self.id_categoria_antigua = self.my_db.run_query(f"""SELECT * FROM categorias WHERE categoria_Nombre LIKE '{categoria_vieja}'""").fetchone()[0]


        Button(self.edit_window, text = 'Actualizar', command = lambda: self.edit_records(nombre_nuevo.get(), nombre, precio_nuevo.get(), precio_viejo, stock_nuevo.get(), stock_viejo, self.categoria_var1.get() , self.id_categoria_antigua)).grid(row = 8, column = 2, sticky = W, pady = 5)
        

        utilidades.center(self.edit_window)
        self.edit_window.grab_set()
        self.ventana_de_mantenimiento.wait_window(self.edit_window)
        self.edit_window.mainloop()
        
    def edit_records(self, nombre_nuevo, nombre_viejo, precio_nuevo, precio_viejo, stock_nuevo, stock_viejo, categoria_nueva, categoria_vieja):
        
        self.id_categoria1 = self.my_db.run_query(f"""SELECT * FROM categorias WHERE categoria_Nombre LIKE '{categoria_nueva}'""").fetchone()[0]
        print(self.id_categoria1)
        
        self.my_db.run_query('UPDATE productos SET producto_Nombre = ?, producto_Precio = ?, producto_Stock = ?, producto_ID_categoria = ? WHERE producto_Nombre = ? AND producto_Precio = ? AND producto_Stock = ? AND producto_ID_categoria = ?',(nombre_nuevo, precio_nuevo, stock_nuevo, self.id_categoria1, nombre_viejo, precio_viejo, stock_viejo, categoria_vieja))
        self.edit_window.destroy()
        print('El producto {} se actualizo correctamente'.format(nombre_viejo))
        self.listar_productos()