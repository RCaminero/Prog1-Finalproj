import db_conection
from tkinter import *
import utilidades

class Clientes_Adm:
    def __init__(self, root, ventana_padre, ventana_de_mantenimiento):
        self.root = root
        self.ventana_padre = ventana_padre
        self.ventana_de_mantenimiento = ventana_de_mantenimiento
        
        utilidades.center(self.ventana_de_mantenimiento)
        #Conexion con base de Datos
        self.my_db = db_conection.Db_connection('sistema')
        self.lista_clientes = self.my_db.run_query('SELECT * FROM clientes').fetchall()

        #Variables
        self.nombre_var = StringVar()
        self.identificacion_var = StringVar()
        self.tipo_identificacion_var = StringVar()
        self.direccion_var = StringVar()
        self.tipo_cliente_var = IntVar()
        self.telefono_var = IntVar()
        self.email_var = StringVar()
        self.limite_credito_var = DoubleVar()

        self.tipos_de_identificaciones = ['RNC / Empresas', 'Cedula / Persona Fisica']
        
        #Entrada nombre
        Label(self.root, text = 'Nombre: ', font = 'Arial 11').grid(row = 1, column = 0)
        self.nombre = Entry(self.root, width = 65, font = 'Arial 11', textvariable = self.nombre_var)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1, pady = 10, sticky = 'w', columnspan = 3,padx = (0,15))

        #Entrada de identificacion
        Label(self.root, text = 'Identificacion: ', font = 'Arial 11').grid(row = 2, column = 0)
        self.identificacion = Entry(self.root, font = 'Arial 11', textvariable = self.identificacion_var, width =21)
        self.identificacion.grid(row = 2, column = 1, padx = (0,0), pady = 10, sticky = 'w')
        
        Label(self.root, text = 'Tipo Identificacion: ', font = 'Arial 11').grid(row = 2, column = 2)
        self.selecciona_tipo = ttk.Combobox(self.root, width = 20, textvariable = self.tipo_identificacion_var, state ='readonly', font = 'Arial 11')
        print(self.tipos_de_identificaciones)
        self.selecciona_tipo['values'] = self.tipos_de_identificaciones#Sacar de la base de datos
        self.selecciona_tipo.grid(row = 2, column = 3, sticky = 'w')

        
        #Entrada de direccion
        Label(self.root, text = 'Direccion: ', font = 'Arial 11').grid(row = 4, column = 0)
        self.direccion = Entry(self.root, font = 'Arial 11', textvariable = self.direccion_var, width = 65)
        self.direccion.grid(row = 4, column = 1, pady = 10, sticky = 'w', columnspan = 3)

        #Entrada de telefono
        Label(self.root, text = 'Telefono: ', font = 'Arial 11').grid(row = 5, column = 0)
        self.telefono = Entry(self.root, font = 'Arial 11', textvariable = self.telefono_var)
        self.telefono.grid(row = 5, column = 1, padx = (5, 0), pady = 10, sticky = 'w')

        #Entrada de email
        Label(self.root, text = 'Email: ', font = 'Arial 11').grid(row = 5, column = 2, sticky = 'e')
        self.email = Entry(self.root, font = 'Arial 11', textvariable = self.email_var, width = 23)
        self.email.grid(row = 5, column = 3, pady = 10, sticky = 'w')

        #Entrada de limite de credito
        Label(self.root, text = 'Limite de Credito: ', font = 'Arial 11').grid(row = 7, column = 0)
        self.limite_credito = Entry(self.root, font = 'Arial 11', textvariable = self.limite_credito_var, width = 19)
        self.limite_credito.grid(row = 7, column = 1, padx = 10, pady = 10, sticky = 'w')

        # Boton añadir cliente 
        Button(self.root, text = 'Guardar', font = 'Arial 9 bold', command = self.añadir_cliente).grid(row = 8,column =  3, sticky = W + E, pady = 5,padx = (0, 10))
        # command = self.añadirProducto
        
        # Mensaje de salida 
        # self.mensaje = Label(self.ventana_padre, text = '', fg = 'red')
        # self.mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)


        # Tabla
        self.campo = Frame(self.ventana_padre)
        self.campo.grid(row = 4, column = 0, columnspan =2, padx = (15, 0))
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
        
        # Botones
        Button(self.ventana_padre, text = 'Eliminar',width = 40,  font = 'Arial 9 bold', command = self.borrar_cliente).grid(row = 5, column = 1, sticky = 'w', padx = (0, 0), pady = (10,0))
        # ,command = self.borrarProducto
        Button(self.ventana_padre, text = 'EDITAR',width = 40,  font = 'Arial 9 bold', command = lambda: self.editar_clientes(self.ventana_padre)).grid(row = 5, column = 1, sticky ='e', pady = (10,0), padx = (0, 130))
        # ,, command = lambda: self.editarProducto(self.ventana_padre)


        self.listar_clientes()
    
    def añadir_cliente(self):
        self.indice_tipo_de_identificacion = self.tipos_de_identificaciones.index(self.tipo_identificacion_var.get())

        self.my_db.run_query(f"INSERT INTO clientes VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?)",(
            self.nombre_var.get(), 
            self.identificacion_var.get(),
            self.indice_tipo_de_identificacion,
            self.direccion_var.get(), 
            0,
            self.telefono_var.get(), 
            self.email_var.get(), 
            self.limite_credito_var.get()
            ))

        self.listar_clientes()

    def listar_clientes(self):
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        self.lista_clientes = self.my_db.run_query('SELECT * FROM clientes').fetchall()

        for self.cliente in self.lista_clientes:
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

    def borrar_cliente(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            print('Complete los campos')
            return

        nombre = self.tree.item(self.tree.selection())['text']
        print(nombre)
        self.my_db.run_query(f"DELETE FROM clientes WHERE cliente_Nombre IS '{nombre}'")
        
        print(f'El producto {nombre} se elimino correctamente')
        self.listar_clientes()

    def editar_clientes(self, ventana_de_mantenimiento):
        self.ventana_de_mantenimiento = ventana_de_mantenimiento
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError:
            print('Por favor seleccione un producto')
            return
        #Variables
        nombre_viejo = self.tree.item(self.tree.selection())['text']
        identificacion_vieja = self.tree.item(self.tree.selection())['values'][1]
        tipo_identificacion_vieja = self.tree.item(self.tree.selection())['values'][2]
        direccion = self.tree.item(self.tree.selection())['values'][3]
        tipo_cliente = self.tree.item(self.tree.selection())['values'][4]
        telefono = self.tree.item(self.tree.selection())['values'][5]
        email = self.tree.item(self.tree.selection())['values'][6]
        limite_credito = self.tree.item(self.tree.selection())['values'][7]
        print(nombre_viejo, identificacion_vieja, tipo_identificacion_vieja, direccion,tipo_cliente,telefono,email, limite_credito)
        #ventana
        self.edit_window = Toplevel(self.ventana_de_mantenimiento)
        self.edit_window.title = 'Editar Cliente'

        # Old Name
        Label(self.edit_window, text = 'Nombre Antiguo:', font = 'Arial 11').grid(row = 0, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = nombre_viejo), state = 'readonly', font = 'Arial 11', width = 78).grid(row = 0, column = 1, padx = 5 , pady = 10, sticky = 'w', columnspan = 3)

        # New Name
        Label(self.edit_window, text = 'Nombre Nuevo:', font = 'Arial 11').grid(row = 1, column = 0, padx = 5, pady = 10)
        nombre_nuevo = Entry(self.edit_window, font = 'Arial 11', width = 78)
        nombre_nuevo.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = 'w', columnspan = 3)

        # Old identificacion
        Label(self.edit_window, text = 'Identificacion Antigua:', font = 'Arial 11').grid(row = 2, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = identificacion_vieja), state = 'readonly', font = 'Arial 11').grid(row = 2, column = 1, padx = 5 , pady = 10, sticky = 'w')

        # New identificacion
        Label(self.edit_window, text = 'Identificación Nueva:', font = 'Arial 11').grid(row = 3, column = 0, padx = 5, pady = 10)
        identificacion_nueva = Entry(self.edit_window, font = 'Arial 11')
        identificacion_nueva.grid(row = 3, column = 1, padx = 5, pady = 10, sticky = 'w')


        # Old tipo identificacion
        Label(self.edit_window, text = 'Tipo de Identificacion Antigua:', font = 'Arial 11').grid(row = 2, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = tipo_identificacion_vieja), state = 'readonly', font = 'Arial 11', width = 30).grid(row = 2, column = 3, padx = 5 , pady = 10, sticky = 'w')

        # New tipo identificacion
        Label(self.edit_window, text = 'Tipo Identificacion Nueva: ', font = 'Arial 11').grid(row = 3, column = 2)
        self.selecciona_tipo = ttk.Combobox(self.edit_window, width = 28, textvariable = self.tipo_identificacion_var, state ='readonly', font = 'Arial 11')
        print(self.tipos_de_identificaciones)
        self.selecciona_tipo['values'] = self.tipos_de_identificaciones#Sacar de la base de datos
        self.selecciona_tipo.grid(row = 3, column = 3, sticky = 'w')


        # Old direccion
        Label(self.edit_window, text = 'Direccion Antigua:', font = 'Arial 11').grid(row = 4, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = direccion), state = 'readonly', font = 'Arial 11', width = 78).grid(row = 4, column = 1, padx = 5 , pady = 10, sticky = 'w', columnspan = 3)

        # New direccion
        Label(self.edit_window, text = 'Direccion Nueva:', font = 'Arial 11').grid(row = 5, column = 0, padx = 5, pady = 10)
        direccion_nueva = Entry(self.edit_window, font = 'Arial 11', width = 78)
        direccion_nueva.grid(row = 5, column = 1, padx = 5, pady = 10, sticky = 'w', columnspan = 3)

        # Old telefono
        Label(self.edit_window, text = 'Telefono Antiguo:', font = 'Arial 11').grid(row = 6, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = telefono), state = 'readonly', font = 'Arial 11').grid(row = 6, column = 1, padx = 5 , pady = 10, sticky = 'w')

        # New telefono
        Label(self.edit_window, text = 'Telefono Nuevo:', font = 'Arial 11').grid(row = 7, column = 0, padx = 5, pady = 10)
        telefono_nuevo = Entry(self.edit_window, font = 'Arial 11')
        telefono_nuevo.grid(row = 7, column = 1, padx = 5, pady = 10, sticky = 'w')

        # Old email
        Label(self.edit_window, text = 'Email Antiguo:', font = 'Arial 11').grid(row = 6, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = email), state = 'readonly', font = 'Arial 11', width = 30).grid(row = 6, column = 3, padx = 5 , pady = 10, sticky = 'w')

        # New email
        Label(self.edit_window, text = 'Email Nuevo:', font = 'Arial 11').grid(row = 7, column = 2, padx = 5, pady = 10)
        email_nuevo = Entry(self.edit_window, font = 'Arial 11', width = 30)
        email_nuevo.grid(row = 7, column = 3, padx = 5, pady = 10, sticky = 'w')

        # Old Limite de Credito
        Label(self.edit_window, text = 'Limite de Credito Antiguo:', font = 'Arial 11').grid(row = 8, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = limite_credito), state = 'readonly', font = 'Arial 11').grid(row = 8, column = 1, padx = 5 , pady = 10, sticky = 'w')

        # New Limite de Credito
        Label(self.edit_window, text = 'Limite de Credito Nuevo:', font = 'Arial 11').grid(row = 9, column = 0, padx = 5, pady = 10)
        limiteCredito_nuevo = Entry(self.edit_window, font = 'Arial 11')
        limiteCredito_nuevo.grid(row = 9, column = 1, padx = 5, pady = 10, sticky = 'w')

        
        Button(self.edit_window, text = 'Actualizar', command = lambda: self.edit_records(nombre_nuevo.get(), nombre_viejo, 
        identificacion_nueva.get(), identificacion_vieja, 
        self.tipo_identificacion_var.get(), tipo_identificacion_vieja, 
        direccion_nueva.get() , direccion,
        telefono_nuevo.get() , telefono,
        email_nuevo.get() , email,
        limiteCredito_nuevo.get() , limite_credito
        )).grid(row =10, column = 3, sticky = W, pady = 5)

        

        utilidades.center(self.edit_window)
        self.edit_window.grab_set()
        self.ventana_de_mantenimiento.wait_window(self.edit_window)
        self.edit_window.mainloop()
    
    def edit_records(self, nombre_nuevo, nombre_viejo,
        identificacion_nueva, identificacion_vieja,
        tipo_identificacion_nueva, tipo_identificacion_vieja,
        direccion_nueva, direccion_vieja,
        telefono_nuevo, telefono_viejo,
        email_nuevo, email_viejo,
        limite_credito_nuevo, limite_credito_viejo):
        print(nombre_nuevo, nombre_viejo,
        identificacion_nueva, identificacion_vieja,
        tipo_identificacion_nueva, tipo_identificacion_vieja,
        direccion_nueva, direccion_vieja,
        telefono_nuevo, telefono_viejo,
        email_nuevo, email_viejo,
        limite_credito_nuevo, limite_credito_viejo)
    
        self.my_db.run_query("UPDATE clientes SET cliente_Nombre = ?, cliente_Identificacion = ?, cliente_Tipo_Identificacion = ?, cliente_Direccion = ?, cliente_Telefono = ?, cliente_Email = ?, cliente_Limite_Credito = ? WHERE cliente_Nombre LIKE ?",(nombre_nuevo, identificacion_nueva, tipo_identificacion_nueva, direccion_nueva, telefono_nuevo, email_nuevo, limite_credito_nuevo, nombre_viejo))
        self.edit_window.destroy()
        print('El cliente {} se actualizo correctamente'.format(nombre_viejo))
        self.listar_clientes()