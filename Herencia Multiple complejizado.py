articulos=[]
herramientas=[]
maquinas=[]
articulosElectricos=[]
maquinasHerramientas=[]
todos=[articulos, herramientas, maquinas, articulosElectricos, maquinasHerramientas]

class Productos():
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio

    def verInformacion(self):
        print(self.codigo,self.nombre,self.precio)
class Articulos(Productos):
    def __init__(self,codigo,nombre,precio,stock):
        Productos.__init__(self,codigo,nombre,precio)
        self.stock=stock

    def debeComprar(self):
        if self.stock<100:
            print("Debe comprar")
class Herramientas(Productos):
    def __init__(self,codigo,nombre,precio,rubro):
        Productos.__init__(self,codigo,nombre,precio)
        self.rubro=rubro

    def verRubro(self):
        print(self.rubro)
class Maquinas(Productos):
    def __init__(self,codigo,nombre,precio,potencia):
        Productos.__init__(self,codigo,nombre,precio)
        self.potencia=potencia

    def verPotencia(self):
        if self.potencia>250:
            print("Es de consumo alto")
class ArticulosElectricos(Articulos):
    def __init__(self,codigo,nombre,precio,stock,tension):
        Articulos.__init__(self,codigo,nombre,precio,stock)
        self.tension=tension

    def verTension(self):
        if self.tension<48:
            print("Es de tension alta")
class MaquinasHerramientas(Herramientas,Maquinas):
    def __init__(self,codigo,nombre,precio,potencia,rubro):
        Herramientas.__init__(self,codigo,nombre,precio,rubro)
        Maquinas.__init__(self,codigo,nombre,precio,potencia)


def menu():
    print("Bienvenido al sistema de la Ferretería La Tuerca")

    global stock, rubro, potencia, tension, producto, codigo, nombre, precio
    producto= input ("Que producto quiere ingresar: ") .lower()
    codigo= input ("Ingrese el codigo: ")
    nombre= input ("Ingrese el nombre: ") .lower()
    precio= int (input ("Ingrese el precio: "))

    op= input ("En que categoria quiere crear el producto: a. Articulos b. Herramientas c. Maquinas d. Articulos Electricos e. Maquinas Herramientas: ") .lower()
    if op=="a":
        stock= int (input ("Ingrese el stock: "))
        producto=Articulos(codigo,nombre,precio,stock)
        articulos.append(producto)
        producto.verInformacion()
        producto.debeComprar()
    elif op=="b":
        rubro= input ("Ingrese el rubro: ")
        producto=Herramientas(codigo,nombre,precio,rubro)
        herramientas.append(producto)
        producto.verInformacion()
        producto.verRubro()
    elif op=="c":
        potencia= int (input ("Ingrese la potencia: "))
        producto=Maquinas(codigo,nombre,precio,potencia)
        maquinas.append(producto)
        producto.verInformacion()
        producto.verPotencia()
    elif op=="d":
        stock= int (input ("Ingrese el stock: "))
        tension= int (input ("Ingrese la tenison: "))
        producto=ArticulosElectricos(codigo,nombre,precio,stock,tension)
        articulosElectricos.append(producto)
        producto.verInformacion()
        producto.verTension()
        producto.debeComprar()
    elif op=="e":
        rubro= input ("Ingrese el rubro: ")
        potencia= int (input ("Ingrese la potencia: "))
        producto=MaquinasHerramientas(codigo,nombre,precio,stock,potencia,rubro)
        maquinasHerramientas.append(producto)
        producto.verInformacion()
        producto.verRubro()
        producto.verPotencia()
    else: 
        print("Ingrese una opcion valida")
        menu()

    op= input ("Que quiere hacer: a. Ver productos b. Modificar productos c. Eliminar productos d. Salir del sistema: ") .lower()
    if op=="a":
        verProductos()
        menu()
    elif op=="b":
        modificarProductos()
        menu()
    elif op=="c":
        eliminarProductos()
        menu()
    elif op=="d":
        exit()
    else: 
        print("Ingrese una opcion valida")
        menu()
   
def verProductos():
    ver= input (("De que categoria quiere ver el producto: a. Articulos b. Herramientas c. Maquinas d. Articulos Electricos e. Maquinas Herramientas: "))
    if ver=="a":
        print(articulos)
    elif ver=="b":
        print(herramientas)
    elif ver=="c":
        print(maquinas)
    elif ver=="d":
        print(articulosElectricos)
    elif ver=="e":
        print(maquinasHerramientas)
    else:
        print("Solo se pueden ver productos que esten en el catalogo")
        verProductos()

def modificarProductos():
    op= input (("Desea modificar caracteristicas a. Generales b. Especificas c. Ambas: ")) .lower()
    global stock, rubro, potencia, tension, producto, codigo, nombre, precio
    if op=="a":
        producto= input ("Modifique el producto: ") .lower()
        codigo= input ("Modifique el codigo: ")
        nombre= input ("Modifique el nombre: ") .lower()
        precio= int (input ("Modifique el precio: "))
    elif op=="b":
        for i in todos:
            if i==articulos:
                stock= int (input ("Modifique el stock: "))
                break
            elif i==herramientas:
                rubro= input ("Modifique el rubro: ") 
            elif i==maquinas:
                potencia= int (input ("Modifique la potencia: "))
            elif i==articulosElectricos:
                tension= int(input ("Modifique la tenison: "))
            elif i==maquinasHerramientas:
                rubro= input ("Modifique el rubro: ") 
                potencia= int (input ("Modifique la potencia: "))
        else:
            print("Solo se pueden modificar productos que esten en el catalogo")
            todos()  
    elif op=="c":
        producto= input ("Modifique el producto: ") .lower()
        codigo= input ("Modifique el codigo: ")
        nombre= input ("Modifique el nombre: ") .lower()
        precio= int (input ("Modifique el precio: "))
        for i in todos:
            if i==articulos:
                stock= int (input ("Modifique el stock: "))
                break
            elif i==herramientas:
                rubro= input ("Modifique el rubro: ")
                break 
            elif i==maquinas:
                potencia= int (input ("Modifique la potencia: "))
                break
            elif i==articulosElectricos:
                stock= int (input ("Modifique el stock: "))
                tension= (input ("Modifique la tenison: "))
                break
            elif i==maquinasHerramientas:
                rubro= input ("Modifique el rubro: ") 
                potencia= int (input ("Modifique la potencia: "))
                break
        else:
            print("Solo se pueden modificar productos que esten en el catalogo")
            todos()
        

def eliminarProductos():
    borrar= input ("De que categoria/s quiere eliminar el producto: a. Articulos b. Herramientas c. Maquinas d. Articulos Electricos e. Maquinas Herramientas: ") .lower()
    print("Los Productos disponibles son: ", articulos, herramientas, maquinas, articulosElectricos, maquinasHerramientas)
    borrar= input("Que producto desea borrar: ") .lower()
    if borrar not in articulos+herramientas+maquinas+articulosElectricos+maquinasHerramientas:
        print("Debe ingresar un articulo que este en el catalogo")
        eliminarProductos()
    if borrar in articulos:
        articulos.remove(borrar)
        print("Se borro el producto")
    if borrar in herramientas:
        herramientas.remove(borrar)
        print("Se borro el producto")
    if borrar in maquinas:
        maquinas.remove(borrar)        
        print("Se borro el producto")
    if borrar in articulosElectricos:
        articulosElectricos.remove(borrar)        
        print("Se borro el producto")
    if borrar in maquinasHerramientas:
        maquinasHerramientas.remove(borrar)        
        print("Se borro el producto")


menu()