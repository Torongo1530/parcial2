class Hotel:
    def __init__(self):
        self.reserva = []
        self.habitacionesDisponibles = 5

    def reservar(self, nombre):
        if self.habitacionesDisponibles > 0:
            if nombre not in self.reserva:
                print(f"Habitacion reservada! Bienvenido {nombre}")
                self.habitacionesDisponibles-=1
                self.reserva.append(nombre)
            else:
                print(f"El nombre {nombre} ya ha sido registrado\n")
        else:
            print(f"Lo siento {nombre}, ya no hay habitaciones disponibles\n")

    def cancelar(self, nombre):
        if nombre in self.reserva:
            self.reserva.remove(nombre)
            self.habitacionesDisponibles+=1
            print(f"{nombre} su reserva ha sido eliminada\n")
        else:
            print(f"No hay ninguna reserva con el nombre {nombre}\n")
    
    def mostrarDisponibilidad(self):
        print(f"Cantidad de habitaciones disponibles: {self.habitacionesDisponibles}\n")
    
    def usuariosRegistrados(self):
        print("---Lista de usuarios registrados actualmente---\n")
        for i in self.reserva:
            print(i)

#Objeto Cliente
Cliente = Hotel()

#Mostrar las habitaciones disponibles luego de que mirian cancelo su reserva
Cliente.mostrarDisponibilidad()

#Reservando los clientes
Cliente.reservar("Angel")
Cliente.reservar("Deiby")
Cliente.reservar("Mirian")
Cliente.reservar("Isaac")
Cliente.reservar("Isaac") #El nombre de isaac ya fue registrado anteriormente
Cliente.reservar("Josue")
Cliente.reservar("Manuel") #No hayhabitacion disponible para manuel

#Cancelando las reservas de los clientes
Cliente.cancelar("Mirian")

#Mostrar las habitaciones disponibles luego de que mirian cancelo su reserva
Cliente.mostrarDisponibilidad()

#Mostrando todos los usuarios registrados
Cliente.usuariosRegistrados()
