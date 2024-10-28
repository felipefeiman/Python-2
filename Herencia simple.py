articulos=[]
herramientas=[]
maquinas=[]
articulosElectricos=[]

print("Bienvenido al sistema de la Ferretería La Tuerca")
def menu():
    producto=("Ingrese el producto que quiere ingresar")
    op= input ("En que categoria quiere agregar el producto: a. Articulos b. Herramientas c. Maquinas d. Articulos Electricos")
    if op=="a":
        articulos.append(producto)
        producto.verInformacion()
        producto.debeComprar()
    elif op=="b":
        herramientas.append(producto)
        producto.verInformacion()
        producto.verRubro()
    elif op=="c":
        maquinas.append(producto)
        producto.verInformacion()
        producto.verPotencia()
    elif op=="d":
        articulosElectricos.append(producto)
        producto.verInformacion()
        producto.verTension()
    else: 
        print("Ingrese una opcion valida")
        menu()

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
        Productos.__init__(self,codigo,nombre,precio,stock)
        self.tension=tension

    def verTension(self):
        if self.tension<48:
            print("Es de tension alta")

menu()
