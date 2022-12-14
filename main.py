import login
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import time
import utilidades
import mantenimiento
import acerca_de
import menu
import procesos
import consultas


title = 'IRYS System' #titlo de la aplicacion


class Main_program:
	def __init__(self, title, my_login): #Metodo constructor
		self.title = title
		self.my_login = my_login
		self.my_login.show_login()

		if self.my_login.usuario_autenticado[0]: #Autenticamos el usuario para permitirle entrar a la aplicacion
			self.root = Tk()
			self.root.title(title)
			
			self.root.geometry('1140x600')
			self.root.resizable(False, False)
			self.root.grid_columnconfigure(0, weight=1)

			menu.Menubar(self.root, self.show_mantenimiento, self.show_procesos, self.show_consultas)

        	

			self.marco_Barra_Superior = Frame(self.root, bg = 'steel blue', pady = 0)
			self.marco_Barra_Superior.grid(row = 0, column = 0, sticky = 'n')
			self.marco_Barra_Superior_left = Frame(self.marco_Barra_Superior, bg = 'steel blue')
			self.marco_Barra_Superior_left.grid(row = 0, column = 0, sticky = 'w', padx = 20)
			self.marco_Barra_Superior_right = Frame(self.marco_Barra_Superior, bg = 'steel blue',)
			self.marco_Barra_Superior_right.grid(row = 0, column = 1, sticky = 'e', padx = (590, 35), pady = 5)
			# marco_Barra_Superior.grid(row = 0, column = 0, sticky = 'w', )
			Label(self.marco_Barra_Superior_left, text  = self.title, font = 'Arial 22 bold', bg = 'steel blue', fg = 'white').grid(row = 0, column = 0, sticky = 'w')
			self.fecha_Hora = Label(self.marco_Barra_Superior_right, text = '', font = 'Arial 14', bg= 'steel blue', fg = 'white')
			self.fecha_Hora.grid(row = 0 , column = 1, sticky = 'e')
			self.times()
			Label(self.marco_Barra_Superior_right, text  = f'Usuario: {self.my_login.usuario_autenticado[1][1]}', font = 'Arial 14 ', bg = 'steel blue', fg = 'white').grid(row = 1, column = 1, sticky = 'e')
			Label(self.marco_Barra_Superior_right, text  = f'Nombre: {self.my_login.usuario_autenticado[1][3]}', font = 'Arial 14 ', bg = 'steel blue', fg = 'white').grid(row = 2, column = 1, sticky = 'e')			
			Label(self.root, text= 'Menú de opciones', font = 'Arial 18 bold').grid(row = 1, column = 0, columnspan = 2, pady = (40,15))
			self.marco_Botones = Frame(self.root, bg = 'gray56', bd = 8, relief="sunken")
			self.marco_Botones.grid(row = 2, column = 0, columnspan = 2)
			# marco_Botones.grid(row = 1, column = 0,pady = 200)
			self.imagen_mantenimiento = PhotoImage(file="imagenes/buttons/herramientas2pq.png")
			self.imagen_procesos = PhotoImage(file="imagenes/buttons/ventas2pq.png")
			self.imagen_consultas = PhotoImage(file="imagenes/buttons/consulta1pq.png")
			Button(self.marco_Botones, text = 'Mantenimiento', image = self.imagen_mantenimiento, width = 205, height = 205, compound="top", font = 'Arial 16 bold', command = self.show_mantenimiento).grid(row = 0, column = 0, padx = 60, pady = 70)
			Button(self.marco_Botones, text = 'Procesos', image = self.imagen_procesos, width = 205, height = 205, compound="top", font = 'Arial 16 bold', command = self.show_procesos).grid(row = 0, column = 1, padx = 60, pady = 70)
			Button(self.marco_Botones, text = 'Consultas', image = self.imagen_consultas, width = 205, height = 205, compound="top", font = 'Arial 16 bold', command = self.show_consultas).grid(row = 0, column = 2, padx = 60, pady = 70)



			

			utilidades.center(self.root)
			self.root.mainloop()
	
	def show_mantenimiento(self):
		mantenimiento.Ventana_mantenimiento(self.root)

	def show_procesos(self):
		procesos.Ventana_Procesos(self.root, self.my_login.usuario_autenticado)

	def show_consultas(self):
		consultas.Ventana_Consultas(self.root)


	def times(self):
		tiempo_actual = time.strftime(' %H:%M:%S - %A %d %B %Y ')
		self.fecha_Hora.config(text = tiempo_actual)
		self.fecha_Hora.after(200, lambda : self.times())

my_login = login.Login()



Main_program(title, my_login)
