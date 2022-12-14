from tkinter import *
import utilidades
from tkinter import ttk
import db_conection
import productos
import clientes
import empleados

class Ventana_mantenimiento:
    def __init__(self, root):
        self.root = root
        self.ventana_de_mantenimiento = Toplevel(self.root)
        self.ventana_de_mantenimiento.title('Mantenimiento')
        self.ventana_de_mantenimiento.geometry("1100x600")
        self.ventana_de_mantenimiento.resizable(0, 0)
        utilidades.center(self.ventana_de_mantenimiento)
        self.tab_Control = ttk.Notebook(self.ventana_de_mantenimiento)
        self.tab1 = ttk.Frame(self.tab_Control)
        self.tab_Control.add(self.tab1, text = 'Productos')
        
        self.cuadro = LabelFrame(self.tab1, text = 'Registrar nuevo producto ', font = 'Arial 12 bold')
        self.cuadro.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = (150,20))
        productos.Productos_Adm(self.cuadro, self.tab1)
        
    

        self.tab2 = ttk.Frame(self.tab_Control)
        self.tab_Control.add(self.tab2, text = 'Clientes')
        self.tab_Control.pack(expand = True, fill = BOTH)

        self.cuadro2 = LabelFrame(self.tab2, text = 'Registrar nuevo Cliente', font = 'Arial 12 bold')
        self.cuadro2.grid(row = 0, column = 0, columnspan = 4, pady = 20, padx = 15)
        clientes.Clientes_Adm(self.cuadro2, self.tab2, self.ventana_de_mantenimiento)


        self.tab3 = ttk.Frame(self.tab_Control)
        self.tab_Control.add(self.tab3, text = 'Empleados')
        self.tab_Control.pack(expand = True, fill = BOTH)

        self.cuadro3 = LabelFrame(self.tab3, text = 'Registrar nuevo Empleado', font = 'Arial 12 bold')
        self.cuadro3.grid(row = 0, column = 0, columnspan = 4, pady = 20, padx = 15)
        empleados.Empleados_Adm(self.cuadro3, self.tab3, self.ventana_de_mantenimiento)


        self.ventana_de_mantenimiento.grab_set()
        self.root.wait_window(self.ventana_de_mantenimiento)