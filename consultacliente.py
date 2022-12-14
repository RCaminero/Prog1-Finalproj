from tkinter import *
import utilidades
from tkinter import ttk
import db_conection

class Ventana_Consulta_Cliente:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consulta_cliente = Toplevel(self.root)
        self.ventana_de_consulta_cliente.title('Consulta Clientes')
        self.ventana_de_consulta_cliente.geometry("1100x600")
        self.ventana_de_consulta_cliente.resizable(0, 0)
        utilidades.center(self.ventana_de_consulta_cliente)
        

        self.my_db = db_conection.Db_connection('sistema')

        self.identificacion_cliente = StringVar()
        self.lista_clientes = self.my_db.run_query('SELECT * FROM clientes').fetchall()


        self.my_frame = LabelFrame(self.ventana_de_consulta_cliente, text = 'Consultar Clientes', font = 'Arial 14 bold')
        self.my_frame.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx = 15)


        Label(self.my_frame, text = 'Identificacion Cliente:', font = 'Arial 12').grid(row = 0, column = 0)
        Entry(self.my_frame, font = 'Arial 12', textvariable = self.identificacion_cliente).grid(row = 0, column =1)
        Button(self.my_frame, text = 'Buscar', font = 'Arial 12', command = self.buscar_cliente).grid(row = 0 , column = 2)
        Button(self.my_frame, text = 'Todos los clientes', font = 'Arial 12', command = lambda: self.listar_clientes(self.lista_clientes)).grid(row = 1 , column = 0, pady =25)
        

        #Tabla
        self.campo = Frame(self.ventana_de_consulta_cliente)
        self.campo.grid(row = 1, column = 0, columnspan =3, padx = (25, 0), pady = 25)
        self.tree = ttk.Treeview(self.campo, height = 10, columns = 4)
        self.tree.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.tree.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = self.verscrlbar.set)

        self.tree["columns"] = ("1", "2","3","4","5","6","7","8")
        self.tree['show'] = 'headings'

        self.tree.column("1", width=215, anchor='c', minwidth = 100, stretch = False)
        self.tree.column("2", width=100, anchor='c')
        self.tree.column("3", width=117, anchor='c')
        self.tree.column("4", width=170, anchor='c')
        self.tree.column("5", width=120, anchor='c')
        self.tree.column("6", width=100, anchor='c')
        self.tree.column("7", width=150, anchor='c')
        self.tree.column("8", width=100, anchor='c')

        self.tree.heading('1', text = 'Nombre', anchor = CENTER)
        self.tree.heading('2', text = 'Identificacion', anchor = CENTER)
        self.tree.heading('3', text = 'Tipo Identificacion', anchor = CENTER)
        self.tree.heading('4', text = 'Direccion', anchor = CENTER)
        self.tree.heading('5', text = 'Estado Cliente', anchor = CENTER)
        self.tree.heading('6', text = 'Telefono', anchor = CENTER)
        self.tree.heading('7', text = 'E-mail', anchor = CENTER)
        self.tree.heading('8', text = 'Limite de credito', anchor = CENTER)


        self.listar_clientes(self.lista_clientes)

        self.ventana_de_consulta_cliente.grab_set()
        self.root.wait_window(self.ventana_de_consulta_cliente)

        
    def listar_clientes(self, listado):
        self.listado = listado
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)


        for self.cliente in self.listado:
            # self.cate_name = self.my_db.run_query(f"SELECT categoria_Nombre FROM categorias WHERE categoria_ID = '{self.cliente[4]}'").fetchone()
            
            self.tree.insert("",'end',text= f"{self.cliente[1]}", values=(
                self.cliente[1],
                self.cliente[2],
                self.cliente[3],
                self.cliente[4],
                self.cliente[5],
                self.cliente[6],
                self.cliente[7],
                self.cliente[8],
            ))

    def buscar_cliente(self):
        query = f"SELECT * FROM clientes WHERE cliente_Identificacion LIKE '{self.identificacion_cliente.get()}'"
        self.my_db = db_conection.Db_connection('sistema')
        self.cliente_buscado = self.my_db.run_query(query).fetchone()
        print(self.cliente_buscado)
        clientes = []
        clientes.append(self.cliente_buscado)
        self.listar_clientes(clientes)
        