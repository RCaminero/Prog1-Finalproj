from tkinter import *
import utilidades
from tkinter import ttk
import db_conection

class Ventana_Consulta_Producto:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consulta_producto = Toplevel(self.root)
        self.ventana_de_consulta_producto.title('Consulta Productos')
        self.ventana_de_consulta_producto.geometry("1100x600")
        self.ventana_de_consulta_producto.resizable(0, 0)
        utilidades.center(self.ventana_de_consulta_producto)

        self.my_db = db_conection.Db_connection('sistema')


        self.categoria_var = StringVar()
        
        self.lista_productos = self.my_db.run_query('SELECT * FROM productos').fetchall()
        self.lista_categorias = self.my_db.run_query('SELECT * FROM categorias').fetchall()


        self.my_frame = LabelFrame(self.ventana_de_consulta_producto, text = 'Consultar Productos', font = 'Arial 14 bold')
        self.my_frame.grid(row = 0, column = 0, columnspan = 6, pady = 10, padx = 15)



        Label(self.my_frame, text = 'Categoria: ', font = 'Arial 11').grid(row = 0, column = 0, padx = (10,5))
        
        self.categoria = StringVar()
        self.mis_categorias = []
        
        self.selecciona_categoria = ttk.Combobox(self.my_frame, width = 23, textvariable = self.categoria_var, state ='readonly', font = 'Arial 11')
        for self.categoria in self.lista_categorias:
            self.mis_categorias.append(self.categoria[1])
        print(self.mis_categorias)
        self.selecciona_categoria['values'] = self.mis_categorias#Sacar de la base de datos
        self.selecciona_categoria.grid(row = 0, column = 1, sticky = 'w')
        
        Button(self.my_frame, text = "Buscar Categoría", font = 'Arial 12', command = self.buscar_producto).grid(row = 0, column = 2)
        Button(self.my_frame, text = 'Todos las categorías', font = 'Arial 12', command = lambda: self.listar_productos(self.lista_productos)).grid(row = 1 , column = 0, pady =25)
        


        # Tabla
        self.campo = Frame(self.ventana_de_consulta_producto)
        self.campo.grid(row = 1, column = 0, columnspan =3, padx = (150, 0))
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
        
        self.listar_productos(self.lista_productos)
    

        self.ventana_de_consulta_producto.grab_set()
        self.root.wait_window(self.ventana_de_consulta_producto)

    
    def listar_productos(self, listado):
        self.listado = listado
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)


        for self.producto in self.listado:
            self.cate_name = self.my_db.run_query(f"SELECT categoria_Nombre FROM categorias WHERE categoria_ID LIKE {self.producto[4]}").fetchone()
            
            self.tree.insert("",'end',text= f"{self.producto[1]}", values=(
                self.producto[1],
                self.producto[2],
                self.producto[3],
                self.cate_name
            ))
        

    def buscar_producto(self):
        categoria = self.categoria_var.get()
        id_categoria = self.my_db.run_query(f"SELECT categoria_ID FROM categorias WHERE categoria_Nombre LIKE '{categoria}'").fetchone()
        print(id_categoria)
        query = f"SELECT * FROM productos WHERE producto_ID_categoria LIKE {id_categoria[0]}"
        self.my_db = db_conection.Db_connection('sistema')
        self.producto_buscado = self.my_db.run_query(query).fetchall()
        

        self.listar_productos(self.producto_buscado)