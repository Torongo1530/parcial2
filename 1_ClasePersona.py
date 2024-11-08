class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
    
    def presentarse(self):
        print(f"\nHola, mi nombre es {self.nombre}, tengo {self.edad} anios y vivo en {self.direccion}\n")

    def modificarAtributos(self):
        nuevoNombre = input("Ingrese el nuevo nombre: ")
        nuevaEdad = input("Ingrese la nueva edad: ")
        nuevaDireccion = input("Ingrese la nueva direccion: ")
        self.nombre = nuevoNombre
        self.edad = nuevaEdad
        self.direccion = nuevaDireccion

Persona1 = Persona("Angel", 24, "Villa Mella")
Persona1.presentarse()
Persona1.modificarAtributos()
Persona1.presentarse()