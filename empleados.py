import db_conection
import utilidades
from tkinter import *


class Empleados_Adm:
    def __init__(self, root, ventana_padre, ventana_de_mantenimiento):
        self.root = root
        self.ventana_padre  = ventana_padre
        self.ventana_de_mantenimiento = ventana_de_mantenimiento

        #Conexion con base de datos
        self.my_db = db_conection.Db_connection('sistema')
        self.lista_empleados = self.my_db.run_query('SELECT * FROM empleados').fetchall()


        #variables
        self.empleado_username = StringVar()
        self.empleado_password = StringVar()
        self.emplado_nombre = StringVar()
        self.empleado_cedula = StringVar()
        self.empleado_direccion = StringVar()
        self.empleado_tipo = StringVar()
        self.empleado_telefono = StringVar()
        self.empleado_email = StringVar()

        self.tipos_empleados = ['Vendedor', 'Administrador']

        #Entrada nombre
        Label(self.root, text = 'Nombre: ', font = 'Arial 11').grid(row = 1, column = 0)
        self.nombre = Entry(self.root, width = 60, font = 'Arial 11', textvariable = self.emplado_nombre)
        self.nombre.focus()
        self.nombre.grid(row = 1, column = 1, pady = 10, sticky = 'w', columnspan = 3,padx = (0,15))

        #Entrada nombre de usuario
        Label(self.root, text = 'Nombre de usuario: ', font = 'Arial 11').grid(row = 2, column = 0)
        self.nombre_usuario = Entry(self.root, width = 25, font = 'Arial 11', textvariable = self.empleado_username)
        self.nombre_usuario.grid(row = 2, column = 1, pady = 10, sticky = 'w', columnspan = 3,padx = (0,15))

        #Entrada contrasena
        Label(self.root, text = 'Password: ', font = 'Arial 11').grid(row = 2, column = 2)
        self.password_usuario = Entry(self.root, font = 'Arial 11', width = 25, textvariable = self.empleado_password, show = '*')
        self.password_usuario.grid(row = 2, column = 3, pady = 10, sticky = 'w', columnspan = 3,padx = (0,15))

        #Entrada de identificacion
        Label(self.root, text = 'Identificación: ', font = 'Arial 11').grid(row = 3, column = 0)
        self.identificacion = Entry(self.root, font = 'Arial 11', textvariable = self.empleado_cedula, width =20)
        self.identificacion.grid(row = 3, column = 1, padx = (0,0), pady = 10, sticky = 'w')
        
        #tipo de empleado
        Label(self.root, text = 'Tipo Empleado: ', font = 'Arial 11').grid(row = 3, column = 2)
        self.selecciona_tipo = ttk.Combobox(self.root, textvariable = self.empleado_tipo, state ='readonly', font = 'Arial 11')
        print(self.tipos_empleados)
        self.selecciona_tipo['values'] = self.tipos_empleados#Sacar de la base de datos
        self.selecciona_tipo.grid(row = 3, column = 3, sticky = 'w', padx = 10)

        #Entrada de direccion
        Label(self.root, text = 'Dirección: ', font = 'Arial 11').grid(row = 4, column = 0)
        self.telefono = Entry(self.root, font = 'Arial 11', textvariable = self.empleado_direccion, width = 60)
        self.telefono.grid(row = 4, column = 1, padx = (0,0), pady = 10, sticky = 'w', columnspan = 3)

        #Entrada de telefono
        Label(self.root, text = 'Teléfono: ', font = 'Arial 11').grid(row = 5, column = 0)
        self.telefono = Entry(self.root, font = 'Arial 11', textvariable = self.empleado_telefono, width =20)
        self.telefono.grid(row = 5, column = 1, padx = (0,0), pady = 10, sticky = 'w')

        #Entrada de email
        Label(self.root, text = 'E-mail: ', font = 'Arial 11').grid(row = 5, column = 2)
        self.email = Entry(self.root, font = 'Arial 11', width = 25, textvariable = self.empleado_email)
        self.email.grid(row = 5, column = 3, padx = (0,0), pady = 10, sticky = 'w')

        # Boton añadir empleado 
        Button(self.root, text = 'Guardar', font = 'Arial 9 bold', command = self.añadir_empleado).grid(row = 6,column =  3, sticky = W + E, pady = 5,padx = (0, 10))
        # command = self.añadir_empleado

        
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
        
        
        # Botones
        Button(self.ventana_padre, text = 'Eliminar',width = 40,  font = 'Arial 9 bold', command = self.borrar_empleado).grid(row = 5, column = 1, sticky = 'w', padx = (0, 0), pady = (10,0))
        
        Button(self.ventana_padre, text = 'EDITAR',width = 40,  font = 'Arial 9 bold', command = lambda: self.editar_empleados(self.ventana_padre)).grid(row = 5, column = 1, sticky ='e', pady = (10,0), padx = (0, 130))
        

        self.listar_empleados()

    def añadir_empleado(self):
        self.indice_tipo_empleado = self.tipos_empleados.index(self.empleado_tipo.get())

        self.my_db.run_query(f"INSERT INTO empleados VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?)",(
            self.empleado_username.get(), 
            self.empleado_password.get(),
            self.emplado_nombre.get(),
            self.empleado_cedula.get(), 
            self.empleado_direccion.get(), 
            self.indice_tipo_empleado,
            self.empleado_telefono.get(), 
            self.empleado_email.get()
            ))

        self.listar_empleados()

    def listar_empleados(self):
        # Limpiar tabla
        self.records = self.tree.get_children()
        for elemento in self.records:
            self.tree.delete(elemento)

        self.lista_empleados = self.my_db.run_query('SELECT * FROM empleados').fetchall()

        for self.empleado in self.lista_empleados:
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

    def borrar_empleado(self):
        try:
            self.tree.item(self.tree.selection())['text'][1]
        except IndexError as e:
            print('Complete los campos')
            return

        nombre = self.tree.item(self.tree.selection())['text']
        print(nombre)
        self.my_db.run_query(f"DELETE FROM empleados WHERE empleado_username IS '{nombre}'")
        
        print(f'El empleado {nombre} se elimino correctamente')
        self.listar_empleados()

    def editar_empleados(self, ventana_de_mantenimiento):
        self.ventana_de_mantenimiento = ventana_de_mantenimiento
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError:
            print('Por favor seleccione un empleado')
            return
        #Variables
        username_viejo = self.tree.item(self.tree.selection())['text']
        password_vieja = self.tree.item(self.tree.selection())['values'][1]
        nombre_viejo = self.tree.item(self.tree.selection())['values'][2]
        cedula_vieja = self.tree.item(self.tree.selection())['values'][3]
        direccion_vieja = self.tree.item(self.tree.selection())['values'][4]
        tipo_empleado_viejo = self.tree.item(self.tree.selection())['values'][5]
        telefono_viejo = self.tree.item(self.tree.selection())['values'][6]
        email_viejo = self.tree.item(self.tree.selection())['values'][7]
        print(username_viejo, password_vieja, nombre_viejo, cedula_vieja,direccion_vieja,tipo_empleado_viejo, telefono_viejo, email_viejo)
        #ventana
        self.edit_window = Toplevel(self.ventana_de_mantenimiento)
        self.edit_window.title = 'Editar Empleado'

        # Old username
        Label(self.edit_window, text = 'Usuario Antiguo:', font = 'Arial 11').grid(row = 0, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = username_viejo), state = 'readonly', font = 'Arial 11').grid(row = 0, column = 1, padx = 5 , pady = 10, sticky = 'w', columnspan = 3)

        # New username
        Label(self.edit_window, text = 'Usuario Nuevo:', font = 'Arial 11').grid(row = 1, column = 0, padx = 5, pady = 10)
        usuario_nuevo = Entry(self.edit_window, font = 'Arial 11')
        usuario_nuevo.grid(row = 1, column = 1, padx = 5, pady = 10, sticky = 'w', columnspan = 3)

        # Old password
        Label(self.edit_window, text = 'Contraseña Antigua:', font = 'Arial 11').grid(row = 0, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = password_vieja), state = 'readonly', font = 'Arial 11').grid(row = 0, column = 3, padx = 5 , pady = 10, sticky = 'w')

        # New password
        Label(self.edit_window, text = 'Contraseña Nueva:', font = 'Arial 11').grid(row = 1, column = 2, padx = 5, pady = 10)
        contraseña_nueva = Entry(self.edit_window, font = 'Arial 11')
        contraseña_nueva.grid(row = 1, column = 3, padx = 5, pady = 10, sticky = 'w')


        # Old name
        Label(self.edit_window, text = 'Nombre Antiguo:', font = 'Arial 11').grid(row = 2, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = nombre_viejo), state = 'readonly', font = 'Arial 11').grid(row = 2, column = 1, padx = 5 , pady = 10, sticky = 'w')

        # New name
        Label(self.edit_window, text = 'Nombre Nuevo:', font = 'Arial 11').grid(row = 3, column = 0)
        Nombre_nuevo = Entry(self.edit_window, font = 'Arial 11')
        Nombre_nuevo.grid(row = 3, column = 1, sticky = 'w')


        # Old identificacion
        Label(self.edit_window, text = 'Identificacion Antigua:', font = 'Arial 11').grid(row = 2, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = cedula_vieja), state = 'readonly', font = 'Arial 11').grid(row = 2, column = 3, padx = 5 , pady = 10, sticky = 'w', columnspan = 3)

        # New identificacion
        Label(self.edit_window, text = 'Identificacion Nueva:', font = 'Arial 11').grid(row = 3, column = 2, padx = 5, pady = 10)
        identificacion_nueva = Entry(self.edit_window, font = 'Arial 11')
        identificacion_nueva.grid(row = 3, column = 3, padx = 5, pady = 10, sticky = 'w', columnspan = 3)

        
        # Old direccion
        Label(self.edit_window, text = 'Direccion Antigua:', font = 'Arial 11').grid(row = 4, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = direccion_vieja), state = 'readonly', font = 'Arial 11').grid(row = 4, column = 1, padx = 5 , pady = 10, sticky = 'w', columnspan = 3)

        # New direccion
        Label(self.edit_window, text = 'Direccion Nueva:', font = 'Arial 11').grid(row = 5, column = 0, padx = 5, pady = 10)
        direccion_nueva = Entry(self.edit_window, font = 'Arial 11')
        direccion_nueva.grid(row = 5, column = 1, padx = 5, pady = 10, sticky = 'w', columnspan = 3)


        # Old tipo empleado
        Label(self.edit_window, text = 'Tipo de Empleado Antiguo:', font = 'Arial 11').grid(row = 4, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = tipo_empleado_viejo), state = 'readonly', font = 'Arial 11').grid(row = 4, column = 3, padx = 5 , pady = 10, sticky = 'w')

        # New tipo empleado
        Label(self.edit_window, text = 'Tipo de Empleado Nuevo: ', font = 'Arial 11').grid(row = 5, column = 2)
        self.selecciona_tipo = ttk.Combobox(self.edit_window, textvariable = self.empleado_tipo, state ='readonly', font = 'Arial 11')
        print(self.tipos_empleados)
        self.selecciona_tipo['values'] = self.tipos_empleados #Sacar de la base de datos
        self.selecciona_tipo.grid(row = 5, column = 3, sticky = 'w')


        # Old telefono
        Label(self.edit_window, text = 'Telefono Antiguo:', font = 'Arial 11').grid(row = 6, column = 0, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = telefono_viejo), state = 'readonly', font = 'Arial 11').grid(row = 6, column = 1, padx = 5 , pady = 10, sticky = 'w')

        # New telefono
        Label(self.edit_window, text = 'Telefono Nuevo:', font = 'Arial 11').grid(row = 7, column = 0, padx = 5, pady = 10)
        telefono_nuevo = Entry(self.edit_window, font = 'Arial 11')
        telefono_nuevo.grid(row = 7, column = 1, padx = 5, pady = 10, sticky = 'w')


        # Old email
        Label(self.edit_window, text = 'Email Antiguo:', font = 'Arial 11').grid(row = 6, column = 2, padx = 5, pady = 10)
        Entry(self.edit_window, textvariable = StringVar(self.edit_window, value = email_viejo), state = 'readonly', font = 'Arial 11').grid(row = 6, column = 3, padx = 5 , pady = 10, sticky = 'w')

        # New email
        Label(self.edit_window, text = 'Email Nuevo:', font = 'Arial 11').grid(row = 7, column = 2, padx = 5, pady = 10)
        email_nuevo = Entry(self.edit_window, font = 'Arial 11')
        email_nuevo.grid(row = 7, column = 3, padx = 5, pady = 10, sticky = 'w')

        
        Button(self.edit_window, text = 'Actualizar', command = lambda: self.edit_records(usuario_nuevo.get(), username_viejo, 
        contraseña_nueva.get(), password_vieja, 
        Nombre_nuevo.get(), nombre_viejo, 
        identificacion_nueva.get() , cedula_vieja,
        direccion_nueva.get() , direccion_vieja,
        self.selecciona_tipo.get() , tipo_empleado_viejo,
        telefono_nuevo.get() , telefono_viejo,
        email_nuevo.get() , email_viejo,
        )).grid(row =8, column = 3, sticky = e, pady = 5)

        
        utilidades.center(self.edit_window)
        self.edit_window.grab_set()
        self.ventana_de_mantenimiento.wait_window(self.edit_window)
        self.edit_window.mainloop()
    

    def edit_records(self, usuario_nuevo, username_viejo,
        contraseña_nueva, password_vieja,
        Nombre_nuevo, nombre_viejo,
        identificacion_nueva, cedula_vieja,
        direccion_nueva, direccion_vieja,
        selecciona_tipo, tipo_empleado_viejo,
        telefono_nuevo, telefono_viejo,
        email_nuevo, email_viejo):
        print(usuario_nuevo, username_viejo,
        contraseña_nueva, password_vieja,
        Nombre_nuevo, nombre_viejo,
        identificacion_nueva, cedula_vieja,
        direccion_nueva, direccion_vieja,
        selecciona_tipo, tipo_empleado_viejo,
        telefono_nuevo, telefono_viejo,
        email_nuevo, email_viejo)
    
        self.my_db.run_query("UPDATE empleados SET Empleado_username = ?, Empleado_password = ?, Empleado_nombre = ?, Empleado_Cedula = ?, Empleado_Direccion = ?, Empleado_Tipo = ?, Empleado_Telefono = ?, Empleado_Email = ? WHERE Empleado_username LIKE ?",(usuario_nuevo, contraseña_nueva, Nombre_nuevo, identificacion_nueva, direccion_nueva, selecciona_tipo, telefono_nuevo, email_nuevo, username_viejo))
        self.edit_window.destroy()
        print('El empleado {} se actualizo correctamente'.format(nombre_viejo))
        self.listar_empleados()
