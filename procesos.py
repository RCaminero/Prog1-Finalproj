from tkinter import *
import utilidades
from tkinter import ttk
import db_conection
import menu
import time
import anadir_producto
import anadir_producto2
from tkinter import messagebox as MessageBox

class Ventana_Procesos:
    def __init__(self, root, vendedor):
        self.root = root
        self.vendedor = vendedor
        self.ventana_de_procesos = Toplevel(self.root)
        self.ventana_de_procesos.title('Procesos')
        self.ventana_de_procesos.geometry("1030x600")
        self.ventana_de_procesos.resizable(0, 0)
        utilidades.center(self.ventana_de_procesos)

        #conexion base de datos
        self.my_db = db_conection.Db_connection('sistema')
        self.cantidad_articulos = IntVar()
        self.subtotal = DoubleVar()
        self.itbis = DoubleVar()
        self.total_pagar = DoubleVar()
        self.info_factura()

        self.cantidades_articulos = []
        self.precios_de_articulos = []



        self.productos_venta = []

        self.lista_productos = self.my_db.run_query('SELECT * FROM productos').fetchall()
        self.lista_categorias = self.my_db.run_query('SELECT * FROM categorias').fetchall()

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 12)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Arial', 12,'bold')) # Modify the font of the headings
        

        #Variables
        self.cliente = StringVar()
        self.lista_de_clientes = self.my_db.run_query("SELECT * FROM clientes").fetchall()
        print(self.lista_de_clientes)


        #menubar
        menu.Menubar_factura(self.ventana_de_procesos, self.añadir_producto, self.edit_window, self.borrar_producto, self.realizar_venta)

        #Barra superior
        self.barra_superior = Frame(self.ventana_de_procesos, bg = 'steel blue')
        self.barra_superior.grid(row = 0, column = 0, columnspan = 5, sticky = 'w') 
        
        #Label Cliente
        Label(self.barra_superior, text = 'Cliente:', font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 0, column = 0, padx = (10, 5), pady = (15,5))
        Label(self.barra_superior, text = '           ', font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 0, column = 2, padx = (10, 5), pady = (15,5))
        Label(self.barra_superior, text = '            ', font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 0, column = 3, padx = (10, 5), pady = (15,5))
        Label(self.barra_superior, text = '            ', font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 0, column = 4, padx = (10, 5), pady = (15,5))

        #Combo-box selecciona cliente
        self.selecciona_cliente = ttk.Combobox(self.barra_superior, width = 30, textvariable = self.cliente, state ='readonly', font = 'Arial 14')
        self.mis_clientes = []
        for cliente in self.lista_de_clientes:
            self.mis_clientes.append(cliente[1]) 
        self.selecciona_cliente['values'] = self.mis_clientes
        self.selecciona_cliente.grid(row = 0, column = 1, sticky = 'w', padx = (5, 10), pady = (15, 5))
        
        #no factura
        Label(self.barra_superior, text = f'Fac No: {self.no_factura + 1}', font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 2, column = 0, padx = (10, 5))
        

        #Hora y fecha
        self.fecha_Hora = Label(self.barra_superior, text = '', font = 'Arial 14', bg= 'steel blue', fg = 'white')
        self.fecha_Hora.grid(row = 0 , column = 5, sticky = 'e', pady = (15,5))
        self.times()

        #nombre vendedor
        Label(self.barra_superior, text = self.vendedor[1][3], font = 'Arial 14', bg= 'steel blue', fg = 'white').grid(row = 1, column = 5)
        
        #label detalle Factura
        Label(self.ventana_de_procesos, text = 'Detalle de Factura', font = 'Arial 16').grid(row = 1, column = 0, pady = (20, 0), columnspan = 4, sticky = 'n')

        # Tabla
        self.campo = Frame(self.ventana_de_procesos)
        self.campo.grid(row = 2, column = 0, columnspan =4, padx = (40, 5), pady = (15, 5))
        self.tree = ttk.Treeview(self.campo, height = 10, columns = 4, style="mystyle.Treeview")
        self.tree.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.tree.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = self.verscrlbar.set)

        self.tree["columns"] = ("1", "2","3","4")
        self.tree['show'] = 'headings'

        self.tree.column("1", width=110, anchor='c', minwidth = 100, stretch = False)
        self.tree.column("2", width=370, anchor='c')
        self.tree.column("3", width=140, anchor='c')
        self.tree.column("4", width=200, anchor='c')

        self.tree.heading('1', text = 'Cantidad', anchor = CENTER)
        self.tree.heading('2', text = 'Producto', anchor = CENTER)
        self.tree.heading('3', text = 'Precio Unitario', anchor = CENTER)
        self.tree.heading('4', text = 'Total', anchor = CENTER)
        

        self.botones = Frame(self.ventana_de_procesos)
        self.botones.grid(row = 2, column = 4)
        Button(self.botones, text = 'Añadir', font = 'Arial 12 bold', command = self.añadir_producto).grid(row = 0, column = 0, pady = (0, 25))
        Button(self.botones, text = 'Editar', font = 'Arial 12 bold', command = self.edit_window).grid(row = 1, column = 0, pady = (0, 25))
        Button(self.botones, text = 'Eliminar', font = 'Arial 12 bold', command = self.borrar_producto).grid(row = 2, column = 0, pady = (0, 25))

        Label(self.ventana_de_procesos, text = f'Articulos: ', font = 'Arial 14').grid(row = 3, column =0,sticky = 'w', padx = (40, 0))
        Label(self.ventana_de_procesos, textvariable = self.cantidad_articulos, font = 'Arial 14').grid(row = 3, column = 0 , padx = (40, 0))
        Label(self.ventana_de_procesos, text = 'Subtotal: ', font = 'Arial 14').grid(row = 3, column =3)
        Label(self.ventana_de_procesos, textvariable = self.subtotal, font = 'Arial 14').grid(row = 3, column =3, sticky = 'e')
        Label(self.ventana_de_procesos, text = 'ITBIS: ', font = 'Arial 14').grid(row = 4, column =3)
        Label(self.ventana_de_procesos, textvariable = self.itbis, font = 'Arial 14').grid(row = 4, column =3 , sticky = 'e')
        Label(self.ventana_de_procesos, text = 'Total a pagar: ', font = 'Arial 14').grid(row = 5, column =3)
        Label(self.ventana_de_procesos, textvariable = self.total_pagar, font = 'Arial 14').grid(row = 5, column =3, sticky = 'e')
        Button(self.ventana_de_procesos, text = 'VENDER', font = 'Arial 16 bold', command = self.realizar_venta).grid(row = 4, column = 4, pady = (0, 25), rowspan = 2)

        self.listar_productos()

        self.ventana_de_procesos.grab_set()
        self.root.wait_window(self.ventana_de_procesos)

        

    def times(self):
        tiempo_actual = time.strftime(' %H:%M:%S - %A %d %B %Y ')
        self.fecha_Hora.config(text = tiempo_actual)
        self.fecha_Hora.after(200, lambda : self.times())

    # def añadirProducto(self):
    #     self.listar_productos()

    def listar_productos(self):
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        # self.lista_productos = self.my_db.run_query("SELECT * FROM productos").fetchall()

        for self.producto in self.productos_venta:
            self.tree.insert("",'end',text= f"{self.producto[1]}", values=(
                self.producto[0],
                self.producto[1],
                self.producto[2],
                self.producto[3],
            ))
            

        self.cantidad_articulos.set(self.contar_articulos())
        self.subtotal.set(self.contar_precios())
        self.itbis.set(round(self.subtotal.get() * 0.18, 2))
        self.total_pagar.set(self.subtotal.get() + self.itbis.get())
            
            
            
       
    def añadir_producto(self):
        # self.anadir = anadir_producto.Ventana_anadir_producto(self.ventana_de_procesos, self.tree, self.cantidad_articulos)
        # anadir_producto2.ventana(self.ventana_de_procesos, self.tree, self.cantidad_articulos, self.subtotal, self.cantidades_articulos, self.precios_de_articulos)
        self.ventana_anadir()
        print(self.cantidad_articulos)

    def info_factura(self):
        self.no_factura = self.my_db.run_query("SELECT * FROM facturas ORDER BY factura_No DESC LIMIT 1").fetchone()[0]
        
        print(self.no_factura + 1)
        
    def ventana_anadir(self):
        # self.my_treeview = my_treeview

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

        self.ventana_de_anadir_producto = Toplevel(self.ventana_de_procesos)
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
        self.ventana_de_procesos.wait_window(self.ventana_de_anadir_producto)


    def añadirProducto(self):
        try:
            self.treeview.item(self.treeview.selection())['text']
        except IndexError:
            MessageBox.showwarning("No se ha seleccionado producto", "Primero debes de seleccionar un producto para añadir")
            return

            # return
        self.nombre = self.treeview.item(self.treeview.selection())['text']
        
        print(self.nombre)
        self.precio = self.my_db.run_query(f"SELECT producto_Precio FROM productos WHERE producto_Nombre LIKE '{self.nombre}'").fetchone()
        print(self.precio, type(self.precio))
        try:    
            float(self.cantidad.get())
        except:
            MessageBox.showwarning("La cantidad tiene que ser un numero", "La cantidad introducida tiene que ser un numero")
            return
        print(self.cantidad.get(), type(self.cantidad.get()))
        if [self.cantidad.get(), self.nombre, str(self.precio[0]), str((int(self.cantidad.get()) * float((self.precio[0]))))] in self.productos_venta:
            MessageBox.showwarning("El producto ya se encuentra facturado", "El producto ya se encuentra facturado")
            return
        try:
            self.productos_venta.append([self.cantidad.get(), self.nombre, str(self.precio[0]), str((int(self.cantidad.get()) * float((self.precio[0]))))])
        except:
            MessageBox.showwarning("No se ha seleccionado producto", "Primero debes de seleccionar un producto para añadir")
            return
        
        if self.cantidad.get() < 1:
            MessageBox.showwarning("Cantidad tiene que ser mayor de 0", "La cantidad no puede ser 0 o menor.")
            return
        
        self.listar_productos()
        # self.tree.insert("",'end',text= f"{self.nombre}", values=(
        #     self.cantidad.get(),
        #     self.nombre,
        #     self.precio,
        #     (int(self.cantidad.get()) * float((self.precio[0]))
        # )))
        print(self.precio)


        
        
        
    


    def contar_articulos(self):
        # contar articulos
        contador = 0
        for producto in self.productos_venta:
            contador += int(producto[0])
        
        return contador
    
    def contar_precios(self):
        contador = 0
        for producto in self.productos_venta:
            contador += float(producto[3])
    
        return contador



    #edit window
    def edit_window(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            MessageBox.showwarning("No se ha seleccionado producto", "Primero debes de seleccionar un producto antes de editarlo")
            return
        self.ventana_editar = Toplevel(self.ventana_de_procesos)
        self.ventana_editar.title('Editar cantidad')
        self.cantidad_editada_var = IntVar()
        
        Label(self.ventana_editar, text = 'Nueva Cantidad').grid(row = 0, column = 0, padx = (15,5), pady = (20,20))
        cantidad_editada = Entry(self.ventana_editar, textvariable = self.cantidad_editada_var).grid(row = 0, column = 1, padx = (5,5), pady = (20,20))
        Button(self.ventana_editar, text = 'Editar Cantidad', command = self.editar).grid(row = 0, column = 2, padx = (5, 15), pady = (20,20))

        utilidades.center(self.ventana_editar)

    def editar(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            MessageBox.showwarning("No se ha seleccionado producto", "Primero debes de seleccionar un producto antes de editarlo")
            return
        if self.cantidad_editada_var.get() < 1:
            MessageBox.showwarning("La cantidad no puede ser 0 o menor", "La cantidad a editar no puede ser 0 o menor")
            return
        indice =  self.productos_venta.index(self.tree.item(self.tree.selection())['values'])
        self.productos_venta[indice][0] = self.cantidad_editada_var.get()
        self.productos_venta[indice][3] = str(int(self.productos_venta[indice][0]) * float(self.productos_venta[indice][2]))
        
        print(self.tree.item(self.tree.selection()))


        self.listar_productos()
        self.ventana_editar.destroy()
        # demas = self.tree.item(self.tree.selection())['values'][1:]
        # self.tree.item(self.tree.selection(), values= [self.cantidad_editada_var.get()] + demas)
        # cantidade = self.tree.item(self.tree.selection())['values']
        # print('mio',cantidade)

        # self.cantidades_articulos.append(self.cantidad.get())
        # self.precios_de_articulos.append(int(self.cantidad.get()) * float((self.precio[0])))
        
        # self.cantidad_articulos.set(self.contar_articulos())
        # self.subtotal.set(self.contar_precios())
        # self.itbis.set(round(self.subtotal.get() * 0.18, 2))
        # self.total_pagar.set(self.subtotal.get() + self.itbis.get())

    def borrar_producto(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            MessageBox.showwarning("Debe Seleccionar un producto", "Primero debes seleccionar un producto antes de borrarlo")
            return

        indice =  self.productos_venta.index(self.tree.item(self.tree.selection())['values'])
        
        print(f'El producto {self.productos_venta.pop(indice)[1]} se elimino correctamente')
        self.listar_productos()

    def realizar_venta(self):
        if self.cliente.get() != '':
            self.cliente_name = self.cliente.get()
            self.cliente_id = self.my_db.run_query(f"SELECT cliente_ID FROM clientes WHERE cliente_Nombre LIKE '{self.cliente_name}'").fetchone()[0]
            self.factura_fecha = time.strftime('%d/%m/%Y')
            self.factura_hora = time.strftime("%H:%M:%S")
            self.factura_id_vendedor = self.vendedor[1][0]
            self.my_db.db_close()
            self.my_db = db_conection.Db_connection('sistema')


            self.my_db.run_query(f"INSERT INTO facturas VALUES (null, ?, ?, ?, ?, ?, ?, ?)", (self.cliente_id, self.factura_fecha, self.factura_hora, self.factura_id_vendedor,0,0,0))

            self.factura_no = self.no_factura + 1
            for producto in self.productos_venta:
                producto_id = self.my_db.run_query(f"SELECT producto_ID FROM productos WHERE producto_Nombre LIKE '{producto[1]}'").fetchone()[0]
                producto_cantidad = producto[0]
                
                precio_total = float(producto[3]) + (float(producto[3]) * 0.18)
                
                self.my_db.run_query(f"INSERT INTO detalle_factura VALUES (null, ?, ?, ?, ?, ?)", (self.factura_no, producto_id, producto_cantidad, precio_total, 0))

            print('factura id vendedor', self.factura_id_vendedor)

            self.show_venta()

            self.productos_venta = []
            self.no_factura = self.no_factura + 1
            self.listar_productos()
        else:
            MessageBox.showwarning("No se Selecciono cliente", "Primero Tienes que seleccionar un cliente.")

    def show_venta(self):
        self.ventana_ver_factura = Toplevel(self.ventana_de_procesos)
        self.ventana_ver_factura.title(f'Factura: {self.no_factura + 1} -' + f'Cliente: {self.cliente_name}') 
        Label(self.ventana_ver_factura, text = f'No. Factura: {self.no_factura + 1}', font = "Arial 16 bold").grid(row = 0, column = 0)
        Label(self.ventana_ver_factura, text = f'Cliente: {self.cliente_name}', font =' Arial 16').grid(row = 1, column = 0)
        Label(self.ventana_ver_factura, text = f'{self.factura_fecha + " - " + self.factura_hora}', font =' Arial 16').grid(row = 0, column = 1)

        # Tabla
        self.campo = Frame(self.ventana_ver_factura)
        self.campo.grid(row = 2, column = 0, columnspan =4, padx = (40, 5), pady = (15, 5))
        self.treeview = ttk.Treeview(self.campo, height = 10, columns = 4, style="mystyle.Treeview")
        self.treeview.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.treeview.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.treeview.configure(yscrollcommand = self.verscrlbar.set)

        self.treeview["columns"] = ("1", "2","3","4")
        self.treeview['show'] = 'headings'

        self.treeview.column("1", width=110, anchor='c', minwidth = 100, stretch = False)
        self.treeview.column("2", width=370, anchor='c')
        self.treeview.column("3", width=140, anchor='c')
        self.treeview.column("4", width=200, anchor='c')

        self.treeview.heading('1', text = 'Cantidad', anchor = CENTER)
        self.treeview.heading('2', text = 'Producto', anchor = CENTER)
        self.treeview.heading('3', text = 'Precio Unitario', anchor = CENTER)
        self.treeview.heading('4', text = 'Total', anchor = CENTER)

        self.listar_productos2()

        Label(self.ventana_ver_factura, text = 'Subtotal: ', font = 'Arial 14').grid(row = 3, column =2)
        Label(self.ventana_ver_factura, textvariable = self.subtotal, font = 'Arial 14').grid(row = 3, column =3, sticky = 'e')
        Label(self.ventana_ver_factura, text = 'ITBIS: ', font = 'Arial 14').grid(row = 4, column =2)
        Label(self.ventana_ver_factura, textvariable = self.itbis, font = 'Arial 14').grid(row = 4, column =3 , sticky = 'e')
        Label(self.ventana_ver_factura, text = 'Total a pagar: ', font = 'Arial 14').grid(row = 5, column =2)
        Label(self.ventana_ver_factura, textvariable = self.total_pagar, font = 'Arial 14').grid(row = 5, column =3, sticky = 'e')

        utilidades.center(self.ventana_ver_factura)
        self.ventana_ver_factura.grab_set()
        self.ventana_de_procesos.wait_window(self.ventana_ver_factura)

    def listar_productos2(self):
        # Limpiar tabla
        self.records = self.treeview.get_children()
        for elemento in self.records:
            self.treeview.delete(elemento)

        # self.lista_productos = self.my_db.run_query("SELECT * FROM productos").fetchall()

        for self.producto in self.productos_venta:
            self.treeview.insert("",'end',text= f"{self.producto[1]}", values=(
                self.producto[0],
                self.producto[1],
                self.producto[2],
                self.producto[3],
            ))