from tkinter import *
import utilidades
from tkinter import ttk
import db_conection
import consultacliente
import consultaempleado
import consultaproducto
import consultafacturaxfecha

class Ventana_Consultas:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consultas = Toplevel(self.root)
        self.ventana_de_consultas.title('Consultas')
        self.ventana_de_consultas.geometry("720x450")
        self.ventana_de_consultas.resizable(0, 0)
        utilidades.center(self.ventana_de_consultas)
        

        self.my_frame = LabelFrame(self.ventana_de_consultas, text = 'Consultas', font = 'Arial 14 bold')

        self.my_frame.grid(row = 0 , column = 0 , padx = 30, pady = 15)
        self.frame_arriba = Frame(self.my_frame)
        self.frame_arriba.grid(row = 0, column = 0, padx = 20, pady = 25)
        self.frame_abajo = Frame(self.my_frame)
        self.frame_abajo.grid(row = 1, column = 0, padx = 20, pady = 25)


        self.imagen_factura = PhotoImage(file = 'imagenes/buttons/factura.png')
        self.imagen_facturaxfecha = PhotoImage(file = 'imagenes/buttons/facxfecha.png')
        self.imagen_clientes = PhotoImage(file = 'imagenes/buttons/clientes.png')
        self.imagen_empleado = PhotoImage(file = 'imagenes/buttons/empleados.png')
        self.imagen_producto = PhotoImage(file = 'imagenes/buttons/productos.png')

        

        Button(self.frame_arriba, text = 'VENTAS X FECHA', font = 'Arial 14', image = self.imagen_facturaxfecha, compound = 'left', command = self.show_consulta_factura_xfecha).grid(row = 0, column = 1, padx = (30,10))

        Button(self.frame_arriba, text = 'CLIENTES', font = 'Arial 14', image = self.imagen_clientes, compound = 'left', command = self.show_consulta_cliente).grid(row = 0, column = 0, padx = (30,10))

        Button(self.frame_abajo, text = 'PRODUCTOS', font = 'Arial 14', image = self.imagen_producto, compound = 'left', command = self.show_consulta_producto).grid(row = 0, column = 1, padx = (30,10))

        Button(self.frame_abajo, text = 'EMPLEADOS', font = 'Arial 14', image = self.imagen_empleado, compound = 'left', command = self.show_consulta_empleado).grid(row = 0, column = 2, padx = (30,10))

        self.ventana_de_consultas.grab_set()
        self.root.wait_window(self.ventana_de_consultas)
        


    def show_consulta_cliente(self):
        consultacliente.Ventana_Consulta_Cliente(self.ventana_de_consultas)

    def show_consulta_producto(self):
        consultaproducto.Ventana_Consulta_Producto(self.ventana_de_consultas)

    def show_consulta_empleado(self):
        consultaempleado.Ventana_Consulta_Empleado(self.ventana_de_consultas)

    def show_consulta_factura_xfecha(self):
        consultafacturaxfecha.Ventana_Consulta_Factura_xFecha(self.ventana_de_consultas)
    