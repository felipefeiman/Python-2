"""
7. Si selecciona la opción ver datos, el sistema le pedirá el dni del usuario que desea ver. Al ingresarlo le imprimirá todos los datos (nombre, edad, dni y contraseña). En caso que ingrese un dni que no se encuentra en el sistema, informárselo.
"""

nombres=[]

class Usuarios():
    def __init__(self,nombre,dni,edad,__cont2):
        self.nombre=nombre
        self.dni=dni
        self.edad=edad
        self.__cont2=__cont2

    def contraseña():
        global __cont2

        __cont1= input("Ingrese una contraseña: ")
        __cont2= input("Confirme la contraseña: ")
        if __cont1==__cont2:
            print("Contraseña almacenada correctamente")
        else: 
            while __cont1!=__cont2:
                print("Contraseñas distintas") 

    def verr():
        ver= input ("Ingrese el dni del usuario que desea ver: ")
        for i in nombres: 
            if i.nombre== ver:
                print(nombre,dni,edad,__cont2)
        else: 
            print("Ingrese un dni que este en el sistema")
            
        
   

def menu():
    print("Bienvenido a la ANSES")
    op= input ("Que quiere hacer: a. Registrarse b. Ver usuarios c. Ver datos d. Borrar usuario e. Salir del sistema")
    if op=="a":
        registrarse()
        usuario.contraseña()
        menu()
    elif op=="b":
        print(nombres)
        menu()
    elif op=="c": 

        menu()
    elif op=="d":
        borrarr()
        menu()
    elif op=="e":
        print("Gracias por usar nuestro sistema")
        exit()
    else: 
        print("Ingrese una opcion correcta")
        menu()


def registrarse():
        global usuario,dni,edad,nombre
        try:
            nombre= input ("Ingrese su nombre: ")
            dni= input ("Ingrese su dni: ")
            edad= int (input ("Ingrese su edad: "))
        
            usuario=Usuarios(nombre,dni, edad)
            nombres.append(usuario)
        except ValueError:
            print("La edad y el dni deben ser numeros")
            registrarse()

def borrarr():
    borrar= input ("Ingrese el dni del usuario que desea borrar: ")
    for i in nombres: 
        if i.nombre== borrar:
            nombres.remove(i)
    else: 
        print("Ingrese un nombre que este en el sistema")
        borrarr()


        
