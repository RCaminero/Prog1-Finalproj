from tkinter import *
import utilidades
from tkinter import ttk
import db_conection
import time

class Ventana_Consulta_Factura_xFecha:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consulta_factura_xfecha = Toplevel(self.root)
        self.ventana_de_consulta_factura_xfecha.title('Consulta Facturas x Fecha')
        self.ventana_de_consulta_factura_xfecha.geometry("920x580")
        self.ventana_de_consulta_factura_xfecha.resizable(0, 0)
        utilidades.center(self.ventana_de_consulta_factura_xfecha)
        self.my_db = db_conection.Db_connection('sistema')


        self.lista_de_facturas = self.my_db.run_query("SELECT * FROM facturas").fetchall()

        

        self.fecha_consultar = StringVar()
        
        self.my_frame = LabelFrame(self.ventana_de_consulta_factura_xfecha, text = 'Consultar Facturas x Fecha')
        self.my_frame.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx = 15)

        Label(self.my_frame, text = 'Fecha a consultar', font = "Arial 12").grid(row = 0, column = 0)
        Entry(self.my_frame, font = 'Arial 12', textvariable = self.fecha_consultar).grid(row = 0, column =1)
        Button(self.my_frame, text = 'Buscar', font = 'Arial 12', command = self.buscar_facturas).grid(row = 0 , column = 2)
        Button(self.my_frame, text = 'Todas las facturas', font = 'Arial 12', command = lambda : self.listar_facturas(self.lista_de_facturas)).grid(row = 1 , column = 0, pady =25)
        self.fecha_consultar.set(time.strftime('%d/%m/%Y'))

        Button(self.ventana_de_consulta_factura_xfecha, text = 'Ver Factura', font = 'Arial 12', command = self.mostrar_factura).grid(row = 2 , column = 0, pady =25)
        # Tabla
        self.campo = Frame(self.ventana_de_consulta_factura_xfecha)
        self.campo.grid(row = 3, column = 0, columnspan =4, padx = (40, 5), pady = (15, 5))
        self.tree = ttk.Treeview(self.campo, height = 10, columns = 4, style="mystyle.Treeview")
        self.tree.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.tree.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = self.verscrlbar.set)

        self.tree["columns"] = ("1", "2","3","4","5")
        self.tree['show'] = 'headings'

        self.tree.column("1", width=110, anchor='c', minwidth = 100, stretch = False)
        self.tree.column("2", width=270, anchor='c')
        self.tree.column("3", width=170, anchor='c')
        self.tree.column("4", width=150, anchor='c')
        self.tree.column("5", width=130, anchor='c')

        self.tree.heading('1', text = 'No Factura', anchor = CENTER)
        self.tree.heading('2', text = 'Cliente', anchor = CENTER)
        self.tree.heading('3', text = 'Fecha - Hora', anchor = CENTER)
        self.tree.heading('4', text = 'Vendedor', anchor = CENTER)
        self.tree.heading('5', text = 'Total', anchor = CENTER)
        

        self.listar_facturas(self.lista_de_facturas)


        self.ventana_de_consulta_factura_xfecha.grab_set()
        self.root.wait_window(self.ventana_de_consulta_factura_xfecha)
        


    def listar_facturas(self, listado):
        self.listado = listado
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        for self.factura in self.listado:
            print('hoo',self.factura)
            # self.cate_name = self.my_db.run_query(f"SELECT categoria_Nombre FROM categorias WHERE categoria_ID = '{self.cliente[4]}'").fetchone()
            self.cliente = self.my_db.run_query(f"SELECT cliente_Nombre FROM clientes WHERE cliente_ID = '{self.factura[1]}'").fetchone()[0]
            vendedor = self.my_db.run_query(f"SELECT Empleado_nombre FROM empleados WHERE Empleado_Id = '{self.factura[4]}'").fetchone()[0]
            detalle = self.my_db.run_query(f"SELECT * FROM detalle_factura WHERE detalle_NO_Factura = '{self.factura[0]}'").fetchall()
            self.count = 0
            for detail in detalle:
                self.count += float(detail[4])

            
            self.tree.insert("",'end',text= f"{self.factura[0]}", values=(
                self.factura[0],
                self.cliente,
                f'{self.factura[2] + " - " + self.factura[3]}',
                vendedor,
                self.count,
            ))

    def buscar_facturas(self):
        query = f"SELECT * FROM facturas WHERE factura_Fecha LIKE '{self.fecha_consultar.get()}'"
        
        self.facturas_buscadas = self.my_db.run_query(query).fetchall()
        print(self.facturas_buscadas)
        
        self.listar_facturas(self.facturas_buscadas)
    
    def mostrar_factura(self):   
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            print('Complete los campos')
            return

        self.no_factura = self.tree.item(self.tree.selection())['values'][0]


        self.ventana_ver_factura = Toplevel(self.ventana_de_consulta_factura_xfecha)
        self.ventana_ver_factura.title(f'Factura: {self.no_factura} -' + f'Cliente: {self.cliente}') 
        Label(self.ventana_ver_factura, text = f'No. Factura: {self.no_factura}', font = "Arial 16 bold").grid(row = 0, column = 0)
        Label(self.ventana_ver_factura, text = f'Cliente: {self.cliente}', font =' Arial 16').grid(row = 1, column = 0)
        Label(self.ventana_ver_factura, text = f'{self.factura[2] + " - " + self.factura[3]}', font =' Arial 16').grid(row = 0, column = 1)

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

        self.listar_productos()

        Label(self.ventana_ver_factura, text = f"Total: {self.count}", font = "Arial 14").grid(row = 3, column = 0)

        utilidades.center(self.ventana_ver_factura)
        self.ventana_ver_factura.grab_set()
        self.ventana_de_consulta_factura_xfecha.wait_window(self.ventana_ver_factura)

    def listar_productos(self):
        # Limpiar tabla
        self.records = self.treeview.get_children()
        for elemento in self.records:
            self.treeview.delete(elemento)

        self.lista_detalle = self.my_db.run_query(f"SELECT * FROM detalle_factura WHERE detalle_NO_Factura = '{self.no_factura}'").fetchall()
        print(self.lista_detalle)
        for self.producto in self.lista_detalle:
            print(self.producto[1])
            producto = self.my_db.run_query(f"SELECT producto_Nombre FROM productos WHERE producto_ID = '{self.producto[2]}'").fetchall()[0][0]
            producto_precio = self.my_db.run_query(f"SELECT producto_Precio FROM productos WHERE producto_ID = '{self.producto[2]}'").fetchall()[0]
            print('producto', producto)
            self.treeview.insert("",'end',text= f"{self.producto[1]}", values=(
                self.producto[3],
                producto,
                producto_precio,
                self.producto[4],
            ))

   