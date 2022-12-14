from tkinter import *
import utilidades
from tkinter import ttk
import db_conection

class Ventana_Consulta_Factura:
    def __init__(self, root):
        self.root = root
        self.ventana_de_consulta_factura = Toplevel(self.root)
        self.ventana_de_consulta_factura.title('Consulta Facturas')
        self.ventana_de_consulta_factura.geometry("1100x600")
        self.ventana_de_consulta_factura.resizable(0, 0)
        utilidades.center(self.ventana_de_consulta_factura)





        self.ventana_de_consulta_factura.grab_set()
        self.root.wait_window(self.ventana_de_consulta_factura)