from tkinter import *
import utilidades

class Acerca_de_window:
    def __init__(self, root):
        self.root = root
        self.newWindow = Toplevel(self.root)
        self.newWindow.iconbitmap('imagenes/icon2.ico')
        self.newWindow.title('Informacion')
        self.newWindow.geometry('700x400')
        self.newWindow.resizable(0, 0)
        Label(self.newWindow, text = 'SISTEMA DE FACTURACION', font = 'Arial 18 bold').pack(pady = (25, 8))
        Label(self.newWindow, text = 'Proyecto Final - Programacion 1', font = 'Arial 16 bold').pack(pady = 2)
        Label(self.newWindow, text = 'Integrantes del Grupo:', font = 'Arial 16 bold').pack(pady = 8)
        Label(self.newWindow, text = 'Ivan Manuel Pimentel Alberto (2019-0282) - PROCESOS Y BASE DE DATOS', font = 'Arial 14').pack(pady = 2)
        Label(self.newWindow, text = 'Roberlina Caminero (2019-0322) - CONSULTAS', font = 'Arial 14').pack(pady = 2)
        Label(self.newWindow, text = 'Yudermi Hernandez (2019-0400) - LOGIN, MAIN, MENUBAR, ACERCA DE', font = 'Arial 14').pack(pady = 2)
        Label(self.newWindow, text = 'Sebastian Rodriguez (2013-1794) - MANTENIMIENTO', font = 'Arial 14').pack(pady = 2)
        Label(self.newWindow, text = 'Profesor:', font = 'Arial 16 bold').pack(pady = 8)
        Label(self.newWindow, text = 'Jose Capellan Maria', font = 'Arial 14').pack()


        utilidades.center(self.newWindow)
        self.newWindow.grab_set()
        self.root.wait_window(self.newWindow)