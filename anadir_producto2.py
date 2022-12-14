from tkinter import *
import utilidades
import db_conection

def ventana(root, my_treeview, articulos_var, subtotal, cantidad_articulos, precios_articulos):
    articulos_var
    root = root
    my_treeview = my_treeview
    cantidad_articulos = []
    precios_articulos = []
    productos_por_categoria = {}
    my_db = db_conection.Db_connection('sistema')
    categorias = my_db.run_query('SELECT * FROM categorias').fetchall()
    productos = my_db.run_query('SELECT * FROM productos').fetchall()
    
    for categoria in categorias:
        productos_por_categoria[categoria[0]] = []
        
    for producto in productos:
        productos_por_categoria[producto[4]].append(producto)
    print(productos_por_categoria)
    cantidad = IntVar()
    ventana_de_anadir_producto = Toplevel(root)
    ventana_de_anadir_producto.title('Procesos')
    ventana_de_anadir_producto.geometry("750x600")
    ventana_de_anadir_producto.resizable(0, 0)
    utilidades.center(ventana_de_anadir_producto)
    Label(ventana_de_anadir_producto, text = 'Selecciona un producto', font = 'Arial 16 bold').grid(row = 0, column = 0, pady = (20, 0))
    campo = Frame(ventana_de_anadir_producto)
    campo.grid(row = 1, column = 0, columnspan =3, padx = (30, 0), pady = (15, 5))
    treeview = ttk.Treeview(campo, height = 15, style="mystyle.Treeview",selectmode='browse')
    treeview.pack(side = 'left')
    treeview.column("#0", width=680, anchor='c', minwidth = 100, stretch = False)
    verscrlbar = ttk.Scrollbar(campo, orient ="vertical", command = treeview.yview)
    verscrlbar.pack(side = 'right', fill = 'y')
    treeview.configure(yscrollcommand = verscrlbar.set)
    
    item = treeview.insert("", 'end', text="Elemento 1")
    treeview.insert(item, 'end', text="Subelemento 1")
    items = []
    for categoria in categorias:
        item = treeview.insert("", 'end', text=f"{categoria[1]}")
        for producto in productos_por_categoria[categoria[0]]:
            treeview.insert(item, 'end', text=f"{producto[1]}")
            
        items.append(item)
    print(items)
    Label(ventana_de_anadir_producto, text = 'Cantidad:', font = 'Arial 12').grid(row = 2, column = 0, sticky = 'e', padx = (0, 5))
    Entry(ventana_de_anadir_producto, font = 'Arial 11', textvariable = cantidad, width = 6).grid(row = 2, column = 1, sticky = 'w')
    Button(ventana_de_anadir_producto, text = 'Añadir', command = lambda: añadirProducto(treeview, cantidad, my_treeview, articulos_var, cantidad_articulos, subtotal, precios_articulos)).grid(row = 3, column = 1)
    ventana_de_anadir_producto.grab_set()
    root.wait_window(ventana_de_anadir_producto)

def añadirProducto(treeview, cantidad, my_treeview, articulos_var, cantidad_articulos, subtotal,precios_articulos):
    my_db = db_conection.Db_connection('sistema')
    treeview.item(treeview.selection())['values']
    # except IndexError:
        # print('Por favor seleccione un producto')
        # return
    nombre = treeview.item(treeview.selection())['text']
    print(nombre)
    precio = my_db.run_query(f"SELECT producto_Precio FROM productos WHERE producto_Nombre LIKE '{nombre}'").fetchone()
    print(precio, type(precio))
    print(cantidad.get(), type(cantidad.get()))
    my_treeview.insert("",'end',text= f"{nombre}", values=(
        cantidad.get(),
        nombre,
        precio,
        (int(cantidad.get()) * float((precio[0]))
    )))
    cantidad_articulos.append(cantidad.get())
    precios_articulos.append(int(cantidad.get()) * float((precio[0])))
        
    articulos_var.set(contar_articulos(cantidad_articulos))
    subtotal.set(contar_precios(precios_articulos))
    
def contar_articulos(cantidad_articulos):
    # contar articulos
    contador = 0
    for num in cantidad_articulos:
        contador += num
    
    return contador

def contar_precios(precios_articulos):
    contador = 0
    for precio in precios_articulos:
        contador += precio
    
    return contador