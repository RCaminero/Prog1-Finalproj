from tkinter import *
import utilidades
from tkinter import ttk
import db_conection

class Ventana_Facturacion:
    def __init__(self, root):
        self.root = root
        self.ventana_de_facturacion = Toplevel(self.root)
        self.ventana_de_facturacion.title('Facturacion')
        self.ventana_de_facturacion.geometry("1100x600")
        self.ventana_de_facturacion.resizable(0, 0)
        utilidades.center(self.ventana_de_facturacion)

        self.ventana_de_facturacion.grab_set()
        self.root.wait_window(self.ventana_de_facturacion)
