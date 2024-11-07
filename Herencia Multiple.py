articulos=[]
herramientas=[]
maquinas=[]
articulosElectricos=[]
maquinasHerramientas=[]

def menu():
    print("Bienvenido al sistema de la Ferretería La Tuerca")
    producto= input ("Que producto quiere ingresar: ")
    codigo= input ("Ingrese el codigo: ")
    nombre= input ("Ingrese el nombre: ")
    precio= int (input ("Ingrese el precio: "))

    op= input ("En que categoria quiere agregar el producto: a. Articulos b. Herramientas c. Maquinas d. Articulos Electricos e. Maquinas Herramientas: ")
    if op=="a":
        stock= int (input ("Ingrese el stock: "))
        producto=Articulos(codigo,nombre,precio,stock)
        articulos.append(producto)
        producto.verInformacion()
        producto.debeComprar()
        menu()
    elif op=="b":
        rubro= input ("Ingrese el rubro: ")
        producto=Herramientas(codigo,nombre,precio,rubro)
        herramientas.append(producto)
        producto.verInformacion()
        producto.verRubro()
        menu()
    elif op=="c":
        potencia= int (input ("Ingrese la potencia: "))
        producto=Maquinas(codigo,nombre,precio,potencia)
        maquinas.append(producto)
        producto.verInformacion()
        producto.verPotencia()
        menu()
    elif op=="d":
        tension= (input ("Ingrese la tenison: "))
        producto=ArticulosElectricos(codigo,nombre,precio,tension)
        articulosElectricos.append(producto)
        producto.verInformacion()
        producto.verTension()
        producto.debeComprar()
        menu()
    elif op=="e":
        rubro= input ("Ingrese el rubro: ")
        potencia= int (input ("Ingrese la potencia: "))
        producto=MaquinasHerramientas(codigo,nombre,precio,stock,potencia,rubro)
        maquinasHerramientas.append(producto)
        producto.verInformacion()
        producto.verRubro()
        producto.verPotencia()

    else: 
        print("Ingrese una opcion valida: ")
        menu()

class Productos():
    def _init_(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio

    def verInformacion(self):
        print(self.codigo,self.nombre,self.precio)

class Articulos(Productos):
    def _init_(self,codigo,nombre,precio,stock):
        Productos._init_(self,codigo,nombre,precio)
        self.stock=stock

    def debeComprar(self):
        if self.stock<100:
            print("Debe comprar")

class Herramientas(Productos):
    def _init_(self,codigo,nombre,precio,rubro):
        Productos._init_(self,codigo,nombre,precio)
        self.rubro=rubro

    def verRubro(self):
        print(self.rubro)

class Maquinas(Productos):
    def _init_(self,codigo,nombre,precio,potencia):
        Productos._init_(self,codigo,nombre,precio)
        self.potencia=potencia

    def verPotencia(self):
        if self.potencia>250:
            print("Es de consumo alto")
    
class ArticulosElectricos(Articulos):
    def _init_(self,codigo,nombre,precio,stock,tension):
        Productos._init_(self,codigo,nombre,precio,stock)
        self.tension=tension

    def verTension(self):
        if self.tension<48:
            print("Es de tension alta")

class MaquinasHerramientas(Herramientas,Maquinas):
    def _init_(self,codigo,nombre,precio,stock,potencia,rubro):
        Herramientas._init_(self,codigo,nombre,precio,rubro)
        Maquinas._init_(self,codigo,nombre,precio,potencia)

menu()