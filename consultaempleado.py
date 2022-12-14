from tkinter import *
import utilidades
from tkinter import ttk
import db_conection

class Ventana_Consulta_Empleado:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consulta_empleado = Toplevel(self.root)
        self.ventana_de_consulta_empleado.title('Consulta Empleados')
        self.ventana_de_consulta_empleado.geometry("1100x600")
        self.ventana_de_consulta_empleado.resizable(0, 0)
        utilidades.center(self.ventana_de_consulta_empleado)



        self.my_db = db_conection.Db_connection('sistema')

        self.identificacion_empleado = StringVar()
        self.lista_empleados = self.my_db.run_query('SELECT * FROM empleados').fetchall()


        self.my_frame = LabelFrame(self.ventana_de_consulta_empleado, text = 'Consultar Empleado', font = 'Arial 14 bold')
        self.my_frame.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx = 15)


        Label(self.my_frame, text = 'Identificacion Empleado:', font = 'Arial 12').grid(row = 0, column = 0)
        Entry(self.my_frame, font = 'Arial 12', textvariable = self.identificacion_empleado).grid(row = 0, column =1)
        Button(self.my_frame, text = 'Buscar', font = 'Arial 12', command = self.buscar_empleado).grid(row = 0 , column = 2)
        Button(self.my_frame, text = 'Todos los empleados', font = 'Arial 12', command = lambda: self.listar_empleados(self.lista_empleados)).grid(row = 1 , column = 0, pady =25)
        

        # Tabla
        self.campo = Frame(self.ventana_de_consulta_empleado)
        self.campo.grid(row = 4, column = 0, columnspan =2, padx = (15, 0))
        self.tree = ttk.Treeview(self.campo, height = 10, columns = 4)
        self.tree.pack(side = 'left')

        self.verscrlbar = ttk.Scrollbar(self.campo, orient ="vertical", command = self.tree.yview)
        self.verscrlbar.pack(side = 'right', fill = 'y')
        self.tree.configure(yscrollcommand = self.verscrlbar.set)

        self.tree["columns"] = ("1", "2","3","4","5","6","7","8")
        self.tree['show'] = 'headings'

        self.tree.column("1", width=100, anchor='c', minwidth = 100, stretch = False)
        self.tree.column("2", width=130, anchor='c')
        self.tree.column("3", width=115, anchor='c')
        self.tree.column("4", width=150, anchor='c')
        self.tree.column("5", width=170, anchor='c')
        self.tree.column("6", width=90, anchor='c')
        self.tree.column("7", width=170, anchor='c')
        self.tree.column("8", width=170, anchor='c')
        

        self.tree.heading('1', text = 'Usuario', anchor = CENTER)
        self.tree.heading('2', text = 'Contraseña', anchor = CENTER)
        self.tree.heading('3', text = 'Nombre', anchor = CENTER)
        self.tree.heading('4', text = 'Identificación', anchor = CENTER)
        self.tree.heading('5', text = 'Dirección', anchor = CENTER)
        self.tree.heading('6', text = 'Tipo', anchor = CENTER)
        self.tree.heading('7', text = 'Teléfono', anchor = CENTER)
        self.tree.heading('8', text = 'E-mail', anchor = CENTER)
    
        self.listar_empleados(self.lista_empleados)


        self.ventana_de_consulta_empleado.grab_set()
        self.root.wait_window(self.ventana_de_consulta_empleado)
        
    def listar_empleados(self, listado):
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        self.lista_empleados = self.my_db.run_query('SELECT * FROM empleados').fetchall()

        for self.empleado in listado:
            # self.cate_name = self.my_db.run_query(f"SELECT categoria_Nombre FROM categorias WHERE categoria_ID = '{self.empleado[4]}'").fetchone()
            
            self.tree.insert("",'end',text= f"{self.empleado[1]}", values=(
                self.empleado[1],
                self.empleado[2],
                self.empleado[3],
                self.empleado[4],
                self.empleado[5],
                self.empleado[6],
                self.empleado[7],
                self.empleado[8],
            ))

    def buscar_empleado(self):
        query = f"SELECT * FROM empleados WHERE Empleado_Cedula LIKE '{self.identificacion_empleado.get()}'"
        self.my_db = db_conection.Db_connection('sistema')
        self.empleado_buscado = self.my_db.run_query(query).fetchone()
        print(self.empleado_buscado)
        empleados = []
        empleados.append(self.empleado_buscado)
        self.listar_empleados(empleados)
        

        