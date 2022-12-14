import db_conection
from tkinter import *
from tkinter import messagebox as MessageBox
import utilidades



class Login:
    def __init__(self):
        self.color_fondo = 'steel blue'
        self.usuario_autenticado = (False, 'No user')
        self.connection = db_conection.Db_connection('sistema')
        try:
            self.seleccion_empleados = self.connection.run_query('SELECT * FROM empleados')
            self.lista_empleados = self.connection.cursor.fetchall()
        except:
            print('No se pudieron obtener los datos de la tabla empleados')
        
    
    def press(self, x = 1):
            self.autenticar(self.valor_usuario.get(), self.valor_password.get())

    def autenticar(self, user_param, password_param):
        #conectamos y accedemos a los datos de la base de datos
        self.user_param = user_param
        self.password_param = password_param

        #Seteamos las variables de validacion
        self.usuario_correcto = False
        self.password_correcto = False

        #comparamos los parametros dados con todos los empleados para acceder al sistema
        for i in range(len(self.lista_empleados)):
            print(self.lista_empleados[i][1], self.user_param)
            if self.lista_empleados[i][1] == self.user_param:
                self.usuario_correcto = True
                print("Usuario correcto")                
                if self.lista_empleados[i][2] == self.password_param:
                    print("password correcto")
                    self.password_correcto = True
                    if (self.usuario_correcto and self.password_correcto):
                        print('Accediste al sistema')
                        self.usuario_autenticado = (True, self.lista_empleados[i])
                        self.root.destroy()
                        break
        
        if self.usuario_correcto == False:
            MessageBox.showwarning("Usuario no encontrado", "El usuario introducido no se encuentra en el sistema.")
            print('Usuario Incorrecto')
        else:
            if self.password_correcto == False:    
                MessageBox.showwarning("Contraseña Incorrecta", "La contraseña introducida es incorrecta.")
                print('Constraseña Incorrecta')

    def show_login(self):
        self.root = Tk()
        self.root.title("Sistema De Facturacion")
        self.root.geometry("470x560")
        self.root.config(background = self.color_fondo)
        self.root.resizable(0,0)
        utilidades.center(self.root)
        
        self.valor_usuario = StringVar()
        self.valor_password = StringVar()
        
        self.user_imagen = PhotoImage(file = 'imagenes/user_img2.png')
        
        Label(self.root, text = "ACCESO AL SISTEMA", font = "Helvetica 18 bold", bg = self.color_fondo, fg = 'white').pack(pady = 10)
        Label(self.root, image = self.user_imagen, bg = self.color_fondo).pack()
        Label(self.root, text = "Usuario:", font = "Helvetica 14 ", bg = self.color_fondo, fg = 'white').pack(pady = 10)
        self.campo_usuario = Entry(self.root, font = "Arial 14",textvariable = self.valor_usuario)
        self.campo_usuario.pack()
        self.campo_usuario.focus()
        
        Label(self.root, text = "Contraseña:", font = "Arial 14", bg = self.color_fondo, fg = 'white').pack(pady = 10)
        self.campo_password = Entry(self.root, font = 'Arial 14', show = '●', textvariable = self.valor_password)
        self.campo_password.pack()
        
        self.boton_iniciar = Button(self.root, text = 'Iniciar sesión', font = 'Arial 14', command= lambda: self.autenticar(self.valor_usuario.get(), self.valor_password.get()),)
        self.boton_iniciar.pack(pady = 15)
        self.root.bind('<Return>', self.press)


        self.root.mainloop()
    

