class Coche:
    def __init__(self, modelo, color, anio):
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.encendido = False

    def arrancar(self):
        if self.encendido == False:    
            print(f"Arrancando el coche.")
            self.encendido = True
        else:
            print("El vehiculo ya esta encendido")

    def apagar(self):
        if self.encendido == True:
            print(f"Apagando el coche.")
            self.encendido = False
        else:
            print("El vehiculo ya esta apagado")

    def cambiarColor(self):
        nuevoColor = input("Ingrese el nuevo color del coche: ")
        self.color = nuevoColor

    def detallesCoche(self):
        print(f"Soy un {self.modelo} {self.color} del anio {self.anio}")
    
coche1 = Coche("Toyota", "Gris", 2015)
coche1.arrancar()
coche1.apagar()
coche1.detallesCoche()
coche1.cambiarColor()
coche1.detallesCoche()