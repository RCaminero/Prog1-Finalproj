from tkinter import *
import acerca_de


class Menubar:
    def __init__(self, root, mantenimiento, procesos, consultas):
        self.root = root
        self.mantenimiento = mantenimiento
        self.procesos = procesos
        self.consultas = consultas
        self.menubar = Menu(self.root)
        #Menu Opciones
        self.opciones_menu = Menu(self.menubar, tearoff = 0)
        self.opciones_menu.add_command(label = 'Mantenimiento / Registro', command = self.mantenimiento)
        self.opciones_menu.add_command(label = 'Procesos Factura', command = self.procesos)
        self.opciones_menu.add_command(label = 'Consultar Factura', command = self.consultas)
        #Menu Acerca de
        self.acerca_de_menu = Menu(self.menubar, tearoff = 0)
        self.acerca_de_menu.add_command(label = 'Información del grupo', command = self.acerca_de_window)
        #Menu Salir
        self.salir_menu = Menu(self.menubar, tearoff = 0)
        self.salir_menu.add_command(label = 'Salir', command = self.root.destroy)
        #añadir menus
        self.menubar.add_cascade(menu = self.opciones_menu, label = 'Opciones')
        self.menubar.add_cascade(menu = self.acerca_de_menu, label = 'Acerca De')
        self.menubar.add_cascade(menu = self.salir_menu, label = 'Salir')
        self.root.config(menu = self.menubar)

    def acerca_de_window(self):
        acerca_de.Acerca_de_window(self.root)


class Menubar_factura:
    def __init__(self, root, anadir, editar, eliminar, vender):
        self.root = root
        self.anadir = anadir
        self.editar = editar
        self.eliminar = eliminar
        self.vender = vender
        self.menubar = Menu(self.root)
        #Menu Factura
        self.opciones_menu = Menu(self.menubar, tearoff = 0)
        self.opciones_menu.add_command(label = 'Añadir', command = self.anadir)
        self.opciones_menu.add_command(label = 'Editar', command = self.editar)
        self.opciones_menu.add_command(label = 'Eliminar', command = self.eliminar)
        #Menu Venta
        self.venta_menu = Menu(self.menubar, tearoff = 0)
        self.venta_menu.add_command(label = 'Vender', command = self.vender)
        #Menu Salir
        self.salir_menu = Menu(self.menubar, tearoff = 0)
        self.salir_menu.add_command(label = 'Salir', command = self.root.destroy)
        #añadir menus
        self.menubar.add_cascade(menu = self.opciones_menu, label = 'Opciones')
        self.menubar.add_cascade(menu = self.venta_menu, label = 'Venta')
        self.menubar.add_cascade(menu = self.salir_menu, label = 'Salir')
        self.root.config(menu = self.menubar)

    