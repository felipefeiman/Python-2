def menu():
    print("Bienvenidos a Automotores La Rueda")
    op= input("Que desea hacer: a. Agregar autos al sistema b. Ver los autos c. Cotizarlos d. Salir del sistema: ")

    if op=="a":
        agregar()
        menu()
    elif op=="b":
        ver()
        menu()
    elif op=="c":
        cotizar()
        menu()
    elif op=="d":
        print("Gracias por usar nuestro sistema")
        exit
    else:
        print("Opcion incorrecta")
        menu()

autos=[]
class Autos():
    def __init__(self,marca,modelo,costo):
        self.marca=marca
        self.modelo=modelo
        self.costo=costo

def agregar():
    marca= input("Ingrese la marca: ")
    modelo= input("Ingrese el modelo: ")
    costo= int (input("Ingrese el costo: "))

    auto= Autos(marca,modelo,costo)
    autos.append(auto)

def ver():
    for i in autos:
        print(i.marca,i.modelo,i.costo)

def cotizar():
    modelo= input("Que modelo quiere cotizar: ")
    for i in autos:
        if i.modelo==modelo:
            print("El costo en pesos es", i.costo*1000)
            break
    else:
        print("No tenemos ese modelo")

menu()
