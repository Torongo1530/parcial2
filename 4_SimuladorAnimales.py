class Animal:
    def __init__(self, nombre, edad, alimentacion, sonido):
        self.nombre = nombre
        self.edad = edad
        self.alimentacion = alimentacion
        self.sonido = sonido

    def moverse(self):
        print(f"Soy {self.nombre} y me estoy moviendo")

    def comer(self):
        print(f"Soy {self.nombre} y estoy comiendo {self.alimentacion}")

    def emitir_sonido(self):
        print(self.sonido)

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Carne", "Guau")

class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Ratón", "Miau")

perro = Perro("Firulay", 5)
gato = Gato("Misuga", 3)

perro.comer()
perro.emitir_sonido()
perro.moverse()

gato.comer()
gato.emitir_sonido()
gato.moverse()