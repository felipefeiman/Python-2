class Pizzeras():
    altura=2
    diametro=30
    material="acero"

class Vasos():
    altura=10
    diametro=5
    material="vidrio"

    def calcularCarga(self):
        self.carga= self.altura*self.diametro
        print("La capacidad de carga es de",self.carga)

class Ollas():
    altura=20
    diametro=40
    material="acero"

    def calcularCarga(self):
        self.carga= self.altura*self.diametro
        print("La capacidad de carga es de",self.carga)


pizzera1=Pizzeras()
pizzera2=Pizzeras()
pizzera3=Pizzeras()
pizzera4=Pizzeras()
pizzera5=Pizzeras()


vaso1=Vasos()
vaso2=Vasos()
vaso3=Vasos()
vaso4=Vasos()
vaso5=Vasos()

vaso2.altura=15
vaso3.altura=15
vaso3.diametro=4.5
vaso4.diametro=4.5
vaso4.material="plastico"


olla1=Ollas()
olla2=Ollas()
olla3=Ollas()
olla4=Ollas()
olla5=Ollas()

olla2.altura=5
olla2.diametro=15
olla2.material="alumino"

olla3.altura=15
olla3.diametro=20
olla3.material="barro"

olla4.altura=10
olla4.diametro=25
olla4.material="cobre"

olla5.altura=25
olla5.diametro=35
olla5.material="ceramica"