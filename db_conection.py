#Imports
import sqlite3

#Objeto conexion
class Db_connection :
	def __init__(self, db_name):
		self.db_name = db_name
		self.connect = sqlite3.connect(f"{self.db_name}.db")
		self.cursor = self.connect.cursor()

		try:
			self.cursor.execute("""
				CREATE TABLE empleados (
					Empleado_Id INTEGER PRIMARY KEY AUTOINCREMENT,
					Empleado_username VARCHAR(50) UNIQUE NOT NULL,
					Empleado_password VARCHAR(50) NOT NULL,
					Empleado_nombre VARCHAR(50) NOT NULL,
					Empleado_Cedula INTEGER UNIQUE NOT NULL,
					Empleado_Direccion VARCHAR(100),
					Empleado_Tipo INTEGER DEFAULT 0,
					Empleado_Telefono INTEGER,
					Empleado_Email VARCHAR(100)
				)
			""")
		except sqlite3.OperationalError :
			print('La Tabla empleados se ha creado correctamente')
		except:
			print('Ha ocurrido un error')

		try:
			self.cursor.execute("""
				CREATE TABLE clientes (
					cliente_ID INTEGER PRIMARY KEY AUTOINCREMENT,
					cliente_Nombre VARCHAR(100) UNIQUE NOT NULL,
					cliente_Identificacion INTEGER UNIQUE NOT NULL,
					cliente_Tipo_Identificacion INTEGER NOT NULL DEFAULT 0,
					cliente_Direccion VARCHAR(100),
					cliente_Tipo INTEGER DEFAULT 0,
					cliente_Telefono INTEGER,
					cliente_Email VARCHAR(100), 
					cliente_Limite_Credito INTEGER DEFAULT 5000
				)
			""")
		except sqlite3.OperationalError:
			print('La Tabla Clientes se ha creado correctamente')
		except:
			print('Ha ocurrido un error')
		try:
			self.cursor.execute("""
				CREATE TABLE facturas (
					factura_No INTEGER PRIMARY KEY AUTOINCREMENT,
					factura_ID_Cliente INTEGER NOT NULL,
					factura_Fecha TEXT NOT NULL,
					factura_Hora TEXT NOT NULL,
					factura_ID_Vendedor INTEGER NOT NULL,
					factura_Estado INTEGER DEFAULT 0,
					factura_ID_Modo_Pago INTEGER NOT NULL,
					factura_Condicion INTEGER DEFAULT 0
				)
			""")
		except sqlite3.OperationalError:   
			print('La Tabla facturas se ha creado correctamente')
		except:
			print('Ha ocurrido un error')

		try:
			self.cursor.execute("""
				CREATE TABLE detalle_factura (
					detalle_ID INTEGER PRIMARY KEY AUTOINCREMENT,
					detalle_NO_Factura INTEGER NOT NULL,
					detalle_ID_Producto INTEGER NOT NULL,
					detalle_Cantidad INTEGER DEFAULT 1,
					detalle_Precio_Venta REAL NOT NULL,
					detalle_Descuento REAL DEFAULT 0.0
				)
			""")
		except sqlite3.OperationalError:   
			print('La Tabla detalle_factura se ha creado correctamente')
		except:
			print('Ha ocurrido un error')
		
		try:
			self.cursor.execute("""
				CREATE TABLE modo_pago (
					modo_pago_ID INTEGER PRIMARY KEY AUTOINCREMENT,
					modo_pago_Tipo VARCHAR(50) DEFAULT 'CONTADO'
				)
			""")
		except sqlite3.OperationalError:   
			print('La Tabla modo_pago se ha creado correctamente')
		except:
			print('Ha ocurrido un error')
		try:
			self.cursor.execute("""
				CREATE TABLE productos (
					producto_ID INTEGER PRIMARY KEY AUTOINCREMENT,
					producto_Nombre VARCHAR(50) NOT NULL UNIQUE,
					producto_Precio REAL NOT NULL,
					producto_Stock INTEGER NOT NULL,
					producto_ID_categoria INTEGER NOT NULL
				)
			""")
		except sqlite3.OperationalError:   
			print('La Tabla productos se ha creado correctamente')
		except:
			print('Ha ocurrido un error')
		try:
			self.cursor.execute("""
				CREATE TABLE categorias (
					categoria_ID INTEGER PRIMARY KEY AUTOINCREMENT,
					categoria_Nombre VARCHAR(50) NOT NULL UNIQUE
				)
			""")
		except sqlite3.OperationalError:   
			print('La Tabla categorias se ha creado correctamente')
		except:
			print('Ha ocurrido un error')

		#Intenta crear el usuario admin si existe ya procede
		try:
			self.cursor.execute("""
				INSERT INTO empleados VALUES (null,'admin', 'admin', 'System_Admin', 100100000, 'No Disponible', 1, 1111111111, 'No Disponible' )
			""")
			self.conexion.commit()
		except:
			print('Usuario admin ya existe')
	
	def run_query(self, query, parameters = ()):
		resultado = self.cursor.execute(query, parameters)
		self.connect.commit()
		return resultado
	def db_close(self):
		self.connect.close()